.. _research-participant-instructions:

Participant instructions (Research Edition)
===========================================

.. note::
   **For researchers.** This page is maintained by the ActivityWatch project so that studies
   can link to it instead of maintaining their own copy of the technical steps. It is kept in
   sync with the current Research Edition build.

   Adapt freely: add your study name, your contact details, and your upload location.
   Translate as needed. The parts worth linking rather than copying are the mechanics below,
   because those are what change between releases.

   *Last reviewed: 2026-09-16, against v0.14.0b5-research.*

The Research Edition is a separate build. It installs alongside a normal ActivityWatch
installation without interfering with it: the Research Edition runs on port **5667**, a
standard installation runs on port 5600. The dashboard shows a **Research Edition** badge at
the top. If you see that badge, you are in the right place.

Installing
----------

Download the build for your system from the link your researcher gave you, then open the
downloaded file and follow the installation steps.

**Windows.** The installer is not code-signed, so Windows may show a blue
"Windows protected your PC" dialog. Click **More info**, then **Run anyway**.

During installation, leave **Start ActivityWatch when Windows starts** ticked. It is ticked
by default.

**macOS.** The app asks for two separate permissions, and it needs both:

1. **Accessibility.** On first launch you may see "Missing accessibility permissions".
   Enable *ActivityWatch Research* under System Settings > Privacy & Security >
   Accessibility, and restart the app if prompted. Without this permission the app cannot
   record anything.
2. **Browser control.** If you use Chrome or Safari, macOS asks whether
   *ActivityWatch Research* may control it. Click **OK**. This is only used to sort the page
   into a category. The address is not stored.

If macOS shows a notification that a background item was added, leave it allowed.

Starting automatically
----------------------

The Research Edition enables start-at-login by itself the first time it runs. You do not need
to configure anything.

It is still worth checking once or twice during the study that the icon is present: in the
system tray on Windows (bottom right, possibly hidden under the **^** arrow), or in the menu
bar on macOS (top right). If it is missing, start *ActivityWatch Research* from the Start menu
or Applications folder.

What is recorded
----------------

The Research Edition records **which applications you use** (for example Word, Teams or
Chrome) and for how long. It does **not** record which websites you visit or what your window
titles say. Browser activity is converted into predefined categories on your own computer
before anything is stored, and your computer's hostname is removed from the export.

No information about your activity is sent anywhere automatically. At the end of the study you
create a file and upload it yourself.

(For completeness: if you open the dashboard, the web interface asks GitHub for the latest
version number. That request contains nothing about your activity.)

Exporting your data at the end of the study
-------------------------------------------

Do this once, at the end of the study period, and keep the Research Edition running while you
do it. It takes a couple of minutes.

1. Click the **ActivityWatch Research** icon (macOS: menu bar, top of the screen. Windows:
   bottom right near the clock, possibly under the **^** arrow) and choose **Open Dashboard**.
   The dashboard opens in your browser. Check that it says **Research Edition** at the top.
   If the dashboard does not open, go to http://localhost:5667
2. Click **Raw Data** at the top right of the page. If your dashboard is not in English,
   this is the same button under a translated name (Swedish: **Rådata**).
3. You will see two rows, ``aw-watcher-window_…`` and ``aw-watcher-afk_…``. That is normal.
   **Do not export them one by one.** Scroll down to **Import and export buckets**, and under
   **Export buckets** click **Export all buckets as JSON** (Swedish: **Importera och
   exportera buckets** > **Exportera alla buckets som JSON**).
4. A file named ``aw-bucket-export.json`` appears in your Downloads folder. You do not need to
   open or edit it.
5. Upload that file where your researcher has asked you to.

If something looks wrong, contact your researcher rather than searching online. The study
version behaves differently from the public ActivityWatch.

Notes for researchers
---------------------

A few things that reliably cause support questions:

- **Two buckets is correct**, not a symptom of a double installation: one window watcher and
  one AFK watcher. Four rows would mean the participant opened the standard dashboard on port
  5600 instead.
- **Use "Export all buckets as JSON", not the per-row menu.** The three-dot menu on a row
  exports a single bucket. Participants following that route upload two files, or silently
  omit AFK data.
- **JSON, not CSV.** CSV covers one bucket, contains events only, carries no metadata, and
  does not go through the export API.
- **The interface may not be in English.** The web UI ships ``en``, ``uk``, ``de``, ``ru``,
  ``zh-CN`` and ``sv`` locales, and it **selects one automatically from the browser
  language** unless the participant has already chosen one. Translation coverage is
  incomplete across all locales, so participants will see a mix. The tray menu is hardcoded
  English regardless.

  Write button names in both languages in your participant instructions, for example
  "Rådata (Raw Data)". Assuming English will send some participants looking for a label
  their screen does not show.
- **The exported filename is fixed.** It cannot carry a participant number, so your upload
  form needs a field or a per-participant link.
- **Live Raw Data is unsanitised by design.** The rewriting to ``research-participant``
  happens in the export.
