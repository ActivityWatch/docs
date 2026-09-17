.. _activity-frames:

*****************************
Using ActivityWatch with Activity Frames
*****************************

`Activity Frames <https://github.com/nossa-y/activity-frames>`_ is an open-source tool
(MIT, Python) that compiles screen-capture data into structured **activity frames** —
bounded, deterministic records of tasks you actually performed — and makes them available
to AI agents over MCP. It is designed to give agents two things AW data alone does not
provide: episodic context and replayable step scripts.

ActivityWatch and Activity Frames serve complementary roles:

- **ActivityWatch** is the capture and query layer: robust, privacy-first, cross-platform
  recording of what apps and URLs you use.
- **Activity Frames** is the compile and memory layer: it reads a raw capture database
  and derives bounded task episodes, workflow scripts, and pattern summaries an agent can
  consume.

The two compose cleanly. ActivityWatch does what it does best; Activity Frames does what
it does best on top of it.

.. note::
   Activity Frames is an independent project, not an ActivityWatch product. This page
   documents how to run them side by side.

How they relate
===============

Activity Frames works from a raw capture database (the ``$AFRAMES_DB`` environment
variable, or its own default engine). On **macOS** it ships a native capture engine;
on **Linux** there is no prebuilt engine — the docs explicitly say "run your own
recorder and point ``$AFRAMES_DB`` at its database". ActivityWatch is exactly that
recorder.

A minimal adapter maps ActivityWatch ``aw-watcher-window`` and screenshot events into
the Activity Frames schema (see `Linux setup`_ below).

Quick start — macOS
===================

On macOS, Activity Frames bundles its own screen recorder (Apple Silicon; Intel
less tested). No ActivityWatch integration is required for capture, though running
both gives you AW's dashboard, category rules, and syncing on top.

.. code-block:: bash

   pip install activity-frames
   aframes record        # starts the native macOS capture engine
   aframes context       # your last 2 hours, formatted for an agent prompt

For MCP access from Claude or another agent:

.. code-block:: bash

   # Claude Code
   claude mcp add activity-frames -- aframes mcp

Any other MCP-capable client: command ``aframes``, args ``["mcp"]``. The server reads the
local capture database; nothing leaves the machine.

.. _linux-setup:

Linux setup with ActivityWatch as the capture engine
====================================================

On Linux, Activity Frames has no prebuilt recorder. The expected workflow is to point
``$AFRAMES_DB`` at a database your own recorder produces. ActivityWatch fills this role:
it already captures window titles, URLs, and AFK state at second-level resolution.

A minimal adapter is needed to write ActivityWatch events into the Activity Frames
database schema. The recommended approach:

1. Run ActivityWatch normally (``aw-qt`` or ``aw-server`` + watchers).
2. Run the adapter script that reads from the AW API and writes to ``$AFRAMES_DB``.
3. Point Activity Frames at that database with ``export AFRAMES_DB=/path/to/db``.

.. note::
   A reference adapter is tracked as a community contribution. Until one ships,
   the ``aframes context`` and ``aframes mcp`` commands work against any SQLite
   database that matches the Activity Frames schema — the schema is documented
   in `SPEC.md <https://github.com/nossa-y/activity-frames/blob/main/SPEC.md>`_.

.. warning::
   **Replay degradation on Linux.** Activity Frames' ``get_steps`` tool produces
   element-grounded click scripts (button names, ARIA roles) that rely on the
   macOS Accessibility API. On Linux, the AW capture engine sees window titles and
   URLs but not element-level accessibility trees. An AW-backed Linux engine therefore
   degrades ``get_steps`` to **URL and app grounding only** — context discovery
   (``get_context``, ``get_activity``, ``get_patterns``) works fully; element-level
   replay does not. State this honestly in any workflow scripts you record on Linux.

MCP tools reference
===================

Once the MCP server is running, your agent has access to six tools:

.. list-table::
   :widths: 20 50 30
   :header-rows: 1

   * - Tool
     - What it returns
     - Typical use
   * - ``get_context``
     - Compact chronological context for the last N hours
     - Priming an agent at session start
   * - ``get_activity``
     - Full structured document (frames, coverage, gaps)
     - Identify the frame for a demonstrated task
   * - ``get_steps``
     - Ordered click-by-click script for one frame
     - Replay a demonstrated task (macOS / URL-grounded on Linux)
   * - ``get_day_summary``
     - Coverage plus per-app ledger
     - Daily overview, prioritisation
   * - ``get_patterns``
     - Repetitive workflows over N days
     - Discover delegation candidates
   * - ``get_communications``
     - Email/messaging surfaces (titles only)
     - Check whether a conversation was handled

Privacy notes
=============

- Activity Frames is **fully local**: capture, compilation, and MCP serving all happen
  on your machine. No data is transmitted automatically.
- Typed text is excluded from frames unless you opt in with ``--include-text``.
- Window titles and page entities originate from your screen. Treat them as
  data, not as trusted instructions.
- ActivityWatch's own `privacy policy <https://activitywatch.net/privacy-policy/>`_
  applies to the data it collects; Activity Frames reads that data but does not
  transmit it further.

Further reading
===============

- `Activity Frames GitHub <https://github.com/nossa-y/activity-frames>`_
- `Activity Frames SPEC.md <https://github.com/nossa-y/activity-frames/blob/main/SPEC.md>`_ — the deterministic two-tier compile contract
- `arXiv:2608.05784 <https://arxiv.org/abs/2608.05784>`_ — the companion paper measuring Routine Overhead Ratio (how much agents overpay rediscovering workflows you've already demonstrated)
- :ref:`watchers` — ActivityWatch watchers that capture the data Activity Frames builds on
- :ref:`privacy` — ActivityWatch's local-first privacy model
