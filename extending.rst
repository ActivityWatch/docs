Extending ActivityWatch
=======================

So, you want to do something more with ActivityWatch? Great!

We've tried to make things easy for you (and ourselves) so here's some advice on how to get started.


Collecting more data
--------------------

To do this you'd want to write a so-called watcher. Watchers are small programs that collect data and send it off to the server.

See :doc:`writing-watchers`.


Exporting data programatically
------------------------------

Exporting data is as simple as:

TODO


Writing visualizers
-------------------

.. note::
    This section is uncomplete and should probably be moved to it's own section later

There are multiple ways to analyze data in activitywatch.

aw-server supplies an "/query" endpoint (also accesible via aw-client's query method) which supplies a basic scripting language which you can utilize to do transformations on the server-side.
This option is good for basic analysis and for lightweight clients (such as aw-webui).

Another option is to fetch events from the "/buckets/bucketname/events" endpoint (also accesible via aw-client's get_events method) and either program your own transformations or use transformation methods available in the aw-analysis python library (which includes all transformations available in the query endpoint).

This is an example of how you can do analysis and aggregation with the query method in aw-client

.. literalinclude:: examples/query_client.py

