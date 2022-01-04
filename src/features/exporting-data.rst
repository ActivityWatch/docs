Exporting data
==============

If you go to the "Raw Data" page in the ActivityWatch webui you can download any of the buckets which contain every collected datapoint in ActivityWatch as a single file.
If running on localhost with the default port, then you can find this at http://localhost:5600/#/buckets.
Each bucket can be exported individually, or all of the buckets can be exported by clicking the "Export all buckets as JSON" button at the bottom.

To export programatically, you can make a simple GET request via the REST API.
If for example, you want to export all of the buckets with ``wget`` you could call

.. code-block:: sh

   wget http://localhost:5600/api/0/export -O path/to/export.json

Alternatively you can export an individual bucket via the REST API.
For example, if you wanted to export a bucket with ID ``bucket-name-HOSTNAME`` you could call

.. code-block:: sh

   wget http://localhost:5600/api/0/buckets/bucket-name-HOSTNAME/export  -O path/to/export.json
