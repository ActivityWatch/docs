Writing your first watcher
==========================

Writing watchers for ActivityWatch is pretty easy, all you need is the :code:`aw-client` library.

.. note:: These examples run the client in *testing* mode, which means that it will try to connect to an aw-server in testing mode on the port 5666 instead of the normal 5600.

Minimal client
--------------

Below is a minimal template client to quickly get started.
This example will:

* create a bucket
* insert an event
* fetch an event from an aw-server bucket
* delete the bucket again

.. literalinclude:: minimal_client.py


Reference client
----------------

Below is a example of a watcher with more in-depth comments.
This example will describe how to:

* create buckets
* send events by heartbeats
* insert events without heartbeats
* do synchronous as well as asyncronous requests
* fetch events from an aw-server bucket
* delete buckets

.. literalinclude:: client.py

