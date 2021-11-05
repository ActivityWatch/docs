Server comparison
=================

The are two server implementations: 

- aw-server-python (the current default)
- aw-server-rust (the future default)

These two are almost at feature parity. Here we've documented some differences:

- aw-server-rust does not serve the API browser (provided by Swagger/OpenAPI) at ``/api/``

Transforms
----------

.. note:: Transforms might have implementation differences across server implementations, which may impact analysis results.

The transforms used by aw-server-python are shipped as part of the ``aw-core`` package.

============= ================ ==============  
Function      aw-server-python aw-server-rust  
============= ================ ==============
period_union  Yes              Yes
============= ================ ==============
