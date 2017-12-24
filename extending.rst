Extending ActivityWatch
=======================

So, you want to do something more with ActivityWatch? Great!

We've tried to make things easy for you (and ourselves) so here's some advice on how to get started.


Collecting more data
--------------------

ActivityWatch is written to be flexible to be able to gather most types of data.
Except for the included aw-watcher-window and aw-watcher-afk which tracks your application usage and are included by default in ActivityWatch, there are additional so-called :doc:`watchers` for activitywatch.

If there is some kind of data you would want to track but are not
To do this you'd want to write a so-called watcher. Watchers are small programs that collect data and send it off to the server.

See :doc:`writing-watchers`.


Fetching Data
-------------

If you want to fetch data from aw-server for visualization, exporting, backup or something we have not yet thought of, there are a few ways you can do this:

* `Exporting a Bucket <features/exporting-data.html>` If you want a complete dump of all events of bucket
* `Bucket REST API <./rest.html#get-events>`_ If you want to export raw events in a specific time interval from a bucket
* `Writing a Query <./querying-buckets.html#writing-a-query>`_ If you want to summarize/aggregate one or more buckets into more easily readable data
