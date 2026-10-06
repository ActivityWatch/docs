REST API
========

ActivityWatch uses a REST API for all communication between aw-server and clients.
Most applications should never use HTTP directly but should instead use the client libraries available.
If no such library yet exists for a given language, this document is meant to provide enough specification to create one.

If you are building an AI assistant or agent integration, start with
:doc:`../examples/agents-and-ai` and prefer bounded, aggregated payloads over raw
event access.

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
    By default, the server only listens on localhost and the API requires no authentication. aw-server-rust supports opt-in API key authentication: when enabled, requests must include an ``Authorization: Bearer <api_key>`` header. See :doc:`../security` for details.

Clients might in the future be able to have read-only or append-only access to buckets, providing additional security and preventing compromised clients from being able to cause a severe security breach.
All clients will probably also encrypt data in transit.


REST Reference
--------------

.. note::
    This reference covers the endpoints watchers and clients use most. For an interactive view of the API, try out the API playground running on your local server at: http://localhost:5600/api/

All endpoints live under ``/api/0/``. Request and response bodies are JSON unless noted.
Timestamps must be RFC 3339 with a timezone (``2026-10-01T10:00:00Z``).
Durations are in seconds.

.. note::
    There are two server implementations: ``aw-server-rust`` (the default) and ``aw-server`` (Python).
    They agree on the happy path but differ on error handling. Differences are called out below.
    Do not rely on error response bodies: aw-server-rust returns an HTML page for 400/422 errors,
    and some invalid inputs cause a 500 on the Python server.

Server info
~~~~~~~~~~~

.. code-block:: shell

    GET /api/0/info

Returns ``{"hostname": ..., "version": ..., "testing": ..., "device_id": ...}``.

Buckets API
~~~~~~~~~~~

The most common API used by ActivityWatch clients is the API providing read and append access buckets.
Buckets are data containers used to group data together which shares some metadata (such as client type, hostname or location).

Get Bucket Metadata
^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    GET /api/0/buckets/<bucket_id>

Status codes: ``200``, ``404`` if the bucket does not exist.

List
^^^^

.. code-block:: shell

    GET /api/0/buckets/

Returns an object mapping bucket id to bucket metadata.

Create
^^^^^^

.. code-block:: shell

    POST /api/0/buckets/<bucket_id>

Body (all three fields are required):

.. code-block:: json

    {"client": "aw-watcher-example", "type": "app.example", "hostname": "my-host"}

Status codes: ``200`` created, ``304`` if the bucket already exists (the existing bucket is left unchanged),
``400`` for malformed JSON, ``422`` for missing fields (aw-server-rust; the Python server returns ``500``).

Delete
^^^^^^

.. code-block:: shell

    DELETE /api/0/buckets/<bucket_id>?force=1

Deletes the bucket **and all its events**. The ``force=1`` parameter is required.
Status codes: ``200``, ``404`` if the bucket does not exist.

Events API
~~~~~~~~~~

The events API provides read and append access to `Events <../buckets-and-events>` in a bucket.

Get events
^^^^^^^^^^

.. code-block:: shell

    GET /api/0/buckets/<bucket_id>/events?start=<rfc3339>&end=<rfc3339>&limit=<n>

All parameters are optional. Events are returned newest first, as a list of
``{"id": 1, "timestamp": "...", "duration": 10.0, "data": {...}}``.
A negative ``limit`` means no limit.

Status codes: ``200``, ``400`` if ``start``/``end`` cannot be parsed, ``404`` if the bucket does not exist.

Create events
^^^^^^^^^^^^^

.. code-block:: shell

    POST /api/0/buckets/<bucket_id>/events

Body: a JSON **list** of events, each with ``timestamp``, ``duration`` and ``data`` (an object):

.. code-block:: json

    [{"timestamp": "2026-10-01T10:00:00Z", "duration": 10, "data": {"app": "firefox"}}]

Always send a list, even for a single event. aw-server-rust rejects a bare object with ``422``,
while the Python server accepts it, so a client tested only against the Python server can break on the default one.

Status codes: ``200``, ``404`` if the bucket does not exist, ``422`` for an invalid body (aw-server-rust).

Count events
^^^^^^^^^^^^

.. code-block:: shell

    GET /api/0/buckets/<bucket_id>/events/count?start=<rfc3339>&end=<rfc3339>

Returns the number of events as a bare JSON number.

Get / delete a single event
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    GET    /api/0/buckets/<bucket_id>/events/<event_id>
    DELETE /api/0/buckets/<bucket_id>/events/<event_id>

``GET`` returns ``404`` for an unknown id on the Python server but ``500`` on aw-server-rust.
``DELETE`` returns ``200`` even if no event with that id exists.

Heartbeat API
~~~~~~~~~~~~~

The `heartbeat <heartbeats>` API is one of the most useful endpoints for writing watchers.

.. code-block:: shell

    POST /api/0/buckets/<bucket_id>/heartbeat?pulsetime=<seconds>

The ``pulsetime`` query parameter is **required** and must be a number: it is the maximum gap, in seconds,
between two heartbeats with identical ``data`` for them to be merged into one event.
Requests without it are rejected (``400`` on the Python server, an HTML ``422`` on aw-server-rust).

Body: a single event object (not a list), with ``timestamp``, ``duration`` (usually ``0``) and ``data``:

.. code-block:: json

    {"timestamp": "2026-10-01T11:00:05Z", "duration": 0, "data": {"app": "firefox"}}

Returns the resulting (possibly merged) event. Status codes: ``200``, ``404`` if the bucket does not exist,
``400``/``422`` for an invalid body or ``pulsetime``.

Query API
~~~~~~~~~

See `Writing Queries <./../examples/querying-data.html>`_ for the query language.

.. code-block:: shell

    POST /api/0/query/

.. code-block:: json

    {
      "timeperiods": ["2026-10-01T00:00:00Z/2026-10-02T00:00:00Z"],
      "query": ["events = query_bucket(\"my-bucket\");", "RETURN = events;"]
    }

``timeperiods`` is a list of ``start/end`` RFC 3339 intervals and ``query`` is a list of statements
(a single string is rejected). The response is a list with one result per time period.

Status codes: ``200``, ``422`` for a malformed request body (aw-server-rust), ``400`` for a query that fails to parse (Python server).
aw-server-rust reports query errors (syntax errors, undefined variables, unknown buckets) as ``500`` with a JSON ``message``.

Export and import
~~~~~~~~~~~~~~~~~

.. code-block:: shell

    GET  /api/0/buckets/<bucket_id>/export
    GET  /api/0/export
    POST /api/0/import

Per-bucket export returns ``{"buckets": {<bucket_id>: {..., "events": [...]}}}``, or ``404`` for an unknown bucket.
``/api/0/import`` takes that same format (JSON body, or a multipart file upload as the web UI does)
and returns ``400`` for malformed input.
Importing into a bucket that already exists is not consistent between servers: aw-server-rust (master) merges
the events, while the Python server fails with ``500``.

Settings API
~~~~~~~~~~~~

Key-value storage for client settings (used by the web UI).

.. code-block:: shell

    GET    /api/0/settings
    GET    /api/0/settings/<key>
    POST   /api/0/settings/<key>
    DELETE /api/0/settings/<key>

``GET`` of an unset key returns ``null``. ``POST`` takes any JSON value as the body and returns ``201`` on aw-server-rust
(``200`` on the Python server), and ``400`` for invalid JSON.
``DELETE`` exists only on aw-server-rust; on the Python server it returns ``405`` and a falsy ``POST`` value deletes the key instead.
