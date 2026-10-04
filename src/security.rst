Security
========

ActivityWatch deals with highly sensitive data, and the security of it is therefore of paramount importance. Unfortunately, we don't have a lot of resources, so things like security audits are currently out of reach for us.

We do try our best to keep security in mind. In this section of the documentation we'll outline some important security considerations, including risks and possible improvements.

.. contents::

ActivityWatch is only as secure as your system
----------------------------------------------

Some things we can't protect against. Examples are malware running on the same host and anything that can access the database file.

As an example, ActivityWatch is not secure on systems with multiple users (due to there being no API authentication).


Deleting sensitive data
-----------------------

Some data may wish to be deleted/filtered/redacted, or simply never logged at all. Making this easy should be one of the most basic privacy features we can add.

This is actually :issue:`1` in the ActivityWatch repository. See `filtering data` for details.


Encrypting data
---------------

Encrypting data at rest minimizes the amount of sensitive data that would be leaked if the database file is copied or stolen.

``aw-server-rust`` has opt-in support for encrypting its database with `SQLCipher <https://www.zetetic.net/sqlcipher/>`_. It is not included in release builds: you need to build ``aw-server-rust`` yourself with the ``encryption`` (or ``encryption-vendored``) Cargo feature, then provide the key with the ``AW_DB_PASSWORD`` environment variable or the ``--db-password`` flag. Prefer the environment variable, since command-line arguments may be visible in process listings.

Encryption at rest does not protect against anything that can access the running server's API.


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

