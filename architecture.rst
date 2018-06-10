Architecture
============

Here we hope to clarify the architecture of ActivityWatch for you. Please file an issue or pull request if you think something is missing.

Server
------

Known as aw-server, it handles storage and retrieval of all activities/entries in buckets. Usually there exists one bucket per watcher.

The server also hosts the Web UI (aw-webui) which does all communication with the server using the REST API.

Watchers
--------

Since aw-server doesn't do any data collection on it's own, we need watchers that observe the world and sent the data off to aw-server for storage.

These utilize the :doc:`aw-client` library for making requests to the aw-server.

For a list of watchers, see :doc:`watchers`.


User interfaces
---------------

ActivityWatch currently has two user interfaces, aw-qt and aw-webui.

 - `aw-qt <https://github.com/ActivityWatch/aw-qt>`_ - Manages the server and watchers to make ActivityWatch easy to use for end-users.
 - `aw-webui <https://github.com/ActivityWatch/aw-webui>`_ - Offers visualization and an overview of the database. Hosted by aw-server in the bundle.

Libraries
---------

Some of the logic of ActivityWatch is shared across the server and clients, for these cases we moved some logic into seperate libraries.

aw-core
^^^^^^^

The aw-core library contains many of the essential parts of ActivityWatch, notably:

 - The `buckets-and-events`
 - The datastore layer
 - Utilities (configuration, logging, decorators)

aw-client
^^^^^^^^^

Writing these clients is something we've tried to make as easy as possible by creating client libraries with a clear API.
A client could both be a watcher which sends data as well as a visualizer which fetches and presents data from the aw-server.

Currently the primary client library is written in Python (known simply as aw-client) but a client library written in JavaScript is on the way and is expected to have the same level of support in the future.

 - `aw-client <https://github.com/ActivityWatch/aw-client>`_ (Python)
 - `aw-client-js <https://github.com/ActivityWatch/aw-client-js>`_ (JavaScript, work in progress)
 - `aw-client-rust <https://github.com/ActivityWatch/aw-client-rust>`_ (Rust, work in progress)

aw-analysis
^^^^^^^^^^^

There are also plans to create a library called `aw-analysis <https://github.com/ActivityWatch/aw-analysis>`_ to aid in
different types of analysis and transformation one might want to make using ActivityWatch data.
