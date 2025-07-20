Syncing
=======

.. note::

    This feature is currently in beta and may change in future releases.

ActivityWatch has basic support for syncing your data across multiple devices using the ``aw-sync`` module since ``v0.13.0``. It works by creating a "staging" database file in a device-specific folder in the sync directory (default is ``~/ActivityWatchSync``), which is then synced to the other devices using a file syncing tool of your choice (like Syncthing, rsync, Dropbox, or Google Drive). So ``aw-sync`` does itself send data over the network, but instead relies on you using a file syncing tool to do that.

Note that syncing is not available on Android, yet.

How to set up syncing
---------------------

.. note::

    We recommend you've switched to ``aw-server-rust`` before using the syncing feature, as it has better performance which will help with syncing large amounts of data. If you are still using the legacy ``aw-server`` (Python), you can find the documentation for switching to the Rust server in :docs:`migrating`.

For detailed instructions on how to use syncing, see the `aw-sync README <https://github.com/ActivityWatch/aw-server-rust/blob/master/aw-sync/README.md>`_.
