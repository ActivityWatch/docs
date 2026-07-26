Syncing
=======

.. note::

    This feature is currently in beta and may change in future releases.

ActivityWatch has basic support for syncing your data across multiple devices using the ``aw-sync`` module since ``v0.13.0``. It works by creating a "staging" database file in a device-specific folder in the sync directory (default is ``~/ActivityWatchSync``), which is then synced to the other devices using a file syncing tool of your choice (like Syncthing, rsync, Dropbox, or Google Drive). So ``aw-sync`` does not itself send data over the network, but instead relies on you using a file syncing tool to do that.

Android
-------

Sync on Android is more limited than on desktop, and is currently **disabled
by default** with no user-facing way to turn it on.

The Android app can push its own events into a sync directory (scoped to the
app's private storage: ``Android/data/net.activitywatch.android/files/sync/``),
but since Android 11 that directory is not accessible to other apps — so a
file syncing tool like Syncthing cannot read from or write into it. In
practice this means the app can produce its side of the sync data, but there
is currently no supported way to push that data to other devices or to pull
other devices' data onto the phone. Automatic background sync used to run unconditionally
every 15 minutes regardless of whether it could do anything useful; it is now
gated behind a preference that defaults to off, so it no longer runs on fresh
installs.

A proper setup flow — a settings toggle plus a way to pick a sync directory
that's actually accessible to a file syncing tool (e.g. via Android's Storage
Access Framework) — is planned but not yet built. Track progress in
`activitywatch#1357 <https://github.com/ActivityWatch/activitywatch/issues/1357>`_.

How to set up syncing
---------------------

.. note::

    We recommend you've switched to ``aw-server-rust`` before using the syncing feature, as it has better performance which will help with syncing large amounts of data. If you are still using the legacy ``aw-server`` (Python), you can find the documentation for switching to the Rust server in :docs:`migrating`.

For detailed instructions on how to use syncing, see the `aw-sync README <https://github.com/ActivityWatch/aw-server-rust/blob/master/aw-sync/README.md>`_.
