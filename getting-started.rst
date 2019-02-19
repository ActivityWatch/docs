***************
Getting started
***************

.. note::
    We're currently working on improving the installation experience by creating proper installers and packages,
    but for now we offer standalone archives containing everything you need.

Installation
============

.. note::
    The prebuilt packages are known to sometimes have issues on Linux.
    If they don't work for you, please create an issue and consider `installing-from-source`.

1. First, grab the `latest release from GitHub <https://github.com/ActivityWatch/activitywatch/releases>`_ for your operating system.

2. Unzip the archive into an appropriate directory and you're done!

Usage
=====

The aw-qt application is the easiest way to use ActivityWatch. It creates a trayicon and automatically starts the server and the default watchers.

Simply run the :code:`./aw-qt` binary in the installation directory (either from your terminal or on Windows by double-clicking). You now should see an icon appear in your system tray (unless you're running Gnome 3, where there is no system tray).

You should now also have the web interface running at `<localhost:5600>`_ and will in a few minutes be able to view your data under the Activity section!

.. note::
    If you want more advanced ways to run ActivityWatch (including running it without aw-qt), check out the "Running" section of `installing-from-source`.

Autostart
=========

You might want to make :code:`aw-qt` start automatically on login.
We hope to automate this for you in the future but for now you'll have to do it yourself.
Searching the web for "autostart application <your operating system>" should get you some good results that don't take long.

Config
=========

Configuration files for ActivityWatch can be found at the following default locations:

- Unix: :code:`~/.config/activitywatch` or the path defined by the :code:`$XDG_CONFIG_HOME` environment variable.
- Mac OS X: :code:`~/Library/Application\ Support/activitywatch/`
- Windows Vista+: :code:`%LocalAppData%\activitywatch\activitywatch`
- Windows XP: :code:`%USERPROFILE%\Application Data\activitywatch\activitywatch`

Config options for the server, client, and default watchers are listed below:

- aw-server

 - :code:`host` Hostname to start the server on. Currently only :code:`localhost` or :code:`127.0.0.1` are supported.
 - :code:`port` Port number to start the server on.
 - :code:`storage` Type of storage for holding buckets and events. Supported types are :code:`memory`, :code:`mongodb`, or :code:`peewee`.

- aw-client

 - :code:`hostname` Hostname of the server to connect to.
 - :code:`port` Port number of the server to connect to.

- aw-watcher-afk

 - :code:`timeout` Time in seconds with no activity required to become afk.
 - :code:`poll_time` Time in seconds between checks for activity.
 - :code:`update_time` Not yet implemented.

- aw-watcher-window:

 - :code:`poll_time` Time in seconds between window checks.
 - :code:`update_time` Not yet implemented.
