Writing your first watcher in Python
====================================

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

Writing your first watcher in Rust
==================================

To get started with writing watchers in Rust, you need to add the ``aw-client-rust`` and ``aw-model`` crates to your ``Cargo.toml`` file.
The most up-to-date versions depend directly on :gh-aw:`aw-server-rust`.

.. literalinclude:: Cargo.toml

Minimal client
--------------

Below is a minimal template client to quickly get started. Mirrors the python example above.
This example will:

* create a bucket
* insert an event
* fetch an event from an aw-server bucket
* delete the bucket again

.. literalinclude:: minimal_client.rs

Reference client
----------------

Below is a example of a watcher with more in-depth comments. Mirrors the python example above.
This example will describe how to:

* create buckets
* send events by heartbeats
* insert events without heartbeats
* do synchronous as well as asyncronous requests
* fetch events from an aw-server bucket
* delete buckets

.. literalinclude:: client.rs

It is recommended to follow conventions and use the ``aw-watcher-<name>`` naming scheme for your watcher.
It is also recommended for watchers to accept a ``--testing`` flag and a ``--port <port>`` flag to allow users to specify the port to connect to.
