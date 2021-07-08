Usage
============

Here we hope to clarify the founder's designed usage of ActivityWatch.

.. contents::

Intended Use of ActivityWatch
----------------

The `vision <https://github.com/ActivityWatch/activitywatch/issues/236>`_ of ActivityWatch has always been for the betterment of the user.
May it be for personal, business, or solely research.


Monitoring of Unaware Individuals Using ActivityWatch
------

In line with ActivityWatch's vision, the users of ActivityWatch should have full consent when they utilize this software.

Data privacy is a right to each individual, and the use of this program to monitor people without their knowledge will go against the design of ActivityWatch.


Employee Monitoring Using ActivityWatch
--------------------------------------------

The monitoring of employees to check their activities can cause harm to workers and is highly illegal employee surveillance.

The ActivityWatch team is currently planning implementations for an enterprise feature (presently called Report) for the program.


Report Feature
---------------

The `plans <https://github.com/ActivityWatch/activitywatch/issues/233>`_ for the Report feature would be a whitelisting system. Users can whitelist which activities to report,
preventing personal data from being leaked.

It would also relay the employers with only work-related activities.

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
 - :gh-aw:`aw-client-rust` (Rust, work in progress)

aw-analysis
^^^^^^^^^^^

There are also plans to create a library called :gh-aw:`aw-analysis` to aid in
different types of analysis and transformation one might want to make using ActivityWatch data.
