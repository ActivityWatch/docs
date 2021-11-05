Data model
==========

.. contents::

Buckets
-------

Each bucket contains a series of events and metadata for those events (such as their type and what collected them).

It is recommended to have one bucket per watcher and host. A bucket should always receive data from the same source.

For example, if we want to write a watcher that should track the currently active window we would first have it create a bucket named 'example-watcher-window_myhostname' and then start reporting events to that bucket (using :ref:`heartbeats`).

.. code-block:: javascript

    bucket = {
      "id": "aw-watcher-test_myhostname",
      "created": "2017-05-16T13:37:00.000000",
      "name": "A short but descriptive human readable bucketname",
      "type": "com.example.test",       // Type of events in bucket
      "client": "example-watcher-test", // Identifier of client software used to report data
      "hostname": "myhostname",         // Hostname of device where data was collected
    }

For information about the "type" field, see examples at :ref:`event types`.

Events
------

The event model used by ActivityWatch is pretty simple, here is the JSON representation:

.. code-block:: javascript

    event = {
      "timestamp": "2016-04-27T15:23:55Z",  // ISO8601 formatted timestamp
      "duration": 3.14,                     // Duration in seconds
      "data": {"key": "value"},  // A JSON object, the schema of this depends on the event type
    }

It should be noted that all timestamps are stored as UTC. Timezone information (UTC offset) is currently discarded.

The "data" field can be any JSON object, but it is recommended that every event in a bucket should follow some format according to the bucket type, so the data is easy to analyze.

Heartbeats
``````````

Heartbeats is a method that merges adjacent events with identical data (within a ``pulsetime`` window). This is useful to save on storage space and disk IO, and it is recommended that watchers use it when sending events to the server.

A merge of two events A and B is done if their ``data`` is identical and their timestamps are within the ``pulsetime`` window. The resulting event will have the earlier timestamp, and a duration to match the difference between the timestamps.

See for example :py:meth:`aw_transform.heartbeat_merge` or the :ref:`heartbeat REST API <Heartbeat API>`.

Event types
```````````

To separate different types of data in ActivityWatch there is the event type. A buckets event type specified the schema of the events in the bucket.

By creating standards for watchers to use we enable easier transformation and visualization.

web.tab.current
~~~~~~~~~~~~~~~

An event type for the currently active webbrowser tab.

.. code-block:: javascript

    {
        url: string,
        title: string,
        audible: bool,
        incognito: bool,
    }

app.editor.activity
~~~~~~~~~~~~~~~~~~~

An event type for tracking the currently edited file.

.. code-block:: javascript

    {
        file: string,     // full path to file, folders separated by forward slash
        project: string,  // full path of cwd, folders separated by forward slash
        language: string, // name of language of the file
    }

currentwindow
~~~~~~~~~~~~~

.. note::
    There are suggestions to improve/change this format
    (see :issue:`201`)

.. code-block:: javascript

    {
        app: string,
        title: string,
    }

afkstatus
~~~~~~~~~

.. note::
    There are suggestions to improve/change this format
    (see :issue:`201`)

.. code-block:: javascript

    {
        status: string   // "afk" or "not-afk"
    }
