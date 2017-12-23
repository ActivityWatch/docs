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


Writing visualizers
-------------------

.. note::
    This section is uncomplete and should probably be moved to it's own section later

There are a couple of ways to analyze data in activitywatch.

aw-server supplies an "/query" endpoint (also accesible via aw-client's query method) which supplies a basic scripting language which you can utilize to do transformations on the server-side.
This option is good for basic analysis and for lightweight clients (such as aw-webui).

Another option is to fetch events from the "/buckets/bucketname/events" endpoint (also accesible via aw-client's get_events method) and either program your own transformations or use transformation methods available in the aw-analysis python library (which includes all transformations available in the query endpoint). This require a lot of more work since you will likely have to reprogram transformations already available in the query API, but on the other hand it is much more flexible.

This is an example of how you can do analysis and aggregation with the query method in aw-client

.. literalinclude:: examples/query_client.py

