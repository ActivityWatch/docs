Writing your first watcher
==========================

Writing watchers for ActivityWatch is pretty easy, all you need is the :code:`aw-client` library.

Minimal client
--------------

Below is a minimal template client to quickly get started.
This example will:

* create a bucket
* insert an event
* fetch an event from an aw-server bucket
* delete the bucket again

.. literalinclude:: examples/minimal_client.py


Reference client
----------------

Below is a example of a watcher with more in-depth comments.
This example will describe how to:

* how to create buckets
* how to send events by heartbeats
* how to insertion events without heartbeats
* how to do syncronous as well as asyncronous requests
* fetch events from a aw-server bucket
* delete buckets

.. literalinclude:: examples/client.py

