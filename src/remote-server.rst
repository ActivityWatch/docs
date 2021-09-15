Remote server
=============

Some users ask us if they can run the ActivityWatch server on a separate machine and have other machines report to it, resulting in data from multiple devices on a single ActivityWatch instance. 

While this is technically possible, it is **not supported** and **strongly discouraged**.

There are two common reasons why users wish to do this:

- You are a single user with multiple devices, and they want all their data in one place, and don't have the patience to wait for syncing to be implemented (:issue:`35`).

  - We sympathize with these users, but we don't think that reporting to a central server is a good approach.

- You have employees or team members you wish to monitor.

  - We strongly wish that people **don't use a remote ActivityWatch server** for this purpose (for security & privacy reasons), and as such will not help or otherwise support people doing so.
  - There are other ways to solve the same problem in a privacy-preserving manner, as you can read about in :issue:`233`.

There are several reasons why we won't support and strongly discourage this:

- It is **not secure**.

  - There is no API security, so exposing the server on the network will let *anyone* on the network read, write, or delete **all data**.
  - There is no HTTPS support, so all data would be sent unencrypted.

- We want ActivityWatch to be **user-first**: something people use of their own will, not something forced on them by others (bosses, colleagues).

- It is not what we designed it for, future updates is likely to break whatever setup you have in unexpected ways.

- We're not interested in volunteering our time to support for-profit companies.


But then how do I get all my data in one place?
-----------------------------------------------

Your options are:

- Manually export & import buckets (recommended)
- Wait for syncing to get implemented
- Find other time tracking software that's more suitable for your usecase
- Keep reading...


I know what I'm doing, how can I set it up anyway?
--------------------------------------------------

.. note:: This is intentionally incomplete documentation, you're expected to figure the rest out yourself (and if you can't, you probably shouldn't try).

If you against these warnings decide to run a remote server that watchers report to, there is **only one** somewhat secure way of doing it: Use an SSH tunnel.

The benefits of using an SSH tunnel is that you don't need to expose aw-server directly to the network, and you don't need to change any of the default watcher configuration (although you do need to disable autostarting aw-server in aw-qt, if you use it).

You can set up an SSH tunnel to the remote machine running SSH and aw-server with: :code:`ssh -L 127.0.0.1:5600:localhost:5600 <remote server IP>`

Known issues:

- Not possible with ActivityWatch for Android, as it does not use the REST API to report events.
- You can't have web watchers from multiple machines stored on the same server (non-unique bucket IDs, no hostname/device ID set)


Previous discussions
--------------------

Links to discussions on the topic:

- https://forum.activitywatch.net/t/activitywatch-as-employee-monitoring-software/499/2
- https://forum.activitywatch.net/t/oauth2-or-pretty-much-any-authentication/75/6
- There is more written about this in issues, on the forum, and on the Discord server. Use the search, Luke.
