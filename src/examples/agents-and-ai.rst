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

ActivityWatch's REST API lets you build custom dashboards and visualizations
without changing the core UI. An AI assistant can generate the code; your data
stays local throughout.

**What to ask for.** Use a prompt like the one below. It starts from a synthetic
event schema so the generated page works before you connect real data, and it
restricts all network access to the local ActivityWatch server:

.. code-block:: text

   Build a single-file HTML dashboard that reads ActivityWatch data.

   Constraints — follow these exactly:
   - All network requests MUST go to http://localhost:5666/api/0/ only.
     No CDN imports, no analytics, no external fonts, no telemetry.
   - All JavaScript must be inline in the HTML file. No npm, no build step.
   - The page must work with SYNTHETIC data first (hardcoded fixture below)
     and optionally connect to the live API via a checkbox or button.
   - Use only read-only API operations (GET requests). No POST, PUT, or DELETE.
   - Do not store, forward, or log any real ActivityWatch events.

   Synthetic fixture (use this until the user enables live data):
   {
     "hostname": "my-machine",
     "start": "2024-01-15T08:00:00",
     "end": "2024-01-15T12:00:00",
     "categories": [
       {"name": ["Coding"], "seconds": 7200},
       {"name": ["Communication"], "seconds": 1800},
       {"name": ["Uncategorized"], "seconds": 600}
     ],
     "apps": [
       {"app": "Code", "seconds": 5400},
       {"app": "Firefox", "seconds": 2400}
     ],
     "active_seconds": 10200,
     "afk_seconds": 600
   }

   When live data is enabled, read `hostname`, `start`, `end` from the URL
   query parameters (?hostname=…&start=…&end=…) and fetch from:
     GET http://localhost:5666/api/0/buckets/
   to discover bucket IDs, then query the canonical activity endpoint at:
     POST http://localhost:5666/api/0/query/
   with the time range. Show totals by category and by app, active time,
   and AFK time. Show a note that "read-only" is not a server-enforced
   boundary — it is a convention this page follows.

This generates a page that:

* renders against known data immediately (no ActivityWatch dependency at first)
* fetches from ``localhost:5666`` when live mode is enabled
* makes no outbound requests during code generation or when run
* handles empty responses, AFK filtering, and timezone-aware timestamps

.. note::

   Code generation and data access are separate. When you ask an AI to write
   this page, the model only sees your prompt and synthetic fixture — not your
   real ActivityWatch data. Real data is only accessed later, locally, when
   *you* open the generated file in a browser pointed at your running AW server.

Testing the generated page
^^^^^^^^^^^^^^^^^^^^^^^^^^

Before using real data, verify the generated page against its synthetic fixture:

1. Open the file directly in a browser (``file://``). It should render the
   fixture categories and totals without any network requests.
2. Open browser DevTools → Network. Reload. Confirm no requests go outside
   ``localhost:5666``.
3. Enable live mode. DevTools should show only requests to ``localhost:5666``.
4. Try an empty time range (start = end). The page should show zero totals, not
   an error.

Using the page as a custom visualization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ActivityWatch's web UI can embed custom pages as an iframe tab. This feature is
**experimental**. To use it:

1. Place the generated HTML file in ``<aw-data-dir>/custom_vis/<name>/``.
2. Open ActivityWatch at ``http://localhost:5666``.
3. Navigate to the custom visualizations tab and select ``<name>``.

The iframe receives ``hostname``, ``start``, and ``end`` as URL parameters so it
automatically follows the selected time range.

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
