"""Export one desktop host's bounded, canonical activity as a local summary.

Requires aw-client. Never sends events to a model or writes to the AW API.
"""

import argparse
import json
from datetime import datetime, timedelta

from aw_client import ActivityWatchClient
from aw_client.classes import default_classes
from aw_client.queries import DesktopQueryParams, canonicalEvents


def summarize(client, hostname, start, end):
    if start.utcoffset() is None or end.utcoffset() is None:
        raise ValueError("Use ISO timestamps with explicit timezone offsets")
    if end < start:
        raise ValueError("End must not precede start")
    summary = {
        "hostname": hostname,
        "start": start.isoformat(),
        "end": end.isoformat(),
        "categories": [],
        "apps": [],
        "active_seconds": 0,
        "afk_seconds": 0,
        "tracked_seconds": 0,
        "unknown_seconds": 0,
    }
    if start == end:
        return summary
    buckets = client.get_buckets()
    window = f"aw-watcher-window_{hostname}"
    afk = f"aw-watcher-afk_{hostname}"
    if window not in buckets or afk not in buckets:
        raise ValueError("Select one host with both window and AFK buckets")
    try:
        settings = client.get_setting("classes")
    except Exception as exc:
        # Only absent settings are expected; connection and other errors must surface.
        if getattr(getattr(exc, "response", None), "status_code", None) != 404:
            raise
        settings = None
    classes = (
        [(c["name"], c["rule"]) for c in settings] if settings else default_classes
    )
    # Explicit classes avoid aw-client's implicit lookup on the default server.
    query = canonicalEvents(
        DesktopQueryParams(bid_window=window, bid_afk=afk, classes=classes)
    )
    # canonicalEvents uses substring-based find_bucket(); bind the exact IDs
    # already verified above so similarly named synced hosts cannot win.
    for bucket in (window, afk):
        query = query.replace(f'find_bucket("{bucket}")', json.dumps(bucket))
    query += "\nRETURN = events;"
    active = client.query(query, [(start, end)])[0]
    # These queries do not mutate data. POST /query/ is a read computation,
    # not an HTTP-method-based permission boundary.
    raw_query = f"windows = query_bucket({json.dumps(window)});"
    afk_query = (
        raw_query
        + f" afk = query_bucket({json.dumps(afk)});"
        + ' afk = filter_keyvals(afk, "status", ["afk"]);'
        + " RETURN = filter_period_intersect(windows, afk);"
    )
    raw = client.query(raw_query + " RETURN = windows;", [(start, end)])[0]
    away = client.query(afk_query, [(start, end)])[0]

    # Bucket queries return intersecting events, not necessarily clipped events.
    # Canonical queries also flood intervals; clip before aggregating durations.
    def clipped(events):
        result = []
        for event in events:
            timestamp = datetime.fromisoformat(
                event["timestamp"].replace("Z", "+00:00")
            )
            stop = timestamp + timedelta(seconds=event["duration"])
            seconds = max(0, (min(stop, end) - max(timestamp, start)).total_seconds())
            if seconds:
                result.append({**event, "duration": seconds})
        return result

    active, raw, away = clipped(active), clipped(raw), clipped(away)
    categories = {}
    apps = {}
    for event in active:
        seconds = event["duration"]
        category = tuple(event["data"].get("$category", ["Uncategorized"]))
        app = event["data"].get("app", "unknown")
        categories[category] = categories.get(category, 0) + seconds
        apps[app] = apps.get(app, 0) + seconds
    summary.update(
        categories=[
            {"name": list(k), "seconds": v} for k, v in sorted(categories.items())
        ],
        apps=[{"app": k, "seconds": v} for k, v in sorted(apps.items())],
        active_seconds=sum(e["duration"] for e in active),
        afk_seconds=sum(e["duration"] for e in away),
        tracked_seconds=sum(e["duration"] for e in raw),
    )
    summary["unknown_seconds"] = max(
        0,
        summary["tracked_seconds"] - summary["active_seconds"] - summary["afk_seconds"],
    )
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("hostname")
    parser.add_argument("start", type=datetime.fromisoformat)
    parser.add_argument("end", type=datetime.fromisoformat)
    parser.add_argument("--port", type=int, default=5666)
    args = parser.parse_args()
    client = ActivityWatchClient("local-dashboard", host="127.0.0.1", port=args.port)
    print(json.dumps(summarize(client, args.hostname, args.start, args.end), indent=2))


if __name__ == "__main__":
    main()
