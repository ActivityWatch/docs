Configuration
=============

Most common configuration options you need is in the Settings page of the web UI.

Other, more technical configuration options, are available through the config files. These are located in different places depending on your platform, see the `directories <config-directory>` documentation for where to find them.

.. note::
    In v0.11.0, the previous ``.ini`` config files used by all Python-based modules were replaced by ``.toml`` files (commented out by default, to allow for updates to the defaults). If you had made any modifications to the ini files prior to v0.11, you need to migrate them to the new files.

Configuration options for the server, client, and default watchers are listed below:

aw-server-python
----------------

- ``host`` Hostname to start the server on. Currently only ``localhost`` or ``127.0.0.1`` are supported.
- ``port`` Port number to start the server on.
- ``storage`` Type of storage for holding buckets and events. Supported types are ``peewee``, ``memory`` (useful in testing), or ``mongodb`` (MongoDB support will be removed in a future version).
- ``cors_origins`` Comma-separated list of allowed origins for CORS (Cross-Origin Resource Sharing). Useful in testing and development to let other origins access the ActivityWatch API, such as aw-webui in development mode on port 27180.

aw-server-rust
--------------

- ``host`` Hostname to start the server on. Currently only ``localhost`` or ``127.0.0.1`` are supported.
- ``port`` Port number to start the server on.
- ``cors`` List of allowed origins for CORS (Cross-Origin Resource Sharing). Useful in testing and development to let other origins access the ActivityWatch API, such as aw-webui in development mode on port 27180.

aw-client
---------

- ``server.hostname`` Hostname of the server to connect to.
- ``server.port`` Port number of the server to connect to.
- ``client.commit_interval`` How often to commit events to the server (in seconds).

aw-watcher-afk
--------------

- ``timeout`` Time in seconds after which a period without keyboard or mouse activity is considered to be AFK (away from keyboard).
- ``poll_time`` Time in seconds between checks for activity.

See `aw_watcher_afk/config.py <https://github.com/ActivityWatch/aw-watcher-afk/blob/master/aw_watcher_afk/config.py>`_ for the default config values.

aw-watcher-window
-----------------

- ``poll_time`` Time in seconds between window checks.
- ``exclude_title`` Don't track window titles
- ``strategy_macos`` The strategy to use on macOS to fetch the active window, can be "swift", "jxa" or "applescript". Swift strategy is preferred.
