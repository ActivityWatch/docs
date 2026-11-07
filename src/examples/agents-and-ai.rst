ActivityWatch with agents and AI
================================

ActivityWatch can be useful context for AI assistants because it records what you
actually did on your computer. The safest workflow is to keep ActivityWatch data
local, reduce it to a small summary, review that summary, and only then decide
whether any model should see it.

Start with categorized summaries, not raw event exports. Window titles, browser
URLs, document names, and chat subjects can contain sensitive information.

Recommended workflow
--------------------

1. Pick a bounded time range, such as the last work session or the current day.
2. Start from canonical events so AFK time and category rules are applied.
3. Aggregate locally by category, app, domain, or coarse timeline block.
4. Remove or reduce sensitive fields before model access.
5. Review the exact payload that will be sent.
6. Prefer local models or an agent you already run locally. Use third-party
   provider upload only when you understand what data is included.

Good questions for an assistant are specific:

* "Summarize my work since 09:00."
* "Which uncategorized activities should become category rules?"
* "Prepare a standup note from today's coding and communication blocks."

Avoid broad prompts such as "analyze my life" or "send all my ActivityWatch data
to a model." They create large payloads, weaker answers, and unnecessary privacy
risk.

Get canonical activity
----------------------

If you have ``aw-client`` installed, the canonical query is the easiest starting
point:

.. code-block:: sh

   aw-client canonical HOSTNAME --start 2026-08-03T08:00:00 --stop 2026-08-03T12:00:00 --cache

Replace ``HOSTNAME`` with the hostname suffix used in your buckets. Canonical
events use the same kind of processing as the ActivityWatch web UI: active time
filtering, event merging, and categorization.

You can also use the Python client directly:

.. code-block:: python

   import socket
   from datetime import datetime

   from aw_client import ActivityWatchClient
   from aw_client.queries import DesktopQueryParams, canonicalEvents

   client = ActivityWatchClient("agent-summary", testing=False)
   start = datetime.fromisoformat("2026-08-03T08:00:00").astimezone()
   end = datetime.fromisoformat("2026-08-03T12:00:00").astimezone()
   hostname = socket.gethostname()

   query = canonicalEvents(
       DesktopQueryParams(
           bid_window=f"aw-watcher-window_{hostname}",
           bid_afk=f"aw-watcher-afk_{hostname}",
       )
   )
   events = client.query(f"{query}\nRETURN = events;", [(start, end)])[0]

   category_seconds = {}
   app_seconds = {}
   for event in events:
       seconds = event["duration"]
       category = tuple(event["data"].get("$category", ["Uncategorized"]))
       app = event["data"].get("app", "unknown")
       category_seconds[category] = category_seconds.get(category, 0) + seconds
       app_seconds[app] = app_seconds.get(app, 0) + seconds

   print("Categories")
   for category, seconds in sorted(category_seconds.items(), key=lambda item: -item[1]):
       print(f"{' / '.join(category)}: {seconds / 3600:.2f}h")

   print("Apps")
   for app, seconds in sorted(app_seconds.items(), key=lambda item: -item[1]):
       print(f"{app}: {seconds / 3600:.2f}h")

This produces a bounded, AFK-filtered summary without giving a model raw window
titles or raw event history.

Compact context example
-----------------------

A small provider-neutral context payload is usually enough:

.. code-block:: json

   {
     "source": "activitywatch",
     "range": {
       "start": "2026-08-03T08:00:00",
       "end": "2026-08-03T12:00:00"
     },
     "totals": {
       "active_seconds": 12600,
       "afk_seconds": 1800
     },
     "categories": [
       {"name": ["Coding"], "seconds": 7200},
       {"name": ["Communication"], "seconds": 1800}
     ],
     "apps": [
       {"app": "Code", "seconds": 5400},
       {"app": "Firefox", "seconds": 2400}
     ],
     "redaction": {
       "window_titles": "omitted",
       "urls": "domain_only"
     }
   }

Keep durations as seconds and timestamps as ISO 8601 strings. Preserve nested
categories as arrays. Include the redaction policy so the assistant knows what it
can and cannot infer from the payload.

Sensitive fields
----------------

Safe defaults:

* category totals
* app totals
* domain-only browser totals
* coarse timeline blocks
* active and AFK totals

Review carefully before including:

* full window titles
* full URLs
* document names
* chat or email subjects
* raw bucket exports
* long timeline histories

If you use a hosted model, make the boundary explicit before sending data:

.. code-block:: text

   This will send 4 hours of aggregated ActivityWatch data to the selected provider.
   Included: category totals, app totals, domain totals.
   Excluded: window titles, full URLs, raw events.

Local-first workflow
--------------------

For local summarization:

1. Generate the compact context locally with ``aw-client`` or the Python client.
2. Review the payload.
3. Pass only the compact context to a local model or local assistant runtime.
4. Ask for a short answer with a narrow task, such as a standup summary or
   category-rule suggestions.

