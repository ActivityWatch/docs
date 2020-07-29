Security
========

ActivityWatch deals with highly sensitive data, and the security of it is therefore of paramount importance.

Unfortunately, we don't have a lot of resources, so things like security audits are currently out of reach for us.

We do try our best to keep security in mind. In this section of the documentation we'll outline some important security considerations, including risks and possible improvements.


ActivityWatch is only as secure as your system
----------------------------------------------

Some things we can't protect against. Examples are malware running on the same host and anything that can access the database file.


Deleting sensitive data
-----------------------

Some data may wish to be deleted/filtered/redacted, or simply never logged at all. Making this easy should be one of the most basic privacy features we can add.

This is actually issue #1 in the ActivityWatch repository: https://github.com/ActivityWatch/activitywatch/issues/1


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

This is due to that on Chrome, the origin of a WebExtension is always a fixed URL. In Firefox however the URL changes for each install, in order to prevent fingerprinting which extensions are installed. It's mentioned here: https://github.com/ActivityWatch/aw-server-rust/issues/24#issuecomment-520802579

This means that on Firefox, a malware WebExtension could easily fetch the entire datastore and do what it wants with it.

Ways to solve this:

 - Short term: Restrict what we let those origins do (i.e. only send heartbeats, maybe even only to a certain bucket)

 - Long term: Use an OAuth2 authentication flow when first installing the extension (this also adds many opportunities for integrations)

More?
-----

This is an early version of this document. There might be more things mentioned in issues (search for "security").

