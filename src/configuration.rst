Configuration
=============

Most common configuration options you need is in the Settings page of the web UI.

Other, more technical configuration options, are available through the config files. These are located in different places depending on your platform, see the `directories <config-directory>` documentation for where to find them.

Configuration options for the server, client, and default watchers are listed below:

- aw-server (Python)

 - :code:`host` Hostname to start the server on. Currently only :code:`localhost` or :code:`127.0.0.1` are supported.
 - :code:`port` Port number to start the server on.
 - :code:`storage` Type of storage for holding buckets and events. Supported types are :code:`peewee`, :code:`memory` (useful in testing), or :code:`mongodb` (MongoDB support will be removed in a future version).

- aw-client

 - :code:`hostname` Hostname of the server to connect to.
 - :code:`port` Port number of the server to connect to.

- aw-watcher-afk

 - :code:`timeout` Time in seconds with no activity required to become afk.
 - :code:`poll_time` Time in seconds between checks for activity.
 - :code:`update_time` Not yet implemented.

- aw-watcher-window:

 - :code:`poll_time` Time in seconds between window checks.
 - :code:`exclude_title` Don't track window titles
 - :code:`update_time` Not yet implemented.
