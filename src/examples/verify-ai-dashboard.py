"""Synthetic-only integration check. Requires aw-server, aw-client, playwright.

Run beside ai-dashboard-summary.py and ai-dashboard.html after installing
Playwright Chromium. No existing ActivityWatch instance is used.
"""

import importlib.util
import json
import os
import tempfile
import threading
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlsplit

from aw_client import ActivityWatchClient
from aw_core.models import Event
from aw_server.server import AWFlask
from flask import request
from playwright.sync_api import sync_playwright
from werkzeug.serving import make_server

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "summary", ROOT / "ai-dashboard-summary.py"
)
summary_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(summary_module)
summarize = summary_module.summarize


def verify(client):
    t = datetime(2024, 1, 15, 8, tzinfo=timezone.utc)
    # Insert the longer prefix match first to catch substring bucket discovery.
    for host in ["fixture-a-other", "fixture-a", "fixture-b"]:
        for watcher, kind in [("window", "currentwindow"), ("afk", "afkstatus")]:
            client.create_bucket(f"aw-watcher-{watcher}_{host}", event_type=kind)
        client.insert_events(
            f"aw-watcher-window_{host}",
            [
                Event(
                    timestamp=t,
                    duration=timedelta(hours=1),
                    data={"app": "Code", "title": "synthetic"},
                ),
                Event(
                    timestamp=t + timedelta(hours=1),
                    duration=timedelta(hours=1),
                    data={"app": "Firefox", "title": "synthetic"},
                ),
            ],
        )
        client.insert_events(
            f"aw-watcher-afk_{host}",
            [
                Event(
                    timestamp=t,
                    duration=timedelta(minutes=30),
                    data={"status": "not-afk"},
                ),
                Event(
                    timestamp=t + timedelta(minutes=30),
                    duration=timedelta(minutes=30),
                    data={"status": "afk"},
                ),
                Event(
                    timestamp=t + timedelta(hours=1),
                    duration=timedelta(hours=1),
                    data={"status": "not-afk"},
                ),
            ],
        )
    # The similarly named host has different AFK coverage and must not be chosen.
    client.delete_bucket("aw-watcher-afk_fixture-a-other")
    client.create_bucket("aw-watcher-afk_fixture-a-other", event_type="afkstatus")
    client.insert_events(
        "aw-watcher-afk_fixture-a-other",
        [Event(timestamp=t, duration=timedelta(hours=2), data={"status": "afk"})],
    )
    client.set_setting(
        "classes",
        [
            {"name": ["Coding"], "rule": {"type": "regex", "regex": "Code"}},
            {"name": ["Communication"], "rule": {"type": "regex", "regex": "Firefox"}},
        ],
    )
    a = summarize(client, "fixture-a", t, t + timedelta(hours=2))
    assert (a["active_seconds"], a["afk_seconds"], a["tracked_seconds"]) == (
        5400,
        1800,
        7200,
    ), a
    assert a["categories"] == [
        {"name": ["Coding"], "seconds": 1800},
        {"name": ["Communication"], "seconds": 3600},
    ], a
    assert a["apps"] == [
        {"app": "Code", "seconds": 1800},
        {"app": "Firefox", "seconds": 3600},
    ], a
    # Both devices overlap completely; selecting A must not include B.
    assert (
        summarize(client, "fixture-b", t, t + timedelta(hours=2))["active_seconds"]
        == 5400
    )
    offset = timezone(timedelta(hours=2))
    assert (
        summarize(
            client,
            "fixture-a",
            t.astimezone(offset),
            (t + timedelta(hours=2)).astimezone(offset),
        )["active_seconds"]
        == 5400
    )
    clipped = summarize(
        client, "fixture-a", t + timedelta(minutes=15), t + timedelta(minutes=75)
    )
    assert (
        clipped["active_seconds"],
        clipped["afk_seconds"],
        clipped["tracked_seconds"],
    ) == (1800, 1800, 3600), clipped
    for start, end in [(t, t), (t + timedelta(days=1), t + timedelta(days=1, hours=1))]:
        empty = summarize(client, "fixture-a", start, end)
        assert (
            empty["active_seconds"]
            == empty["afk_seconds"]
            == empty["tracked_seconds"]
            == 0
        ), empty
    for host, start, end in [
        ("fixture-a", t.replace(tzinfo=None), t),
        ("fixture-a", t + timedelta(hours=1), t),
        ("missing", t, t + timedelta(hours=1)),
    ]:
        try:
            summarize(client, host, start, end)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid host/range accepted")
    # A window interval without any AFK coverage remains unknown.
    gap = t + timedelta(days=2)
    client.insert_events(
        "aw-watcher-window_fixture-a",
        [Event(timestamp=gap, duration=timedelta(minutes=10), data={"app": "Code"})],
    )
    unknown = summarize(client, "fixture-a", gap, gap + timedelta(minutes=10))
    assert (
        unknown["active_seconds"],
        unknown["afk_seconds"],
        unknown["unknown_seconds"],
    ) == (0, 0, 600), unknown
    return a, empty


