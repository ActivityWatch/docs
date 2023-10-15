Querying Data
=============

There are a couple of ways to query data in ActivityWatch.

aw-server supplies a "/query" endpoint (also accessible via aw-client's query method) which supplies a basic scripting language which you can utilize to do transformations on the server-side.
This option is good for basic analysis and for lightweight clients (such as aw-webui).

Another option is to fetch events from the "/buckets/bucketname/events" endpoint (also accessible via aw-client's get_events method) and either program your own transformations or use transformation methods available in the aw-analysis python library (which includes all transformations available in the query endpoint). This requires a lot of more work since you will likely have to reprogram transformations already available in the query API, but on the other hand it is much more flexible.


Writing a Query
---------------

.. note::
    This section is still WIP.
    There is still no documentation of all the transform functions, but for most simple queries these examples should be enough.

Queries are the easiest yet advanced way to get events from aw-server buckets in a format which fits most needs.
Queries can be done by doing a POST request to aw-server either manually or with the aw-client library.

For an incomplete API reference of the transform functions, see the API reference for :py:mod:`aw_transform` and :py:mod:`aw_query`.

In a query you start by getting events from a bucket and assign that collection of events to a variable, then there are multiple transform functions which you can use to for example filter, limit, sort, and merge events from a bucket.
After that you assign what you want to receive from the request to the RETURN variable.

Magic Variables:
    There is a magic variable `__CATEGORIES__` you can use in the web UI's Query Explorer to include your configured categories in your query.

    Here's an example of using this variable to find all events categorized as "Web Browsing"

    .. code-block:: python

        events = flood(query_bucket(find_bucket("aw-watcher-window_")));
        not_afk = flood(query_bucket(find_bucket("aw-watcher-afk_")));
        not_afk = filter_keyvals(not_afk, "status", ["not-afk"]);
        events = filter_period_intersect(events, not_afk);
        events = categorize(events, __CATEGORIES__);
        events = filter_keyvals(events, "$category", [["Work"]]);
        RETURN = sort_by_duration(events);

Minimal example:
    Minimal query which only gets events from a bucket and returns it:

    .. code-block:: bash

        events = query_bucket("my_bucket");
        RETURN = events;


Example which arranges a hierarchy:
    A query which merges events from a bucket in a key1->key2 hierarchy:

    .. code-block:: bash

        events = query_bucket("my_bucket");
        events = merge_events_by_keys(events, "merged_key1", "merged_key2");
        RETURN = events;


Example combining window and AFK events:
    A simplified query example of how to summarize what programs used while not afk.
    The query intersects the not-afk events from the afk bucket with the events from the window bucket, merges keys from the result and sorts by duration.

    .. code-block:: bash

        afk_events = query_bucket(find_bucket("aw-watcher-afk_"));
        window_events = query_bucket(find_bucket("aw-watcher-window_"));
        window_events = filter_period_intersect(window_events, filter_keyvals(afk_events, "status", ["not-afk"]));
        merged_events = merge_events_by_keys(window_events, ["app", "title"]);
        RETURN = sort_by_duration(merged_events);

Example including aw-client:
    This is an example of how you can do analysis and aggregation with the query method in Python with aw-client.
    You probably need to install the client library by following the instructions in its `repository <https://github.com/ActivityWatch/aw-client>`_.

	.. note:: This example runs the client in *testing* mode, which means that it will try to connect to an aw-server in testing mode on the port 5666 instead of the normal 5600.

    .. literalinclude:: query_client.py

Fetching Raw Events
-------------------

**TODO:** Write this section

`Bucket REST API <./rest.html#get-events>`_
