.. _research-participant-instructions-android:

Participant instructions — Android (Research Edition)
======================================================

.. note::
   **For researchers.** This page is maintained by the ActivityWatch project so that studies
   can link to it instead of maintaining their own copy of the technical steps. It is kept in
   sync with the current Research Edition build.

   Adapt freely: add your study name, your contact details, and your upload location.
   Translate as needed. The parts worth linking rather than copying are the mechanics below,
   because those are what change between releases.

   *Last reviewed: 2026-09-17, against v0.14.0b5-research.*

The Android Research Edition is a separate build. It installs alongside a normal
ActivityWatch installation without interfering with it: the Research Edition runs on port
**5667**, a standard installation runs on port 5600. The dashboard shows a **Research
Edition** badge at the top. If you see that badge, you are in the right place.

The build has the application ID ``net.activitywatch.android.research``, so it appears as
**ActivityWatch Research** on your device.

Step 1 — Allow installation from unknown sources
-------------------------------------------------

Android blocks apps that are not installed from the Play Store by default. You need to allow
your file manager or browser to install APK files before you can proceed. The exact steps
depend on your Android version.

**Android 8 or newer (most devices):**

The permission is granted per app. When Android asks during installation (step 3 below),
it will prompt you automatically. If it does not, or if you prefer to enable it in advance:

1. Open **Settings** → **Apps** (or **Application Manager**).
2. Tap the three-dot menu or find **Special app access**.
3. Tap **Install unknown apps**.
4. Select the app you will use to open the APK (usually **Files**, **My Files**, or your
   browser).
5. Enable **Allow from this source**.

**Android 7 or earlier:**

1. Open **Settings** → **Security**.
2. Enable **Unknown sources**.
3. Confirm the warning dialog.

**Oculus / Meta Quest headsets:**

On a Quest 2, Quest 3, or similar headset, sideloading via APK requires **Developer Mode**:

1. Open the Meta app on your phone, go to **Menu** → **Devices** → select your headset.
2. Tap **Developer Mode** and turn it on.
3. Confirm on the headset if asked.

After enabling Developer Mode, you can install the APK using a file manager sideloaded
onto the headset, or using ``adb install`` from a computer if your researcher provides that
option. If your researcher asks you to use a particular install method, follow their
instructions.

Step 2 — Download the APK
--------------------------

Download the Research Edition APK from the link your researcher provided. Save it somewhere
you can find it (Downloads folder is fine).

The file is named something like ``activitywatch-research-v0.14.0b5-research.apk``. Do not
rename it.

Step 3 — Install the app
------------------------

1. Open the Downloads folder (or wherever you saved the APK).
2. Tap the APK file.
3. Android may ask **"Do you want to install this application?"** — tap **Install**.
4. If Android asks whether to allow the file manager or browser to install unknown apps,
   tap **Settings**, enable the permission, then go back and tap **Install** again.
5. When installation is complete, tap **Open** or find **ActivityWatch Research** in your
   app drawer.

Step 4 — Confirm the Research Edition badge
--------------------------------------------

After opening the app:

1. The app starts a background service and opens the dashboard in the on-device browser (or
   you can go to ``http://localhost:5667`` manually).
2. Check that the page says **Research Edition** at the top. If it says only "ActivityWatch"
   without that badge, you may have opened the wrong app or the wrong port. Contact your
   researcher.
3. Leave the app running in the background for the duration of the study.

Step 5 — Export your data at the end of the study
--------------------------------------------------

Do this once, at the end of the study period, while ActivityWatch Research is still running.
It takes a couple of minutes.

1. Open the **ActivityWatch Research** app (or go to ``http://localhost:5667`` in your
   browser). Confirm the **Research Edition** badge is visible.
2. Tap **Raw Data** at the top right. You will see two rows:
   ``aw-watcher-android_…`` and ``aw-watcher-afk_…``. That is normal.
3. Scroll down to **Import and export buckets**.
4. Under **Export buckets**, tap **Export all buckets as JSON**.
5. Your browser will either ask where to save the file or send it straight to your
   **Downloads** folder without asking. Both are normal, and the export has succeeded as
   soon as the file exists. If you are not shown a chooser, open your browser's downloads
   list (or the **Files** app → **Downloads**) and the file will be there.
6. The file is named ``aw-bucket-export.json``. Upload it where your researcher has asked
   you to, or use the share sheet to send it to the researcher's upload link if they
   provided one.

If something looks wrong, contact your researcher rather than searching online. The study
version behaves differently from the public ActivityWatch.

Notes for researchers (Android)
-------------------------------

A few things specific to the Android Research Edition:

- **Port 5667, application ID ``net.activitywatch.android.research``.** These are the two
  reliable identifiers. Do not rely on the app icon or name alone — participants may have
  both the standard and Research builds installed.
- **The app must be running in the background while participants use the device.** Android
  may kill background services on low-battery or power-save modes. Ask participants to
  add ActivityWatch Research to their battery optimisation exemptions: Settings → Battery
  → Battery optimisation → All apps → ActivityWatch Research → Don't optimise.
- **The Research Edition has its own data store, not a shared one.** It has its own
  application ID (``net.activitywatch.android.research``) and its own app data directory,
  so installing it next to a standard ActivityWatch installation does not mix the two
  databases and does not require a fresh device. A participant who already uses
  ActivityWatch keeps their own install and data untouched.
- **Pre-existing data can still reach the Research database through an import.** The
  reachable path is not a shared database but an import or restore: if anyone imports an
  exported database into the Research app, those events land in the Research database and
  are exported with everything else. The desktop Research Edition refuses to export a
  database containing unfiltered events; the Android build does not implement that guard,
  so the only protection here is not importing in the first place. Do not ask participants
  to import or restore anything into the Research app, and do not re-use a standard
  ActivityWatch export file as study data.
- **Sideloading on Oculus / Meta Quest requires Developer Mode** (see Step 1 above).
  If your study uses VR headsets, confirm with each participant that Developer Mode is on
  before the study period begins, not at export time.
- **Two buckets is normal.** One window/app watcher and one AFK watcher. See the desktop
  instructions for the full explanation.
- **The exported filename is fixed.** It cannot carry a participant number. Your upload
  form needs a field or a per-participant link — the same constraint as the desktop export.
- **Battery optimisation and task-killer apps** are the most common reason for missing
  data on Android. Coach participants to add the app to the battery exemption list before
  the study period starts.

See also :ref:`research-participant-instructions` for the desktop (Windows / macOS)
instructions.
