Server comparison
=================

The are two server implementations: 

- aw-server-python (the current default)
- aw-server-rust (the future default)

These two are almost at feature parity. Here we've documented some differences:

- aw-server-rust does not serve the API browser (provided by Swagger/OpenAPI) at ``/api/``

Transforms might have implementation differences across server implementations, which may impact analysis results. 
We are working to minimize these differences, and encourage you to report any issues you find.
