Configuration
=============

Most common configuration options you need is in the Settings page of the web UI.

Other, more technical configuration options, are available through the config files. These are located in different places depending on your platform, see the `directories <config-directory>` documentation for where to find them.

.. note::
    In v0.11.0, the previous ``.ini`` config files used by all Python-based modules were replaced by ``.toml`` files (commented out by default, to allow for updates to the defaults). If you had made any modifications to the ini files prior to v0.11, you need to migrate them to the new files.

Configuration options for the server, client, and default watchers are listed below:

aw-server-python
----------------

These settings go under the ``[server]`` section of ``aw-server/aw-server.toml``.

- ``host`` Address to bind the server to. The default is ``localhost``. Binding to any other address exposes the server to the network, see :doc:`remote-server`.
- ``port`` Port number to start the server on.
- ``storage`` Type of storage for holding buckets and events. Supported types are ``peewee`` (the default), ``sqlite``, or ``memory`` (useful in testing).
- ``cors_origins`` Comma-separated list of allowed origins for CORS (Cross-Origin Resource Sharing). Useful in testing and development to let other origins access the ActivityWatch API, such as aw-webui in development mode on port 27180.
- ``query_cache`` Whether to cache query results for finished past periods in memory. The default is ``true``.
- ``custom_static`` A table under ``[server.custom_static]`` mapping watcher names to directories containing their :doc:`custom visualizations <watchers>`.

aw-server-rust
--------------

These settings go at the top level of ``aw-server-rust/config.toml`` (there is no ``[server]`` section).

- ``address`` Address to bind the server to. The default is ``127.0.0.1``. Binding to any other address exposes the server to the network, see :doc:`remote-server`.
- ``port`` Port number to start the server on.
- ``cors`` List of allowed origins for CORS (Cross-Origin Resource Sharing). Useful in testing and development to let other origins access the ActivityWatch API, such as aw-webui in development mode on port 27180.
- ``cors_regex`` List of regular expressions matching additional allowed CORS origins.
- ``custom_static`` A table mapping watcher names to directories containing their :doc:`custom visualizations <watchers>`.
- ``api_key`` Under an ``[auth]`` section: an optional API key that clients must send to access the API. Authentication is disabled when it is unset, see :doc:`security`.

aw-client
---------

- ``server.hostname`` Hostname of the server to connect to.
- ``server.port`` Port number of the server to connect to.
- ``client.commit_interval`` How often to commit events to the server (in seconds).

aw-watcher-afk
--------------

- ``timeout`` Time in seconds after which a period without keyboard or mouse activity is considered to be AFK (away from keyboard). The default is ``180`` seconds.
- ``poll_time`` Time in seconds between checks for activity. The default is ``5`` seconds.

These settings live in ``aw-watcher-afk/aw-watcher-afk.toml``, the config file for the ``aw-watcher-afk`` component, not in the ActivityWatch web UI settings page.
You can open the config folder from the ActivityWatch tray menu, or use the :ref:`config directory <config-directory>` for your platform.
If a setting is commented out in the file, remove the leading ``#`` before changing it.
After saving the file, restart ActivityWatch or ``aw-watcher-afk`` for the change to take effect.

See `aw_watcher_afk/config.py <https://github.com/ActivityWatch/aw-watcher-afk/blob/master/aw_watcher_afk/config.py>`_ for the source of the default config values.

aw-watcher-window
-----------------

- ``poll_time`` Time in seconds between window checks.
- ``exclude_title`` Don't track window titles
- ``strategy_macos`` The strategy to use on macOS to fetch the active window, can be "swift", "jxa" or "applescript". Swift strategy is preferred.
