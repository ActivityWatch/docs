Architecture
============

Here we hope to clarify the architecture of ActivityWatch for you. Please file an issue or pull request if you think something is missing.

.. contents::

Dependency graph
----------------

The illustration below is a graph of the fundamental dependencies between projects, these do not reflect the folder structure.

.. graphviz:: dependency.dot

Server
------

Known as :gh-aw:`aw-server`, it handles storage and retrieval of all activities/entries in buckets. Usually there exists one bucket per watcher.

The server also hosts the Web UI (aw-webui) which does all communication with the server using the REST API.

Clients (watchers, importers, and observers)
--------------------------------------------

Since aw-server doesn't do any data collection on it's own, we need watchers that observe the world and sent the data off to aw-server for storage.

These utilize the aw-client library for making requests to the aw-server.

For a list of watchers, see :doc:`watchers`. For a list of importers see :doc:`importers`.


User interfaces
---------------

ActivityWatch currently has two user interfaces, aw-qt and aw-webui.

- :gh-aw:`aw-qt` - Manages the server and watchers to make ActivityWatch easy to use for end-users.
- :gh-aw:`aw-webui` - Offers visualization and an overview of the database. Hosted by aw-server in the bundle.

Libraries
---------

Some of the logic of ActivityWatch is shared across the server and clients, for these cases we moved some logic into separate libraries.

aw-core
^^^^^^^

The aw-core library contains many of the essential parts of ActivityWatch, notably:

- The `buckets-and-events`
- The datastore layer
- Event transformation and queries
- Utilities (configuration, logging, decorators)

aw-client
^^^^^^^^^

Writing these clients is something we've tried to make as easy as possible by creating client libraries with a clear API.
A client could both be a watcher which sends data as well as a visualizer which fetches and presents data from the aw-server.

Currently the primary client library is written in Python (known simply as aw-client) but a client library written in JavaScript is on the way and is expected to have the same level of support in the future.

- :gh-aw:`aw-client` (Python)
- :gh-aw:`aw-client-js` (TypeScript/JavaScript, beta)
- :gh-aw:`aw-client-rust <aw-server-rust/tree/master/aw-client-rust>` (Rust, work in progress)

aw-analysis
^^^^^^^^^^^

There are also plans to create a library called :gh-aw:`aw-analysis` to aid in
different types of analysis and transformation one might want to make using ActivityWatch data.
