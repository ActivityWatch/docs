REST API
========

ActivityWatch uses a REST API for all communication between aw-server and clients.
Most applications should never use HTTP directly but should instead use the client libraries available.
If no such library yet exists for a given language, this document is meant to provide enough specification to create one.

.. warning::
    The API is currently under development, and is subject to change.
    It will be documented in better detail when first version has been frozen.

.. note::
    Part of the documentation might be outdated, you can get up-to-date API documentation
    in the API browser available from the web UI of your aw-server instance.

.. contents::


REST Security
-------------

.. note::
    Our current security consists only of not allowing non-localhost connections, this is likely to be the case for quite a while.

Clients might in the future be able to have read-only or append-only access to buckets, providing additional security and preventing compromised clients from being able to cause a severe security breach.
All clients will probably also encrypt data in transit.


REST Reference
--------------

.. note::
    This reference is highly incomplete. For an interactive view of the API, try out the API playground running on your local server at: http://localhost:5600/api/

Buckets API
~~~~~~~~~~~

The most common API used by ActivityWatch clients is the API providing read and append access buckets.
Buckets are data containers used to group data together which shares some metadata (such as client type, hostname or location).

Get Bucket Metadata
^^^^^^^^^^^^^^^^^^^

Will return 404 if bucket does not exist

.. code-block:: shell

    GET /api/0/buckets/<bucket_id>

List
^^^^

.. code-block:: shell

    GET /api/0/buckets/

Create
^^^^^^

Will return 304 if bucket already exists

.. code-block:: shell

    POST /api/0/buckets/<bucket_id>


Events API
~~~~~~~~~~

The most common API used by ActivityWatch clients is the API providing read and append `Events <../buckets-and-events>` to buckets.
Buckets are data containers used to group data together which shares some metadata (such as client type, hostname or location).

Get events
^^^^^^^^^^

.. code-block:: shell

    GET /api/0/buckets/<bucket_id>/events

Create event
^^^^^^^^^^^^

.. code-block:: shell

    POST /api/0/buckets/<bucket_id>/events

Heartbeat API
~~~~~~~~~~~~~

The `heartbeat <heartbeats>` API is one of the most useful endpoints for writing watchers.

.. code-block:: shell

    POST /api/0/buckets/<bucket_id>/heartbeat

Query API
~~~~~~~~~~~~~

**TODO: Add link to writing queries once that page is done**
