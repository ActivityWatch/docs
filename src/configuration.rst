Configuration
=============

Most common configuration options you need is in the Settings page of the web UI.

Other, more technical configuration options, are available through the config files. These are located in different places depending on your platform, see the `directories <config-directory>` documentation for where to find them.

.. note::
    In v0.11.0, the previous ``.ini`` config files used by all Python-based modules were replaced by ``.toml`` files (commented out by default, to allow for updates to the defaults). If you had made any modifications to the ini files prior to v0.11, you need to migrate them to the new files.

Configuration options for the server, client, and default watchers are listed below:

aw-server-python
----------------

- :code:`host` Hostname to start the server on. Currently only :code:`localhost` or :code:`127.0.0.1` are supported.
- :code:`port` Port number to start the server on.
- :code:`storage` Type of storage for holding buckets and events. Supported types are :code:`peewee`, :code:`memory` (useful in testing), or :code:`mongodb` (MongoDB support will be removed in a future version).

aw-server-rust
--------------

- :code:`host` Hostname to start the server on. Currently only :code:`localhost` or :code:`127.0.0.1` are supported.
- :code:`port` Port number to start the server on.
- :code:`cors` Enable CORS (Cross-Origin Resource Sharing) for the server. This is useful if you want to access the server from a different domain than the one it's hosted on.

aw-client
---------

- :code:`server.hostname` Hostname of the server to connect to.
- :code:`server.port` Port number of the server to connect to.
- :code:`client.commit_interval` How often to commit events to the server (in seconds).

aw-watcher-afk
--------------

- :code:`timeout` Time in seconds after which a period without keyboard or mouse activity is considered to be AFK (away from keyboard).
- :code:`poll_time` Time in seconds between checks for activity.

See `aw_watcher_afk/config.py <https://github.com/ActivityWatch/aw-watcher-afk/blob/master/aw_watcher_afk/config.py>`_ for the default config values.

aw-watcher-window
-----------------

- :code:`poll_time` Time in seconds between window checks.
- :code:`exclude_title` Don't track window titles
- :code:`strategy_macos` The strategy to use on macOS to fetch the active window, can be "swift", "jxa" or "applescript". Swift strategy is preferred. 