def verify_browser(summary, empty, base_url):
    destinations, errors = [], []
    with sync_playwright() as p, tempfile.TemporaryDirectory() as tmp:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.on("request", lambda req: destinations.append(req.url))
        page.on("pageerror", lambda err: errors.append(str(err)))
        page.on("websocket", lambda ws: destinations.append(ws.url))
        try:
            page.goto((ROOT / "ai-dashboard.html").as_uri())
            assert page.locator("#active-seconds").inner_text() == "9600"
            assert page.locator("#afk-seconds").inner_text() == "600"
            assert page.locator("#tracked-seconds").inner_text() == "10200"
            for key, value in [
                ("Coding", "7200"),
                ("Communication", "1800"),
                ("Uncategorized", "600"),
            ]:
                row = page.locator("#categories .row").filter(has_text=key)
                assert value in row.inner_text()

            def load(data):
                path = Path(tmp) / "summary.json"
                path.write_text(json.dumps(data))
                page.locator("#summary-file").set_input_files([])
                page.locator("#summary-file").set_input_files(str(path))
                page.wait_for_timeout(100)

            load({**summary, "active_seconds": 3599.6})
            assert page.locator("#active-fmt").inner_text() == "1h 00m 00s"
            load(summary)
            assert page.locator("#active-seconds").inner_text() == "5400"
            assert page.locator("#afk-seconds").inner_text() == "1800"
            assert "+00:00" in page.locator("#range").inner_text()
            load(empty)
            assert page.locator("#active-seconds").inner_text() == "0"
            assert "No activity" in page.locator("#categories").inner_text()
            load({**summary, "active_seconds": -1})
            assert page.locator("#error").is_visible()
            load({**summary, "end": "2024-01-01T00:00:00Z"})
            assert page.locator("#error").is_visible()
            bad = Path(tmp) / "bad.json"
            bad.write_text("{invalid")
            page.locator("#summary-file").set_input_files(str(bad))
            page.wait_for_timeout(100)
            assert page.locator("#error").is_visible()
            load(
                {
                    **summary,
                    "hostname": "<img src=https://example.invalid/ onerror=alert(1)>",
                }
            )
            assert page.locator("#host").inner_text().startswith("<img")
            assert page.locator("img").count() == 0
            # Python custom-static path, no CORS changes or production listener.
            page.goto(base_url + "/pages/dashboard/")
            assert page.locator("#active-seconds").inner_text() == "9600"
            page.set_viewport_size({"width": 390, "height": 844})
            assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")
            # Optional caller-controlled evidence directory; default has no image output.
            if os.environ.get("AW_GUIDE_SCREENSHOT"):
                page.screenshot(path=os.environ["AW_GUIDE_SCREENSHOT"], full_page=True)
            assert not errors, errors
            allowed = {base_url + "/pages/dashboard/"}
            assert all(
                urlsplit(url).scheme == "file" or url in allowed for url in destinations
            ), destinations
        finally:
            browser.close()
    return destinations


def main():
    # Default AWFlask datastore is in-memory; no existing database is opened.
    static_dir = tempfile.TemporaryDirectory()
    (Path(static_dir.name) / "index.html").write_bytes(
        (ROOT / "ai-dashboard.html").read_bytes()
    )
    app = AWFlask(
        "127.0.0.1", testing=True, custom_static={"dashboard": static_dir.name}
    )
    requests = []
    app.before_request(lambda: requests.append((request.method, request.path)))
    server = make_server("127.0.0.1", 0, app)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base_url = f"http://127.0.0.1:{server.server_port}"
    client = ActivityWatchClient(
        "synthetic-guide-verification", host="127.0.0.1", port=server.server_port
    )
    try:
        summary, empty = verify(client)
        # Separate setup writes from the exporter's permitted read calculations.
        requests.clear()
        summarize(
            client,
            "fixture-a",
            datetime(2024, 1, 15, 8, tzinfo=timezone.utc),
            datetime(2024, 1, 15, 10, tzinfo=timezone.utc),
        )
        assert all(
            method == "GET" or (method == "POST" and path == "/api/0/query/")
            for method, path in requests
        ), requests
        exporter_requests = list(requests)
        destinations = verify_browser(summary, empty, base_url)
        print(
            json.dumps(
                {
                    "status": "PASS",
                    "summary": summary,
                    "exporter_requests": exporter_requests,
                    "browser_destinations": destinations,
                },
                indent=2,
            )
        )
    finally:
        server.shutdown()
        thread.join()
        static_dir.cleanup()


if __name__ == "__main__":
    main()