For category-rule assistance, send examples of uncategorized app/title patterns
only after removing private names. Ask the assistant to propose rules, then add
them manually in ActivityWatch's categorization settings.

Agent and tool workflow
-----------------------

Agents can access ActivityWatch through several layers:

* Export: good for offline analysis and backups. See :doc:`../features/exporting-data`.
* Python client: good for scripts and local summarization. See :doc:`working-with-data`.
* Query API: good for custom local tools. See :doc:`../api/rest`.
* MCP or other agent tooling: good when your assistant supports tool calls.

The same privacy rule applies to all of them: aggregate and redact before model
access. Do not give an agent write access or raw historical exports unless the
workflow really needs it.

Third-party provider upload
---------------------------

Using a third-party model provider is a user choice, not the default
ActivityWatch workflow. Before uploading data:

* prefer aggregated summaries over raw events
* remove titles and full URLs unless they are necessary
* check the provider's retention and training policy
* keep the exact sent payload in your own notes if you need auditability
* use a shorter time range than you would use for local analysis

AI-generated local interfaces
-----------------------------

ActivityWatch's existing collection and query tools can support a different
presentation without rebuilding the tracker. Customization complements improving
the default UI; it should not be necessary to get a usable activity summary.

The smallest integration is an **offline HTML viewer of a local summary**.
Generate code from synthetic data, test it, then optionally load a bounded summary
from your own server. The viewer needs no API connection, CORS changes or build
step. This is a desktop, single-host example, not a multi-device timeline merger.

**What to ask for.** Give your assistant only this prompt and synthetic fixture,
not access to real ActivityWatch events. A locally running agent can still use a
cloud model or tools that upload files; inspect its configuration first:

.. code-block:: text

   Build a single-file HTML dashboard with inline JavaScript and CSS.
   Render the synthetic summary below first. Add a local JSON file picker
   (FileReader) for another summary in the same schema, never an API fetch.
   Show categories, apps, active/AFK/tracked seconds, hostname and the range
   with its explicit timezone offsets. Show zero totals for empty data.
   Keep hosts separate; never sum overlapping devices as personal active time.
   Reject negative/nonfinite durations and invalid/reversed/offset-free dates.
   Treat loaded labels as untrusted text, not HTML.
   No network requests, imports, CDN, external fonts, analytics or telemetry.
   No storage, forwarding or logging of loaded data. No npm or build step.
   Add a CSP meta tag with default-src 'none'; connect-src 'none';
   script-src 'unsafe-inline'; style-src 'unsafe-inline'.

   Synthetic fixture (use this before loading a local summary):
   {
     "hostname": "my-machine",
     "start": "2024-01-15T08:00:00+00:00",
     "end": "2024-01-15T12:00:00+00:00",
     "categories": [
       {"name": ["Coding"], "seconds": 7200},
       {"name": ["Communication"], "seconds": 1800},
       {"name": ["Uncategorized"], "seconds": 600}
     ],
     "apps": [
       {"app": "Code", "seconds": 7200},
       {"app": "Firefox", "seconds": 1800},
       {"app": "Terminal", "seconds": 600}
     ],
     "active_seconds": 9600,
     "afk_seconds": 600,
     "tracked_seconds": 10200
   }

