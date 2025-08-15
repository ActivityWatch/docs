Working with ActivityWatch Data
===============================

This guide covers how to retrieve and work with your ActivityWatch data, from simple exports to advanced custom analysis.

Most users will want to start with canonical events, which provide processed, meaningful activity data using the same logic as the web UI.

.. contents:: 
   :local:


Getting Started: Canonical Events
----------------------------------

**Canonical events** are processed activity data that combine raw events from multiple sources (window tracking, AFK detection, etc.) into meaningful activity summaries. This is what the ActivityWatch web UI uses and what most users should start with.

The canonical query automatically handles:

* AFK detection from multiple sources (keyboard/mouse, audio, custom patterns)
* Multi-device activity merging with priority handling  
* Event categorization using your configured rules
* Activity summarization and time calculations

Python Implementation
~~~~~~~~~~~~~~~~~~~~~

The easiest way to get canonical events is using the Python client:

.. code-block:: python

    from aw_client import ActivityWatchClient
    from aw_client.queries import canonicalEvents
    from datetime import datetime, timedelta
    
    # Connect to ActivityWatch (use testing=True for safety during development)
    client = ActivityWatchClient("my-analysis", testing=False)
    
    # Get canonical events for today
    start = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    end = start + timedelta(days=1)
    
    # Get processed activity data (same as web UI)
    events = canonicalEvents(client, start, end)
    
    # events now contains categorized activity data with durations
    for event in events:
        print(f"{event.data['app']}: {event.duration.total_seconds()/3600:.1f} hours")

Reference Implementations
~~~~~~~~~~~~~~~~~~~~~~~~~

For more advanced usage, see the actual canonical query implementations:

* `Python canonical queries <https://github.com/ActivityWatch/aw-client/blob/master/aw_client/queries.py>`_ - Production-ready functions
* `Web UI implementation <https://github.com/ActivityWatch/aw-webui/blob/master/src/queries.ts>`_ - TypeScript version used by the interface
* `Query examples <https://github.com/ActivityWatch/aw-webui/blob/master/test/unit/__snapshots__/queries.test.node.js.snap>`_ - Human-readable query snapshots


Comprehensive Examples
-----------------------

The `aw-client repository <https://github.com/ActivityWatch/aw-client/tree/master/examples>`_ contains comprehensive, safe examples for working with ActivityWatch data:

**Getting Started:**
    * `time_spent_today.py <https://github.com/ActivityWatch/aw-client/blob/master/examples/time_spent_today.py>`_ - Simple canonical events example
    * `load_dataframe.py <https://github.com/ActivityWatch/aw-client/blob/master/examples/load_dataframe.py>`_ - Load data into pandas for analysis

**Advanced Analysis:**
    * `working_hours.py <https://github.com/ActivityWatch/aw-client/blob/master/examples/working_hours.py>`_ - Complex analysis using canonical queries
    * `suggest_categories.py <https://github.com/ActivityWatch/aw-client/blob/master/examples/suggest_categories.py>`_ - AI-powered category suggestions

**Data Management:**
    * `redact_sensitive.py <https://github.com/ActivityWatch/aw-client/blob/master/examples/redact_sensitive.py>`_ - Safely redact sensitive data (dry-run by default)
    * `merge_buckets.py <https://github.com/ActivityWatch/aw-client/blob/master/examples/merge_buckets.py>`_ - Combine data from multiple buckets

.. note::
    These examples follow best practices including safety checks, dry-run modes, and comprehensive error handling.


Custom Queries
--------------

For specialized analysis beyond canonical events, you can write custom queries using ActivityWatch's query language.

Query Language Basics
~~~~~~~~~~~~~~~~~~~~~~

Queries use a simple scripting language for server-side data processing:

.. code-block:: javascript

    // Get events from a bucket
    events = query_bucket("aw-watcher-window_hostname");
    
    // Filter to only active periods  
    afk_events = query_bucket("aw-watcher-afk_hostname");
    not_afk = filter_keyvals(afk_events, "status", ["not-afk"]);
    events = filter_period_intersect(events, not_afk);
    
    // Group by application
    events = merge_events_by_keys(events, ["app"]);
    
    // Sort by time spent
    RETURN = sort_by_duration(events);

