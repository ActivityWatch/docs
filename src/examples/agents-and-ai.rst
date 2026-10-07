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

Related docs
------------

* :doc:`working-with-data`
* :doc:`../features/exporting-data`
* :doc:`../features/categorization`
* :doc:`../api/rest`