Download the :download:`tested example HTML <ai-dashboard.html>` for a reference
implementation. Save it locally and open it with your browser (``file://``).
The initial sample is synthetic; it does not describe your actual activity.
A prompt is not a guarantee: review and test any newly generated variation too.

Optional: load your own local summary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use Python 3.11 or newer and install ``aw-client``, then download
:download:`ai-dashboard-summary.py <ai-dashboard-summary.py>` to that environment.
Discover your bucket suffix with ``aw-client buckets`` and select **one desktop
hostname** with both ``aw-watcher-window_HOSTNAME`` and
``aw-watcher-afk_HOSTNAME`` buckets. With your existing AW server listening on
loopback port 5666, run:

.. code-block:: sh

   python3 ai-dashboard-summary.py HOSTNAME \
     2024-01-15T08:00:00+00:00 2024-01-15T12:00:00+00:00 > summary.json

Replace the sample dates and hostname. Use explicit offsets (or ``Z``); for a
local day across a daylight-saving transition, the two offsets can differ.
The exporter applies canonical desktop AFK filtering and category rules from
that server (or the client's bundled defaults if no rules are configured), then
clips intervals to the requested range before aggregation.
It does not export titles or URLs. Category/app names can still be sensitive;
review ``summary.json`` locally and load it using the HTML file picker, **not by
pasting it back into the code-generation chat**.

``tracked_seconds`` means observed window-event duration, not the entire selected
wall-clock range. AFK is observed AFK overlapping those windows. A gap in AFK
coverage is unknown, not automatically active or AFK; ``unknown_seconds`` in the
JSON records the nonnegative remainder. For a non-empty range, missing buckets
produce an error rather than a misleading zero. This assumes normal,
nonoverlapping window events per host. Canonical processing can bridge short
heartbeat gaps; do not treat these estimates as precise time accounting.
Synced buckets for other hosts are not included: compare hosts separately, do not
add their active durations without a separately defined overlap/precedence policy.

The exporter uses GET for bucket/settings discovery and ``POST /api/0/query/``
for read-only calculations. POST is required by the query API; it does not imply
an event write. The script does not call mutation endpoints. **Read-only is a
client convention, not a server-enforced permission boundary.** Keep the server
on loopback and do not loosen CORS or give unreviewed generated code API access.

Testing the generated page
^^^^^^^^^^^^^^^^^^^^^^^^^^

Before using real data:

1. Open the HTML file directly. Check Coding = 7200 s, Communication = 1800 s,
   Uncategorized = 600 s, active = 9600 s, AFK = 600 s, tracked = 10200 s.
   Category and app totals both equal active time, not active plus AFK.
2. Open browser DevTools → Network and reload. Loading the document itself is
   expected; it must make no HTTP(S), WebSocket, telemetry or model requests,
   including when choosing a local JSON file. CSP is defense in depth, not a
   substitute for reviewing the page.
3. Load a summary with empty category/app arrays and zero durations. Expect
   zero totals and a clear no-activity state. Try invalid JSON and a reversed
   range: expect a visible error, not a silent stale-data success.
4. Test the exporter on synthetic window/AFK events before trusting changed
   aggregation code. Check events straddling range boundaries, equivalent times
   with different UTC offsets, unknown AFK gaps, and two overlapping devices.

The reproducible :download:`verification script <verify-ai-dashboard.py>` starts
an isolated in-memory Python ``aw-server`` on a random loopback port; it never
connects to your normal server. In a disposable Python environment with
``aw-client``, ``aw-server`` and ``playwright`` installed, place it beside the
exporter and HTML file, install Playwright Chromium, then run
``python3 verify-ai-dashboard.py``. The reference was checked on Python 3.12 with
aw-client 0.5.15, aw-core 0.5.17 and aw-server 0.13.2 source (with Flask 2.2);
this is not a compatibility claim for all installed versions. It checks the known fixture, canonical query
results, range boundaries and browser file loading, and records attempted
network destinations. It does not prove that arbitrary future generated code or
every released server implementation behaves identically.

Using the page as a custom visualization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is **experimental and not required for the offline recipe above**. There
is no automatic ``<aw-data-dir>/custom_vis/`` discovery path. The Python server
can explicitly serve a directory (containing ``index.html``), for example:

.. code-block:: sh

   aw-server --host 127.0.0.1 --port 5666 \
     --custom-static dashboard=/absolute/path/to/reviewed-page

Use this when configuring your server, not while another server already owns
that port. The page is then at ``http://127.0.0.1:5666/pages/dashboard/``.
The equivalent persistent Python-server setting is a ``dashboard`` path entry
under ``[server.custom_static]`` in ``aw-server.toml``. Check the installed
server's help/config; do not assume Python CLI flags apply to the Rust server.
The Python-server path is covered by the verification script.

The web UI's custom visualization selector can embed configured pages and passes
``hostname``, ``start`` and ``end`` URL parameters. The offline reference viewer
**does not consume those parameters or automatically follow the selected range**;
its displayed range is the loaded summary. Building a live embedded viewer would
require separate query and security review, not just copying this HTML.

.. warning::

   Custom visualizations run in the ActivityWatch server's origin. A malicious
   page could read your data or make API calls. Only use pages you wrote or
   reviewed.

Capability map
--------------

ActivityWatch covers the local data collection layer. Before building a custom
interface, confirm which features are available in your installed version:

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Feature
     - Notes
   * - Desktop activity (window titles, app names)
     - Collected by ``aw-watcher-window``; titles available but sensitive
   * - AFK / active time
     - Collected by ``aw-watcher-afk``; used in canonical queries
   * - Rule-based categories
     - Set in the web UI; applied at query time; not automatic AI inference
   * - Android activity
     - Collected by the Android app; synced via :doc:`../features/syncing`
   * - iOS activity
     - Not available
   * - Automatic project attribution
     - Not built-in; rule-based only unless you add custom processing
   * - Seamless multi-device sync
     - Sync is manual/scheduled; see :doc:`../features/syncing` for current status

Rule-based categories are not AI-generated labels. They match patterns you
define against app names and window titles. Describing them as automatic
AI understanding overstates what is collected.

Related docs
------------

* :doc:`working-with-data`
* :doc:`../features/exporting-data`
* :doc:`../features/categorization`
* :doc:`../api/rest`
