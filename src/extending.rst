Extending ActivityWatch
=======================

So, you want to do something more with ActivityWatch? Great!

We've tried to make things easy for you (and ourselves) so here's some advice on how to get started.


Collecting more data
--------------------

ActivityWatch is written to be flexible to be able to gather most types of data.
Except for the included aw-watcher-window and aw-watcher-afk which tracks your application usage, there are additional so-called :doc:`watchers` for activitywatch.
Watchers are small programs that collect data and send it off to the server.
The only requirement for what kind of data is sent to aw-server as an event is that it has to contain a starttime (and preferably a duration aswell) so it can fit on a timeline.

If you want to write a watcher of your own, see :doc:`writing-watchers`.


Fetching Data
-------------

If you want to fetch data from aw-server for visualization, exporting, backup or something we have not yet thought of, there are a few ways you can do this:

* `Exporting a Bucket <features/exporting-data>` If you want a complete dump of all events of bucket
* `Bucket REST API <api-reference>` If you want to export raw events in a specific time interval from a bucket
* `Writing a Query <querying-data>` If you want to summarize/aggregate one or more buckets into more easily readable data
