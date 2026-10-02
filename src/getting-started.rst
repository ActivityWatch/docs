.. _getting-started:

***************
Getting started
***************

Getting started with ActivityWatch is as easy as installing, starting it, and setting up autostart (if your installation method doesn't do it for you).

Installation
============

.. tabs::

   .. group-tab:: Windows

      Download and run the Windows installer for the `latest release on GitHub <https://github.com/ActivityWatch/activitywatch/releases/latest>`_.

   .. group-tab:: macOS

      Download the ``.dmg`` for the `latest release from GitHub <https://github.com/ActivityWatch/activitywatch/releases/latest>`_ and drag the ``.app`` to your Applications folder as usual, then add it to your autostart applications.

   .. group-tab:: Linux

      Download the `latest release from GitHub <https://github.com/ActivityWatch/activitywatch/releases/latest>`_, unzip the archive into an appropriate directory, and add the ``aw-qt`` executable to your autostart applications.

      .. note::
         If you are using Arch Linux you can install using the official ``activitywatch-bin`` package in `the AUR <https://aur.archlinux.org/packages/activitywatch-bin/>`_.

   .. group-tab:: Android

      Install it from the `Play Store <https://play.google.com/store/apps/details?id=net.activitywatch.android>`_ or using the APK from the `aw-android releases page <https://github.com/ActivityWatch/aw-android/releases>`_.

      .. note::
         Getting it to F-droid is a work-in-progress, see `this PR <https://gitlab.com/fdroid/fdroiddata/-/merge_requests/5502>`_.


Usage
=====

The aw-qt application is the easiest way to use ActivityWatch. It creates a trayicon and automatically starts the server and the default watchers.

If you've installed by extracting a zip archive, simply run the ``./aw-qt`` binary in the installation directory (either from your terminal or on Windows by double-clicking). You now should see an icon appear in your system tray.

You should now also have the web interface running at `<localhost:5600>`_ and within a few minutes be able to view your data in the Activity view!

If you want more advanced ways to run ActivityWatch (including running it without aw-qt), check out the "Running" section of `installing-from-source`.

.. note::
   If you are running GNOME 3 or another desktop environment that does not support system trays, or if for some reason Qt can't be used on your machine, read `Running on GNOME`.

.. note::
   If you are using a proxy ActivityWatch might not work out of the box. To fix this you can set the environment variable ``NO_PROXY`` to include ``127.0.0.1`` before starting aw-qt. How to set an environment variable depends on your operating system; use Google if you are unsure how to do this.

Next steps after installing
===========================

Once ActivityWatch is running and you can see your tray icon, there are a few extra things worth doing to get useful data right away.

Install the browser extension
-----------------------------

The default :doc:`watchers` track the active *application* (e.g. ``Firefox``, ``Slack``), but the browser extension — :gh-aw:`aw-watcher-web` — adds the **title and URL of the active tab**. Without it, your browsing history inside the browser shows up as plain ``Firefox`` with no further detail.

The extension is available for the major browsers:

- `Chrome / Edge / Brave <https://chromewebstore.google.com/detail/activitywatch-web-watcher/nglaklfkpbjkhcdbgdkkfkgnjjlfpjcg>`_
- `Firefox <https://addons.mozilla.org/en-US/firefox/addon/aw-watcher-web/>`_

After installing, pin the extension and reload any tabs you have open so it can start logging.

.. note::
   The browser extension only runs while its toolbar icon is enabled. If you don't see events from it, click the extension's icon to confirm it is on (its badge colour tells you whether it is currently logging).

Install an editor watcher
-------------------------

If you spend a meaningful amount of time in a code or text editor, install the matching editor watcher. Without one, every "coding" minute shows up as the editor's binary name only, with no file, project or language breakdown.

See the *Editor watchers* section in :doc:`watchers` for the full list (VS Code, Vim/Neovim, JetBrains, Emacs, Sublime, Zed, Obsidian, …).

Set up categories
-----------------

ActivityWatch records *what* you were doing but doesn't know what to call it. Categories let you map raw app or window titles onto your own labels (e.g. ``github.com → Coding``, ``Slack → Communication``) so the dashboard can roll activity up by purpose.

There are two ways to set them up:

- From the web UI: open ``http://localhost:5600`` → **Settings → Categories** and create a rule.
- From the config file: edit ``categories.yaml`` in your user data directory (see :doc:`directories`); the schema is documented in :doc:`configuration`.

A useful starter set covers the apps you spend most of your day in; you can always refine later.

Where your data lives
----------------------

Everything ActivityWatch has recorded lives in a per-user directory and survives reinstalls and updates. See :doc:`directories` for the exact paths on Windows, macOS and Linux, and where to find the logs if something goes wrong.

.. note::
   To back up your data, copy that directory. To start fresh, stop ActivityWatch, delete the directory, and start ActivityWatch again — all your watchers will begin logging from a clean slate.

Autostart
=========

.. tabs::

   .. group-tab:: Windows

      .. note::
         Autostart is set up automatically by the Windows installer.

   .. group-tab:: macOS
      You can automatically start ActivityWatch when you log in by [adding it to your Login Items](https://support.apple.com/guide/mac-help/open-items-automatically-when-you-log-in-mh15189/mac).

   .. group-tab:: Arch Linux

      .. note::
         Autostart is set up automatically for Arch Linux by the AUR package, if your desktop environment supports `XDG Autostart <https://wiki.archlinux.org/index.php/XDG_Autostart>`_.

         You can set up autostart in other environments by adding [``dex``](https://archlinux.org/packages/extra/any/dex/) (to enable XDG autostart) or simply ``aw-qt`` to whatever place you put your startup applications (i3 config, etc).

   .. group-tab:: Ubuntu

      Go to "Activities" or click the "Show Applications" button, search for "Startup Applications". Click "Add" and enter a name and optionally a comment. For the command, enter the path to the ``aw-qt`` executable in the application directory. For example, ``/home/<your username>/.local/opt/activitywatch/aw-qt``.

   .. group-tab:: Other

      You probably want to make ActivityWatch start automatically on login using your operating system's autostart settings.
      Searching the web for "autostart application <your operating system>" should get you some good results that don't take long. You want to start the ``aw-qt`` executable in the application directory.
