*********
Migrating
*********

In some cases, such as in an upgrade, ActivityWatch needs to migrate data. Usually this is nothing you should have to think about, but in some cases it is useful to know what happens and what you can do when things go wrong.

Migrating to aw-server-rust
===========================

In an upcoming version, ActivityWatch will switch the default server implementation from aw-server (hereafter aw-server-python for clarity) to aw-server-rust. The reason for this is that aw-server-rust has far superior performance, and has almost full feature parity with aw-server-python (see `server comparison`).


Using aw-server-rust by default
-------------------------------

To set aw-server-rust to be automatically started instead of aw-server-python, you need to go into the `Configuration` file ``aw-qt.toml`` (located in the config :doc:`directories`) and set it to the following:

.. code-block::

    [aw-qt]
    autostart_modules = ["aw-server-rust", "aw-watcher-afk", "aw-watcher-window"]

Make sure you've uncommented the lines, as otherwise they won't be read.

Now you should be able to just restart aw-qt, wait for the initial import from aw-server-python to happen (might take a few minutes, depending on db size), and then you should be good to go!


Importing from aw-server-python
-------------------------------

On aw-server-rust startup, if no database already exists, it will automatically look for an aw-server-python database (only the default peewee datastore supported) and import it into the new database. This can cause some slowness on first startup, especially if you have a large aw-server-python database.

The automatic import only runs when the aw-server-rust database is first created. If you've ran aw-server-rust before (for example, tried it and switched back to aw-server-python), the import will not run again, and data recorded by aw-server-python since then will be missing from aw-server-rust. The server log says so on startup ("Datastore was already initialized, skipping legacy import").

Running the import manually
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Newer versions of aw-server-rust (released after v0.14.0) can re-run the import explicitly. Stop the running aw-server-rust (e.g. quit aw-qt), then start it once with ``--import-legacy``:

.. code-block:: sh

    aw-server-rust --import-legacy

(The binary is named ``aw-server`` if you built aw-server-rust from source.)

The import is idempotent: buckets that already exist in aw-server-rust only get the events they're missing, so running it more than once does not create duplicates. Once it's done you can restart ActivityWatch normally.

By default the legacy database is looked up at ``<data dir>/activitywatch/aw-server/peewee-sqlite.v2.db`` (see :doc:`directories`). If yours is somewhere else, point to it with ``--legacy-dbpath``:

.. code-block:: sh

    aw-server-rust --import-legacy --legacy-dbpath /path/to/peewee-sqlite.v2.db

Setting a custom ``--dbpath`` disables the automatic import; add ``--import-legacy`` to run it anyway.

On older versions without ``--import-legacy``, you can retrigger the import by stopping aw-server-rust, moving/removing your aw-server-rust database file, and then starting aw-server-rust again.

Another option for migrating is to use the "Export all"/"Import all" buttons under the "Raw data" menu in the web UI. This should work with all datastores in aw-server-python.

.. note::
    Importing an aw-server-rust export into aw-server-python is untested and might break in unexpected ways, potentially leading to data loss.


Database schema migrations
==========================

Between versions aw-server-rust might run migrations that upgrade the database schema. These should always go as planned (if not, file an issue), but may mean that you can't downgrade to an older version.
