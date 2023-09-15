Directories
===========

Where things get stored depends on the platform you're using. All paths should follow standard directories on their platforms, and to accomplish this we use `appdirs <https://pypi.org/project/appdirs/>`_ in Python code and `appdirs-rs <https://crates.io/crates/appdirs/>`_ in Rust code.

.. _data-directory:

Data
----

- Windows: ``%LocalAppData%\activitywatch\activitywatch``
- macOS: ``~/Library/Application Support/activitywatch``
- Linux: ``~/.local/share/activitywatch``

.. _config-directory:

Config
------


- Windows: ``%LocalAppData%\activitywatch\activitywatch``
- macOS: ``~/Library/Application\ Support/activitywatch/``
- Linux: ``~/.config/activitywatch``, or the path defined by the :code:`$XDG_CONFIG_HOME` environment variable.

.. _logs-directory:

Logs
----

- Windows: ``C:\Users\<USER>\AppData\Local\activitywatch\activitywatch``
- macOS: ``~/Library/Logs/activitywatch``
- Linux: ``~/.cache/activitywatch/log`` 

.. _cache-directory:

Cache
-----

- Windows: TODO
- macOS: TODO
- Linux: ``~/.cache/activitywatch``
