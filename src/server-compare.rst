Server comparison
=================

There are two server implementations:

- **aw-server** (Python): the default server in the classic app (aw-qt).
- **aw-server-rust**: the server in the new Tauri app (aw-tauri), also bundled with the classic app. It is the future default.

They serve the same REST API and the same web UI, store data in their own databases, and as of v0.14.0 they return the same query results for the same data, with the known exceptions listed below.

Same data, same results
-----------------------

Since v0.14.0, a **query parity test suite** (``scripts/tests/query_parity/`` in the `activitywatch repo <https://github.com/ActivityWatch/activitywatch>`_) runs on every change. It starts both servers with empty databases, inserts identical events, runs the same queries on both and fails if the results differ. It covers:

- every query transform on its own (``flood``, ``union_no_overlap``, ``filter_period_intersect``, ``merge_events_by_keys``, ``categorize``, and so on)
- the real queries the web UI and aw-client run: the desktop, browser and Android canonical queries and the multi-device query
- hand-written edge cases (overlapping, contained, adjacent and zero-duration events, equal timestamps, unsorted input, DST offsets, fractional seconds, period clipping) and seeded random event sets for two desktops and a phone

It also checks invariants on each server's own output, such as sorted results, no overlaps after ``union_no_overlap`` and ``flood``, and conserved durations. Writing the suite found and fixed a series of real differences in both servers, for example in ``flood``, ``union_no_overlap``, ``filter_period_intersect``, duration rounding, event ordering and query parsing.

Known differences
~~~~~~~~~~~~~~~~~

The remaining differences are tracked as known failures in the suite, each with its measured cause:

- **Timestamp precision.** aw-server stores timestamps at millisecond resolution, aw-server-rust at nanosecond resolution. This is by design and only affects sub-millisecond values.
- **Output shape of a few transforms.** ``merge_events_by_keys``, ``split_url_events`` and ``tag`` return differently shaped event data. For example, aw-server drops non-key fields from merged events, so web UI lists that color rows by category (such as top window titles) show default colors on aw-server. Durations and totals are not affected. aw-server is being changed to match aw-server-rust (`aw-core#173 <https://github.com/ActivityWatch/aw-core/pull/173>`_, `activitywatch#1466 <https://github.com/ActivityWatch/activitywatch/issues/1466>`_).
- ``chunk_events_by_key`` is deprecated in both servers.

If you find another difference, please `report it <https://github.com/ActivityWatch/activitywatch/issues>`_.

Feature comparison
------------------

.. list-table::
   :header-rows: 1

   * - Feature
     - aw-server (Python)
     - aw-server-rust
   * - REST API, web UI, queries, settings, import/export
     - ✅
     - ✅
   * - Query result cache for finished days
     - ✅
     - ✅
   * - Bucket CSV export
     - ✅
     - ✅
   * - Custom CORS origins (``cors_origins``, ``cors_regex``)
     - ✅
     - ✅
   * - Named profiles (``--profile``)
     - ✅
     - ✅
   * - Sync (:doc:`syncing`), via aw-sync
     - ✅
     - ✅ (recommended for large amounts of synced data)
   * - Optional API key authentication
     - ❌
     - ✅
   * - Database encryption (SQLCipher, opt-in build feature, not in release builds)
     - ❌
     - ✅
   * - Android
     - ❌
     - ✅
   * - Interactive API browser at ``/api/``
     - ✅
     - ❌

Performance
-----------

Both servers are fast enough for everyday use. On large, multi-year databases aw-server-rust is generally faster on first loads, and both make repeat loads near instant with the query cache. Measured on a real 9-year database (9.2 million events, 1.8 GB) with the web UI's Year view (365 daily queries) in v0.14.0:

.. list-table::
   :header-rows: 1

   * - Server
     - First load
     - Repeat load
   * - aw-server
     - 41 s
     - 0.6 s
   * - aw-server-rust
     - 32 s
     - 0.2 s

aw-server-rust doesn't yet cache All-time views on databases this large (`aw-server-rust#784 <https://github.com/ActivityWatch/aw-server-rust/issues/784>`_).

Switching servers
-----------------

See :doc:`migrating` for how to switch from aw-server to aw-server-rust.
