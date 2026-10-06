Directories
===========

Where things get stored depends on the platform you're using. All paths should follow standard directories on their platforms, and to accomplish this we use `platformdirs <https://pypi.org/project/platformdirs/>`_ in Python code and the `dirs <https://crates.io/crates/dirs/>`_ crate in Rust code.

Each ActivityWatch component stores its data in a subdirectory named after itself.

The paths below use ``aw-server-rust`` as an example component.

.. note::
    On Windows, Python components (``aw-server``, ``aw-qt``, ``aw-watcher-afk``, ``aw-watcher-window``, ...) use one extra ``activitywatch`` level, e.g. ``C:\Users\<USER>\AppData\Local\activitywatch\activitywatch\aw-server`` for data and ``...\Local\activitywatch\activitywatch\Logs\aw-watcher-window`` for logs. Rust components (``aw-server-rust``, ``aw-sync``) use the paths listed below; ``aw-tauri`` follows them for its own config and data from the release after ``v0.14.0`` (`aw-tauri#280 <https://github.com/ActivityWatch/aw-tauri/pull/280>`_).

.. note::
    ``v0.14.0`` on Windows mistakenly stored ``aw-server-rust`` data and config, and ``aw-sync`` config, under ``AppData\Roaming`` (``%APPDATA%``) instead of ``AppData\Local`` (``%LOCALAPPDATA%``). The release after ``v0.14.0`` fixes this and migrates automatically on startup:

    - If ``AppData\Local\activitywatch\aw-server-rust`` has no database yet, the ``Roaming`` folder is copied there, verified, and the original kept as ``aw-server-rust.migrated-<date>``. Nothing is deleted or overwritten. If a Python ``aw-server`` database exists, ``aw-server-rust`` also runs the import of it that ``v0.14.0`` skipped, once.
    - If ``AppData\Local`` already has a database (you used ActivityWatch before ``v0.14.0``), it stays in use and the ``Roaming`` folder is left untouched, with a warning in the log. Events recorded while running ``v0.14.0`` are in that ``Roaming`` database and are not merged automatically.
    - If the copy cannot be completed safely, the ``Roaming`` folder keeps being used and the migration is retried on the next start.

.. note::
    These paths are pinned by tests on every platform: ``tests/test_dirs_pinned.py`` in aw-core (Python), ``test_default_paths_are_pinned`` in aw-server-rust (and aw-tauri once #280 lands), and ``test_legacy_dbfile_path_is_pinned`` in aw-server-rust (where the Python database is looked for when migrating). If you change a path, change this page and those tests together, and add a migration for existing installs.

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

- Windows: ``C:\Users\<USER>\AppData\Local\activitywatch\Logs\aw-server-rust``
- macOS: ``~/Library/Logs/activitywatch/aw-server-rust``
- Linux: ``~/.cache/activitywatch/log/aw-server-rust``

.. _cache-directory:

Cache
-----

- Windows: ``C:\Users\<USER>\AppData\Local\activitywatch\Cache\aw-server-rust``
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
