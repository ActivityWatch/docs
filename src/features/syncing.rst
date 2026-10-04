Syncing
=======

Syncing is one of the most requested features for ActivityWatch. Basic syncing has been available through the ``aw-sync`` module since ``v0.13.0``, and is still in beta.

See :doc:`/syncing` for how it works and how to set it up, and the `aw-sync README <https://github.com/ActivityWatch/aw-server-rust/tree/master/aw-sync>`_ for details.

Old syncing prototype
---------------------

.. note:: The below details the architecture of the old syncing prototype, which predates ``aw-sync``. It is kept here for reference.

Before ``aw-sync``, syncing was explored with a proof-of-concept prototype. You can read what was discussed in this issue: https://github.com/ActivityWatch/activitywatch/issues/35

Here's a graph showing how data flowed in the old syncing prototype:

.. graphviz:: syncing.dot

Green boxes are source buckets (only written to and read from by the owner). Yellow boxes are the synced version of buckets (written to by the owner, read by consumers). Gray boxes are local copies of remote buckets.

It can be briefly described as follows:

Device A takes its buckets to sync and puts the data in the synced copy, the synced copy gets distributed to device B, device B takes the synced copy and imports it to it's local datastore.