Key Transform Functions
~~~~~~~~~~~~~~~~~~~~~~~

Common query functions include:

* ``query_bucket(bucket_id)`` - Get events from a bucket
* ``filter_keyvals(events, key, values)`` - Filter events by data values
* ``filter_period_intersect(events1, events2)`` - Only keep overlapping time periods
* ``merge_events_by_keys(events, keys)`` - Group events by specified keys
* ``categorize(events, categories)`` - Apply category rules
* ``sort_by_duration(events)`` - Sort by time spent

Magic Variables
~~~~~~~~~~~~~~~

The web UI provides special variables you can use:

* ``__CATEGORIES__`` - Your configured categorization rules
* ``find_bucket(pattern)`` - Find bucket names matching a pattern

Example using categories to filter work activities:

.. code-block:: javascript

    events = flood(query_bucket(find_bucket("aw-watcher-window_")));
    not_afk = flood(query_bucket(find_bucket("aw-watcher-afk_")));
    not_afk = filter_keyvals(not_afk, "status", ["not-afk"]);
    events = filter_period_intersect(events, not_afk);
    events = categorize(events, __CATEGORIES__);
    events = filter_keyvals(events, "$category", [["Work"]]);
    RETURN = sort_by_duration(events);

Query Examples
~~~~~~~~~~~~~~

**Minimal example** - Get events from a bucket:

.. code-block:: javascript

    events = query_bucket("my_bucket");
    RETURN = events;

**Hierarchy example** - Create app→title hierarchy:

.. code-block:: javascript

    events = query_bucket("my_bucket");
    events = merge_events_by_keys(events, ["app", "title"]);
    RETURN = events;

**Practical Python example** - The `query_client.py <query_client.py>`_ file demonstrates:

* Creating test buckets and data
* Writing queries with transformations  
* Using merge_events_by_keys for grouping
* Time period filtering
* Safe cleanup with testing mode

Complete Example
~~~~~~~~~~~~~~~~

Here's a complete custom query for analyzing productivity:

.. code-block:: javascript

    // Get window and AFK events
    events = flood(query_bucket(find_bucket("aw-watcher-window_")));
    not_afk = flood(query_bucket(find_bucket("aw-watcher-afk_")));
    not_afk = filter_keyvals(not_afk, "status", ["not-afk"]);
    
    // Only count active time
    events = filter_period_intersect(events, not_afk);
    
    // Apply categories
    events = categorize(events, __CATEGORIES__);
    
    // Filter to work categories only
    events = filter_keyvals(events, "$category", [["Work"]]);
    
    // Group by application and sort
    events = merge_events_by_keys(events, ["app"]);
    RETURN = sort_by_duration(events);

For more transform functions, see the API reference for :py:mod:`aw_transform` and :py:mod:`aw_query`.


Raw Events (Advanced)
----------------------

For maximum flexibility, you can work directly with raw events from buckets. This is useful for:

* Custom analysis requiring full event details
* Building your own processing pipeline  
* Using the aw-analysis library directly

.. warning::
    Working with raw events requires more care:
    
    * Always test with ``testing=True`` first
    * Back up your data before any modifications
    * Use dry-run modes for destructive operations
    * Raw events don't include AFK filtering or categorization

Basic Raw Event Access
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from aw_client import ActivityWatchClient
    
    client = ActivityWatchClient("my-app", testing=True)  # Safe mode
    
    # Get buckets
    buckets = client.get_buckets()
    print("Available buckets:", list(buckets.keys()))
    
    # Get raw events from a bucket
    bucket_id = "aw-watcher-window_" + client.client_hostname
    events = client.get_events(bucket_id, limit=100)
    
    # Process events manually
    for event in events:
        print(f"Time: {event.timestamp}, Duration: {event.duration}")
        print(f"Data: {event.data}")


Exporting Data
--------------

For simple data export, see :doc:`../features/exporting-data` which covers:

* Exporting complete buckets to JSON
* Using the web UI export feature
* Backup and restore procedures

The web UI's export feature uses canonical events by default, providing clean, processed data suitable for external analysis.


API Reference
-------------

For low-level API access, see:

* :doc:`../api/rest` - HTTP REST API documentation
* :doc:`../api/python` - Python client library API