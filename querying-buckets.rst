Querying Buckets
================

There are a couple of ways to query data in activitywatch.

aw-server supplies an "/query" endpoint (also accesible via aw-client's query method) which supplies a basic scripting language which you can utilize to do transformations on the server-side.
This option is good for basic analysis and for lightweight clients (such as aw-webui).

Another option is to fetch events from the "/buckets/bucketname/events" endpoint (also accesible via aw-client's get_events method) and either program your own transformations or use transformation methods available in the aw-analysis python library (which includes all transformations available in the query endpoint). This require a lot of more work since you will likely have to reprogram transformations already available in the query API, but on the other hand it is much more flexible.


Writing a Query
---------------

.. note::
    This section is still WIP

This is an example of how you can do analysis and aggregation with the query method in aw-client

.. literalinclude:: examples/query_client.py


Fetching Raw Events
-------------------

**TODO:** Write this section

`Bucket REST API <./rest.html#get-events>`_
