.. include:: global.rst

=========
Changelog
=========

v0.9.0
------

Released 2020-03-15
 - add Rust server as an option. It has better performance and will be the main supported server soon.
 - Almost all python components have been moved to poetry / pyproject.toml from old pip / setup.py building.

[Main repo]( ActivityWatch/activitywatch )
 - Add aw-server-rust binary to pyinstaller bundles (a567003)
 - Automatic stale issue detection / closing (issues marked as stale after 180 days of inactivity, closed after 14 stale days)
 - Added aw-server-rust
 - Add .app and .dmg building

aw-client:
 - switched to using pyproject/poetry (d66f319)
 - Change default limit from 100 to return all by default (d35449a)

aw-core:
 - added strict-rfc3339 (c5e9d34)
 - upgraded jsonschema (a803443)

aw-qt
 - Use manager to stop all modules (ac40452)
Make aw-qt less annoying:
 - Remove confirm dialog on exit (246ff05)
 - Remove startup notification (#45) (b1f66c3)
 - added aw-server-rust to possible modules (b4e9411)
 - Add dark mode detection to MacOS logo logic (502b77d)

aw-server
 - migrated from flask-restplus to flask-restx, updated submodule (36e970e)
 - Makefile improvements: use pip3 (47a208b), fixed make build DEV=true (817723b)

aw-server-rust:
 - Added in this release. 

aw-watcher-window
 - readded script that disappeared in previous PR (1e424e4)
 - revise exclude_title logic (b1bd00d)

aw-webui:
 - added ability to edit start and end in EventEditor, added ability to edit events from Bucket view (10dc80f)
 - Add vuex support for editor activity (47fed8b)
 - added setting for 'show last' duration default value (20ca6fa)
 
 - buckets: Fix broken export bucket button (0a60cf7)
 - fixed long lines (c502787)
 - fixed bugs in event editor and stopwatch (d121fcb)
 - fixed editing events in bucket view (b6c1405)
 - stopwatch: Fixes broken "stop" and "edit" (06be96b)
 - Fix firefox developer edition browser data not showing up in activity view. (4a05131)
 - views/activity: Fix so subview is kept between date changes (c0ae191)
 
 - Improvements to Stopwatch and EventEditor (#166) (2040a92)
 - package.json: Update to fix vulnerabilities (a2f48a8)
 - Swich from timeline-plus to vis-timeline (98cd372)
 - queries: Removed trailing lines (d25cf09)

v0.8.4
------

Released 2019-12-10

 - Adds the ability to filter the activity view by category.
 - Fixes a bug where setting rule for a category to 'None' breaks the UI :issue:`313`.
 - Fixes the broken favicon for aw-webui.

v0.8.3
------

Released 2019-11-13 (yes, the same day as v0.8.2)

 - Fixes the Windows builds

v0.8.2
------

Released 2019-11-13

Just minor fixes to the v0.8.1 that was released the day before.

 - Added a Windows installer
 - :strike:`Fixes the Windows builds` (it did not)
 - Fixes a bug in the web UI where weeks didn't always start on Mondays and months didn't always start on the first

v0.8.1
------

Released 2019-11-12

The v0.8 versions are finally leaving beta, and we celebrate this by giving you a truly awesome release!

It's the culmination of a lot of behind-the-scenes work that has been going on for quite a while. Several of our most requested features have made it into this release (categorization, better weekly/monthly visualizations, preparations for syncing), making it our best release yet!

Web UI:

 - Categorization is finally here! Including visualizations and settings. The UX still leaves some things to be desired, but it's a great start.
 - Daily and Summary views are now merged into one so that you get all the goodies of the Daily view but for arbitrary timeperiods like days/weeks/months!
 - Updated the start page, including links to resources like the `user survey <https://forms.gle/q2N9K5RoERBV8kqPA>`_.

Server:

 - New unique device ID is now exposed through the info API endpoint, a pre-requisite for building the much requested sync feature.
 - Now contains the transforms needed for categorization.

Other:

 - There is now a Windows installer available, and it automatically sets up autostart!

v0.8.0b9
--------

Released 2019-07-03

.. note::
   Changelog incomplete

Web UI:

 - Now includes the Summary view for summarizing activity across weekly/monthly/yearly timeperiods!

v0.8.0b8
--------

Released 2019-03-09

.. note::
   Changelog incomplete

Server:

 - Import and export APIs are now usable

Web UI:

 - Added Stopwatch functionality
 - Added ability to import buckets from export
 - Bucket export button now does a full export that includes metadata

Other:

 - The lowest version of Python supported for building ActivityWatch is now 3.6.
 - Fixed PyInstaller-built releases on Windows

v0.8.0b7
--------

Released 2018-11-03

Web UI:

  - Fix broken editor bucket visualization

Misc:

  - CI Improvements

v0.8.0b2 - v0.8.0b6
-------------------

No changelog written.

v0.8.0b1
--------

Released 2018-05-07

Server:

- New query2 API for querying and transforming data
- Added :code:`version` field to :code:`/info` endpoint
- Set stricter allowed CORS origins in testing mode
- Added :code:`--cors-origins` CLI argument

Web UI:

- Added datepicker to the activity view
- Moved the today/clock visualization into the activity view
- New visualization for most-visited domains
- New visualization for previous days active time
- New query explorer
- Now displays version and hostname in bottom-right corner
- Now uses aw-client-js for all API calls

Watchers:

- Improved stability of client event queues (:gh-aw:`see this PR <aw-client/pull/28>`)

Other:

- Windows: Console window and taskbar icon now hidden by default (:issue:`139`)
- All issues assigned to the v0.8 milestone can be found :gh-aw:`on GitHub <activitywatch/milestone/1>`

v0.7.1
------

Released 2017-11-06

- Actually fixed the timezone issue in the web UI (:issue:`117`).
- All issues assigned to the v0.7 milestone can be found :gh-aw:`on GitHub <activitywatch/milestone/4>`.

v0.7.0b4
--------

Released 2017-10-22

- The ActivityWatch WebExtension is officially supported from this version forward, see the announcement `on the forum <https://forum.activitywatch.net/t/you-can-now-track-your-web-browsing-with-activitywatch/28>`_.
- (Not really, see v0.7.1) Fixed pesky timezone issue in web UI (:issue:`117`).
- Fixed bug on macOS where keyboard activity would not be used to detect AFK state.
- Fixed packaging bugs (macOS, PyInstaller).
- The web extension now has a better look and notifies if connection to server failed.

v0.7.0b3
--------

Released 2017-08-25

- Even more improvements to the web UI.
- Major improvements to the documentation, notably instructions on how to install from builds and sources.

v0.7.0b2
--------

Released 2017-08-09

- Improvements to the web UI: a new visualization method (the "today" view) and information for users about the state of the project on the first page.

v0.7.0b1
--------

Released 2017-06-14

There have been several major changes since v0.6. Much of it wont end up here but hopefully the major things will.

.. note::
    If you are upgrading from a previous version, you might want to stop all loggers for the duration of your UTC offset to prevent issues which we've had difficulty debugging (or you can just start right away and expect your first hours to end up a bit weird).

- Now works on Windows.
- Working standalone packages. (edit: not reliable on all systems, but a lot easier to get running in many cases)
- All timestamps are now in UTC.
- Updated outdated parts of the documentation.
- Makefiles are now used throughout the projects to manage building, testing, and CI.
- A lot of bug fixes (and hopefully not too many new bugs).
- Vastly improved code quality.

v0.6.0 and older
----------------

We haven't been keeping track of changes very well for older versions. Please refer to the git history.
