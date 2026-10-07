Syncing
=======

.. note::

    Sync works, but it is still rough in places and is not started by default. See `Limitations`_.

``aw-sync`` lets your devices share their ActivityWatch data with each other, so you can see your laptop, desktop and phone together, for example in the Activity view's device selector. It has shipped with ActivityWatch since ``v0.13.0``, and v0.14.0 is the first release where it works across desktops and Android.

How it works
------------

Sync is **local-first and bring-your-own-sync**. There is no ActivityWatch server and no account:

- ``aw-sync`` writes each device's data into its own folder inside a sync directory (``~/ActivityWatchSync`` by default), as ``{hostname}/{device_id}/``.
- You move that directory between devices with any file syncing tool you already use: Syncthing, Dropbox, Google Drive, a network drive, rsync. ``aw-sync`` never sends data over the network itself.
- Each device only writes its own files, and opens the other devices' files read-only. Devices can't overwrite or corrupt each other's data, so there are no sync conflicts to resolve.
- Data from other devices is imported into your local server as ``-synced-from-`` buckets (e.g. ``aw-watcher-window_laptop-synced-from-laptop``), which you can query, merge in the Activity view, or ignore.

Setting up sync on desktop
--------------------------

1. Set up your file syncing tool to sync ``~/ActivityWatchSync`` (or another folder) between your devices **before** running ``aw-sync``.
2. On each device, run a sync pass. Either:

   - **One-shot:** ``aw-sync sync`` pushes this device's data and pulls everyone else's, then exits. Run it by hand, or on a timer (cron, systemd, launchd).
   - **In the background:** start ``aw-sync`` from the modules menu in aw-qt or aw-tauri (or run ``aw-sync daemon``). By default the background daemon only **pushes** this device's data. To also pull the other devices' data on every pass, edit aw-sync's ``config.toml`` (created on the daemon's first start, in ``~/.config/activitywatch/aw-sync/`` on Linux, ``~/Library/Application Support/activitywatch/aw-sync/`` on macOS and ``%LOCALAPPDATA%\activitywatch\aw-sync\`` on Windows, see :doc:`directories`):

     .. code-block:: toml

        [daemon]
        pull = true

3. Check what is happening with ``aw-sync status``. It lists the devices found in the sync folder, what each has synced, the daemon's effective mode and which config file it read (the same file the daemon uses).

Use a custom sync directory with ``--sync-dir`` or the ``AW_SYNC_DIR`` environment variable. Restrict which buckets are synced with ``--buckets``. See ``aw-sync --help`` and the `aw-sync README <https://github.com/ActivityWatch/aw-server-rust/blob/master/aw-sync/README.md>`_ for all options.

.. note::

    Use ``aw-server-rust`` (the server in the Tauri app, also bundled with the classic app) for syncing. It handles large amounts of synced data better. See :doc:`migrating` to switch.

Android
-------

Since `ActivityWatch for Android 0.14 <https://activitywatch.net/blog/activitywatch-android-0-14-stable/>`_, the Android app runs the same sync code. It is **off by default**: turn it on in the app's settings and pick a folder through Android's storage picker, so that a syncing tool like Syncthing can sync that folder to your other devices. The app shows when the next sync is scheduled and what each pass did.

The Android app currently only **pushes** its own data. Your phone's activity shows up on your desktops, but desktop data is not pulled onto the phone.

Limitations
-----------

- **Disk space.** Every device keeps a full copy of every other device's data, so with many devices it uses a lot of space. A much more compact format is in development.
- **Setup is manual.** You set up the file syncing tool yourself, and sync is not started by default.
- **Settings are not synced**, only activity data.
- **Deletions are not synced.** Edits made on the device that recorded an event are synced (within 7 days).
- **Synced buckets are best treated as read-only.** Local edits to ``-synced-from-`` buckets can be overwritten by later sync passes.

If you synced before v0.14.0 and see duplicate events in ``-synced-from-`` buckets, ``aw-sync dedupe --dry-run`` reports them, and ``aw-sync dedupe --bucket <bucket-id>`` removes the extra copies.

Please report problems on `GitHub <https://github.com/ActivityWatch/activitywatch/issues>`_.
