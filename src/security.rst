Security
========

ActivityWatch deals with highly sensitive data, and the security of it is therefore of paramount importance. Unfortunately, we don't have a lot of resources, so things like security audits are currently out of reach for us.

We do try our best to keep security in mind. In this section of the documentation we'll outline some important security considerations, including risks and possible improvements.

.. contents::

ActivityWatch is only as secure as your system
----------------------------------------------

Some things we can't protect against. Examples are malware running on the same host and anything that can access the database file.

As an example, ActivityWatch is not secure on systems with multiple users, since the API is unauthenticated by default (see `API authentication`_ below).


API authentication
------------------

By default, the ActivityWatch API requires no authentication: any process that can reach the server (normally only processes on the same machine, since it listens on ``localhost``) can read, write, and delete all data.

``aw-server-rust`` supports **opt-in** API key authentication. To enable it, set an API key under the ``[auth]`` section of the server's ``config.toml`` (see `directories <config-directory>` for its location) and restart the server:

.. code-block:: toml

    [auth]
    api_key = "your-secret-key-here"

When an API key is set, every request to ``/api/*`` (except ``GET /api/0/info``) must include the header ``Authorization: Bearer <api_key>``, otherwise the server responds with ``401 Unauthorized``. An empty ``api_key`` leaves authentication disabled.

Things to keep in mind:

- Authentication is disabled by default on desktop, so existing setups keep working unchanged.
- It is only supported by ``aw-server-rust``. ``aw-server`` (Python) does not support it.
- Every client must send the key. ``aw-sync`` reads it from the server config automatically, and ``aw-client-rust`` accepts one via ``AwClient::new_with_api_key``, but other clients and watchers may not support it yet and will fail with ``401`` once it's enabled.
- The key protects the API, not the data at rest: anything that can read the config file or the database file can still access your data.
- Authentication does not make it safe to expose the server on a network. The API is served over plain HTTP, so see `remote-server` before doing so.


Deleting sensitive data
-----------------------

Some data may wish to be deleted/filtered/redacted, or simply never logged at all. Making this easy should be one of the most basic privacy features we can add.

This is actually :issue:`1` in the ActivityWatch repository. See `filtering data` for details.


Encrypting data
---------------

Encrypting old data with a password would minimize the amount of sensitive data that would be leaked in case of a breach.

The easiest way to build this would be to write a client that takes all events older than some duration and moves it into a encrypted container. This way it wouldn't add complexity to the server code.


Reproducible builds
-------------------

It's important that our builds are reproducible, such that we can ensure the integrity of a built package.

We currently lack tests for it, so we don't actually know if they are (they should be, at least some of them).


CORS configuration
------------------

CORS is configured such that origins can only be ``localhost:5600`` or match the ActivityWatch WebExtension URL for Chrome, or **any extension** on Firefox.

This is due to that on Chrome, the origin of a WebExtension is always a fixed URL. In Firefox however the URL changes for each install, in order to prevent fingerprinting which extensions are installed. It's mentioned here: :gh-aw:`aw-server-rust/issues/24#issuecomment-520802579`.

This means that on Firefox, a malware WebExtension could easily fetch the entire datastore and do what it wants with it.

Ways to solve this:

 - Short term: Restrict what we let those origins do (i.e. only send heartbeats, maybe even only to a certain bucket)

 - Long term: Use an OAuth2 authentication flow when first installing the extension (this also adds many opportunities for integrations)

More?
-----

This is an early version of this document. There might be more things mentioned in issues (search for "security").

