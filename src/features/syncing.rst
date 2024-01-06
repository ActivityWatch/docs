Syncing
=======

Syncing is one of the most requested features for ActivityWatch. It is currently being worked on and is in a testing phase.

You can read more about it, and how to try the early release, in the `aw-sync README <https://github.com/ActivityWatch/aw-server-rust/tree/master/aw-sync>`_.

Here is a tweet announcing the early MVP: https://twitter.com/ErikBjare/status/1519399784234246147

Old syncing prototype
---------------------

.. note:: The below details the architecture of the old syncing prototype. It is kept here for reference.

There isn't much written about syncing yet since it's not yet implemented in a stable release. However, there does exist a working proof-of-concept prototype which should be easy to implement once details have been finalized. You can read what has been discussed in this issue: https://github.com/ActivityWatch/activitywatch/issues/35

Here's a graph showing how data flows in the current syncing prototype:

.. graphviz:: syncing.dot

Green boxes are source buckets (only written to and read from by the owner). Yellow boxes are the synced version of buckets (written to by the owner, read by consumers). Gray boxes are local copies of remote buckets.

It can be briefly described as follows:

Device A takes its buckets to sync and puts the data in the synced copy, the synced copy gets distributed to device B, device B takes the synced copy and imports it to it's local datastore.
