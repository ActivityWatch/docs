Buckets and Events
==================

Buckets
-----------

.. code-block:: javascript

    bucket = {
      "id": "aw-watcher-mywatcher_myhostname",
      "created": "2017-05-16T13:37:00.000000",
      "name": "A short but descriptive human readable bucketname",
      "type": "mybuckettype",
      "client": "aw-watcher-mywatcher",
      "hostname": "myhostname",
    }

In ActivityWatch we try and separate each kind of datapoint.
Normally what is most convenient is to have one bucket per client and host.
For example if we have a watcher which tracks info about the focused window on your computer we would upon startup create a bucket named 'aw-watcher-window_my-host-name' to fill all of our events with datapoints to.

Each bucket also has a buckettype which specifies the format of the events inside the buckets. See examples at :ref:`buckettypes`


Events
-----------

The ActivityWatch event model is pretty simple, here's its representation in JSON:

.. code-block:: javascript

    event = {
      "timestamp": "2016-04-27T15:23:55Z",  // ISO8601 formatted timestamp
      "duration": 3.14,                     // Duration in seconds
      "data": {"key": "value"},  // A JSON object, the schema of this depends on the bucket type
    }

It should be noted that all timestamps are stored as UTC. Timezone information (UTC offset) is currently discarded.

The content in the "data" field could be any JSON object, but it is recommended that every event in a bucket should follow some format depending on the buckettype so the data is easy to analyze.


Buckettypes
-----------

The buckettype specifies the format of the data in the event, so for example for the bucket of our focused window watcher we could have the buckettype 'currentwindow'.
The buckettype is just a ordinary string, but it is good for clients who want to visualize the data in ActivityWatch to know what the buckets contain.

web.tab.current

.. code-block:: javascript

    {
        url: string,
        title: string,
        audible: bool,
        icognito: bool,
    }

app.editor.activity

.. code-block:: javascript

    {
        file: string, (full path to file)
        project: string, (full path of cwd)
        language: string, (name of language of the file)
    }


currentwindow

.. note::
	There are suggestions to improve/change this format
	(see `GitHub issue
	<https://github.com/ActivityWatch/activitywatch/issues/201>`_)

.. code-block:: javascript

    {
        app: string,
        title: string,
    }


afkstatus

.. note::
	There are suggestions to improve/change this format
	(see `GitHub issue
	<https://github.com/ActivityWatch/activitywatch/issues/201>`_)

.. code-block:: javascript

    {
        status: string ("afk" or "not-afk")
    }
