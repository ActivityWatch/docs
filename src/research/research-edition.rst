.. _research-edition:

Research Edition
================

The **Research Edition** is a separate build of ActivityWatch for research studies. It
records which applications participants use and for how long, converts browser activity into
categories defined by the study, and discards window titles and URLs before anything is
written to disk. Data stays on the participant's computer until they export it and send it
to the study team.

This page is for researchers deciding whether it fits their study. Participants should use
the :doc:`participant instructions <participant-instructions>`.

.. note::
   *Last reviewed: 2026-09-30, against v0.14.0b5-research.* Desktop builds are
   **prereleases**. Read the platform status below before planning around a platform.

What it collects
----------------

The desktop Research Edition turns on a privacy filter in ``aw-watcher-window``
(``research_enabled = true``):

- **Browsers**: each browser window is classified into a study category by matching the URL
  (where available) and otherwise the window title against the study's category map. The
  longest matching pattern wins. Windows that match nothing are stored as ``excluded``. The
  title and URL are discarded **before** the event is recorded, not at export.
- **Other applications**: the window title is discarded. The **application name is kept**.
  A variant can instead replace application names with categories by setting the optional
  ``research_app_category_map``. Unmapped apps then become ``Excluded``.
- **Away from computer**: recorded by the regular AFK watcher.
- **Export**: the participant's computer name is rewritten to ``research-participant``. The
  export refuses to run if the database contains unfiltered events, for example when the
  Research Edition was installed over an existing ActivityWatch database.

What is *not* collected: page titles, URLs, document names and window titles. What *is*
visible in the current build: application names, including which browser was used.

There is no telemetry and no study server. The participant exports one JSON file from the
dashboard and uploads it where the study team asks.

Keeping participant and study data apart
----------------------------------------

The Research Edition has its own app identity, its own data folder and its own server port
(**5667**, against **5600** for a standard install). A participant who already uses
ActivityWatch can run both side by side, and the standard install's data is not read or
changed. The dashboard shows a **Research Edition** badge.

Making a variant for your study
-------------------------------

Studies tend to want the same thing: categorized time, no raw titles or URLs, a simple
end-of-study export. A variant is therefore mostly:

1. **A category map**: which sites and apps belong to which of your categories, with
   everything else excluded. This is the part only the study can define.
2. **A tagged build**: research builds are published as GitHub prereleases with a
   ``-research`` tag, which gives participants a stable download link you can cite in a
   methods section.
3. **A participant guide and export step**: start from the
   :doc:`participant instructions <participant-instructions>` and add your study name,
   contact details and upload location.

The design is intended to fit an ethics review, but your committee decides that for your
study. Bring its requirements when you get in touch.

To request a variant, contact Erik Bjäreholt, the ActivityWatch maintainer, at
erik@bjareho.lt.

Platform status
---------------

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Platform
     - Status
     - Notes
   * - Windows, macOS, Linux
     - Shipped as prereleases
     - Latest: `v0.14.0b5-research
       <https://github.com/ActivityWatch/activitywatch/releases/tag/v0.14.0b5-research>`_.
       The participant instructions cover Windows and macOS.
   * - Android
     - In development
     - ``aw-android`` has a ``research`` build flavor with its own application ID
       (``net.activitywatch.android.research``) and port 5667, so it installs beside the
       regular app. The category filter that the desktop build has is **not** on Android
       yet, and no ``-research`` Android release has been published. See the
       :doc:`Android participant instructions <participant-instructions-android>` for the
       intended install path.
   * - iPhone and iPad
     - Planned
     - There is no iOS app. `aw-import-screentime
       <https://github.com/ActivityWatch/aw-import-screentime>`_ imports Apple's Screen Time
       data into ActivityWatch. It requires a Mac with Screen Time "Share Across Devices"
       enabled on both devices under the same Apple account, and Full Disk Access on the Mac.
       It is a standalone tool, and the research filter does not apply to that data path yet.
