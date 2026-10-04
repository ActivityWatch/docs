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

.. _profiles:

Profiles
--------

Starting with ``v0.14``, you can run named profiles. A profile is an isolated ActivityWatch instance with its own data, config, and logs, which can run at the same time as your normal instance. The ``default`` profile is the normal install, and ``testing`` is the profile used by the ``--testing`` flag (which runs on port 5666).

To start a profile, run ``aw-qt --profile <name>``. aw-qt passes the profile on to the modules it starts through the ``AW_PROFILE`` environment variable. When starting modules separately, set ``AW_PROFILE=<name>`` for each of them; ``aw-server``, ``aw-server-rust``, and ``aw-sync`` also accept ``--profile <name>``.

For a profile other than ``default``, every directory above uses ``activitywatch-<name>`` in place of ``activitywatch``. For example, the Linux data directory for a profile named ``research`` is ``~/.local/share/activitywatch-research/aw-server-rust``.

Profile names must be lowercase letters, digits, ``-`` or ``_`` (starting with a letter or digit), and at most 32 characters.

.. note::
    A named profile uses port 5600 unless configured otherwise, which collides with your default instance. Set a different ``port`` in that profile's server and ``aw-client`` config files (see :doc:`configuration`) before running both at once.
