*********
Migrating
*********

In some cases, such as in an upgrade, ActivityWatch needs to migrate data. Usually this is nothing you should have to think about, but in some cases it is useful to know what happens and what you can do when things go wrong.

Migrating to aw-server-rust
===========================

In an upcoming version, ActivityWatch will switch the default server implementation from aw-server (hereafter aw-server-python for clarity) to aw-server-rust. On aw-server-rust startup, if no database already exists, it will automatically look for an aw-server-python database (only the default peewee datastore supported) and import it into the new database. This can cause some slowness on first startup, especially if you have a large aw-server-python database.

If you've ran aw-server-rust before that version, but switched back, this import has already been triggered, and the import will therefore not run a second time. This can cause you to have old data in the aw-server-rust database. You can retrigger the import by stopping aw-server-rust, moving/removing your aw-server-rust database file, and then starting aw-server-rust again.

Another option for migrating is to use the "Export all"/"Import all" buttons under the "Raw data" menu in the web UI. This should work with all datastores in aw-server-python.

.. note::
    Importing an aw-server-rust export into aw-server-python is untested and might break in unexpected ways, potentially leading to data loss.


Database schema migrations
==========================

Between versions aw-server-rust might run migrations that upgrade the database schema. These should always go as planned (if not, file an issue), but may mean that you can't downgrade to an older version.
