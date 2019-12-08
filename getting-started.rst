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

Simply **run the :code:`./aw-qt` binary in the installation directory** (either from your terminal or on Windows by double-clicking). You now should see an icon appear in your system tray.

.. note::
   If you are running GNOME 3 or another desktop that does not support system trays, or if for some reason Qt can't be used on your machine, have a look at the *Installing from GNOME* section below.



You should now also have the web interface running at `<localhost:5600>`_ and will in a few minutes be able to view your data under the Activity section!

.. note::
    If you want more advanced ways to run ActivityWatch (including running it without aw-qt), check out the "Running" section of `installing-from-source`.

.. note::
   If you are using a proxy, activitywatch will not work by default. To circumvent this you can set the environment variable HTTP_PROXY before starting aw-qt. How to set an environment variable depends on your operating system, use Google if you are unsure how to do this.

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
- Windows: :code:`%LocalAppData%\activitywatch\activitywatch`

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
 - :code:`exclude_title` Don't track window titles
 - :code:`update_time` Not yet implemented.

Installing on GNOME
===================

As an alternative for users of GNOME 3 and other DEs that don't support app trays, or simply to avoid depending on Qt, you can place two simple workaround scripts in your ActivityWatch install folder:

:code:`start.sh`:
::

  #!/bin/bash

  cd ~/.local/opt/activitywatch         # Put your ActivityWatch install folder here

  ./aw-server/aw-server &
  ./aw-watcher-afk/aw-watcher-afk &
  ./aw-watcher-window/aw-watcher-window &                 # you can add --exclude-title here to exclude window title tracking for this session only

  notify-send "ActivityWatch started"   # Optional, sends a notification when ActivityWatch is started


:code:`kill.sh`:
::

  #!/bin/bash
  pkill aw-
  notify-send "ActivityWatch killed"    # Optional, sends a notification when ActivityWatch is killed


Don't forget to :code:`chmod +x start.sh` and :code:`chmod +x kill.sh`.

Then you can create two desktop files for these scripts to show up among your apps:

:code:`~/.local/share/applications/aw-start.desktop`:
::

  [Desktop Entry]
  Name=Start ActivityWatch
  Comment=Start AW
  Exec=~/.local/opt/activitywatch/start.sh
  Hidden=false
  Terminal=false
  Type=Application
  Version=1.0
  Icon=activitywatch
  Categories=Utility;


:code:`~/.local/share/applications/aw-kill.desktop`:
::

  [Desktop Entry]
  Name=Kill ActivityWatch
  Comment=Kill AW
  Exec=~/.local/opt/activitywatch/kill.sh
  Hidden=false
  Terminal=false
  Type=Application
  Version=1.0
  Icon=activitywatch
  Categories=Utility;
