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

ActivityWatch has two server implementations:

- :gh-aw:`aw-server` - The current default Python implementation
- :gh-aw:`aw-server-rust` - A Rust implementation that is the planned future default

The server handles storage and retrieval of all activities/entries in buckets. Usually there exists one bucket per watcher.

The server also hosts the Web UI (``aw-webui``) which does all communication with the server using the REST API.

Clients (watchers and importers)
--------------------------------

Since ``aw-server`` doesn't do any data collection on it's own, we need watchers that observe the world and sent the data off to ``aw-server`` for storage.

These utilize the ``aw-client`` library for making requests to the ``aw-server``.

ActivityWatch can't track everything, so sometimes you might want to import data from another source, that's where importers come in.

For a list of watchers, see :doc:`watchers`. For a list of importers see :doc:`importers`.


User interfaces
---------------

ActivityWatch currently has two user interfaces, ``aw-qt`` and ``aw-webui``.

- :gh-aw:`aw-qt` - Manages the server and watchers to make ActivityWatch easy to use for end-users.
- :gh-aw:`aw-webui` - Offers visualization and an overview of the database. Hosted by ``aw-server`` in the bundle.

Libraries
---------

Some of the logic of ActivityWatch is shared across the server and clients, for these cases we moved some logic into separate libraries.

:gh-aw:`aw-core`
^^^^^^^^^^^^^^^^

The ``aw-core`` library contains many of the essential parts of ActivityWatch, notably:

- The `buckets-and-events`
- The datastore layer
- Event transformation and queries
- Utilities (configuration, logging, decorators)

:gh-aw:`aw-client`
^^^^^^^^^^^^^^^^^^

Writing these clients is something we've tried to make as easy as possible by creating client libraries with a clear API.
A client could both be a watcher which sends data as well as a visualizer which fetches and presents data from the ``aw-server``.

Currently the primary client library is written in Python (known simply as ``aw-client``) but a client library written in JavaScript is on the way and is expected to have the same level of support in the future.

- :gh-aw:`aw-client` (Python)
- :gh-aw:`aw-client-js` (TypeScript/JavaScript, beta)
- :gh-aw:`aw-client-rust <aw-server-rust/tree/master/aw-client-rust>` (Rust, work in progress)

:gh-aw:`aw-research`
^^^^^^^^^^^^^^^^^^^^

There are also plans to create a library called ``aw-research`` to aid in
different types of analysis and transformation one might want to make using ActivityWatch data.
