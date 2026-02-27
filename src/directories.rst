Directories
===========

Where things get stored depends on the platform you're using. All paths should follow standard directories on their platforms, and to accomplish this we use `appdirs <https://pypi.org/project/appdirs/>`_ in Python code and the `dirs <https://crates.io/crates/dirs/>`_ crate in Rust code.

Each ActivityWatch component stores its data in a subdirectory named after itself.

The paths below use ``aw-server-rust`` as an example component.

.. _data-directory:

Data
----

This is where the SQLite database and other persistent data is stored.

- Windows: ``C:\Users\<USER>\AppData\Local\activitywatch\aw-server-rust``
- macOS: ``~/Library/Application Support/activitywatch/aw-server-rust``
- Linux: ``~/.local/share/activitywatch/aw-server-rust``

.. _config-directory:

Config
------

Configuration files for each component.

- Windows: ``C:\Users\<USER>\AppData\Local\activitywatch\aw-server-rust``
- macOS: ``~/Library/Application Support/activitywatch/aw-server-rust``
- Linux: ``~/.config/activitywatch/aw-server-rust``, or the path defined by the :code:`$XDG_CONFIG_HOME` environment variable.

Other components have their own config directories, e.g. ``aw-watcher-afk``, ``aw-watcher-window``.

.. _logs-directory:

Logs
----

- Windows: ``C:\Users\<USER>\AppData\Local\activitywatch\aw-server-rust\logs``
- macOS: ``~/Library/Logs/activitywatch/aw-server-rust``
- Linux: ``~/.cache/activitywatch/log/aw-server-rust``

.. _cache-directory:

Cache
-----

- Windows: ``C:\Users\<USER>\AppData\Local\activitywatch\aw-server-rust\cache``
- macOS: ``~/Library/Caches/activitywatch/aw-server-rust``
- Linux: ``~/.cache/activitywatch/aw-server-rust``
