Examples
========

This section provides practical examples for working with ActivityWatch, from retrieving your data to extending functionality with custom watchers.

Getting Your Data Out
----------------------

**Most users should start here:**

.. toctree::
    :maxdepth: 1

    examples/working-with-data

This comprehensive guide covers:

* **Canonical Events** - Get processed activity data (what the web UI uses)
* **Custom Queries** - Write your own analysis using the query language
* **Raw Events** - Advanced direct access to bucket data
* **Safety Best Practices** - Avoiding data corruption with proper testing and dry-run modes

The guide includes links to production-ready examples from the `aw-client repository <https://github.com/ActivityWatch/aw-client/tree/master/examples>`_.

Writing Your Own Watchers
-------------------------

Want to collect custom data? **See:**

.. toctree::
    :maxdepth: 1

    examples/writing-watchers

These guides cover:

* **Minimal watcher example** - Get started with a simple template
* **Full-featured watcher** - Complete example with heartbeats and proper structure
* **Best practices** - Error handling, bucket management, and testing modes
* **Rust examples** - Alternative implementation for performance-critical watchers

Watchers are small programs that collect data and send it to ActivityWatch. You can track anything with a timestamp!

Example Code Repository
-----------------------

The `aw-client examples <https://github.com/ActivityWatch/aw-client/tree/master/examples>`_ contain comprehensive, well-documented examples including:

* **Time analysis** - ``time_spent_today.py``, ``working_hours.py``
* **Data export** - ``load_dataframe.py`` for pandas integration
* **Data management** - ``redact_sensitive.py`` with safe dry-run mode
* **Advanced analysis** - ``suggest_categories.py`` with AI categorization

All examples follow safety best practices with testing modes and error handling.
