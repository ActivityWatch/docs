API Reference
=============

Here's an API reference for some of the most central components in :code:`aw_core`, :code:`aw_client` and :code:`aw_server`.
These are the most important packages in ActivityWatch.
A lot of it currently lacks proper docstrings, but it's a start.

.. contents::



aw_core
-------
.. automodule:: aw_core
   :members:
   :undoc-members:

aw_core.models
^^^^^^^^^^^^^^
.. automodule:: aw_core.models
   :members: Event
   :undoc-members:

aw_core.log
^^^^^^^^^^^
.. automodule:: aw_core.log
   :members:
   :undoc-members:

aw_core.dirs
^^^^^^^^^^^^
.. automodule:: aw_core.dirs
   :members:
   :undoc-members:


aw_client
---------

The aw_client package contains a programmer-friendly wrapper around the servers REST API.

.. automodule:: aw_client
   :members: ActivityWatchClient
   :undoc-members:

aw_transform
------------

The aw_transform package contains transforms used in the query language.

.. note:: Their function signatures and return types may deviate from how the transforms are actually implemented in the query language. For more details, see `aw_query.functions`

.. automodule:: aw_transform
   :members:
   :undoc-members:

aw_query
-----------

The `aw_query` package contains the interpreter for the query language and registers the standard functions, usually based on Python implementations of them available in `aw_transform`.

.. automodule:: aw_query
   :members:
   :undoc-members:

.. automodule:: aw_query.functions
   :members:
   :exclude-members: q2_function, q2_typecheck, TQueryFunction
   :undoc-members:


aw_server
---------

.. automodule:: aw_server
   :members:
   :undoc-members:

aw_server.api
^^^^^^^^^^^^^

The :code:`ServerAPI` class contains the basic API methods, these methods are primarily called from RPC layers such as the one found in :code:`aw_server.rest`.

.. automodule:: aw_server.api
   :members: ServerAPI
   :undoc-members:

