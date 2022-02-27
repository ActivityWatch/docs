.. _getting-started:

***************
Getting started
***************

Getting started with ActivityWatch is as easy as installing, starting it, and setting up autostart (if your installation method doesn't do it for you).

Installation
============

.. tabs::

   .. group-tab:: Windows

      Download and run the Windows installer for the `latest release on GitHub <https://github.com/ActivityWatch/activitywatch/releases>`_.

   .. group-tab:: macOS

      .. note::
         macOS >10.15 (Catalina) introduced some complications for running ActivityWatch (privacy and application permissions). See :issue:`334` for post-install steps needed to allow ActivityWatch to read the current active window / application (without these steps, ActivityWatch may not start and will show window and application names as `unknown`).

      Download the ``.dmg`` for the `latest release from GitHub <https://github.com/ActivityWatch/activitywatch/releases>`_ and drag the ``.app`` to your Applications folder as usual, then add it to your autostart applications.

   .. group-tab:: Linux

      Download the `latest release from GitHub <https://github.com/ActivityWatch/activitywatch/releases>`_, unzip the archive into an appropriate directory, and add the ``aw-qt`` executable to your autostart applications.

      .. note::
         If you are using Arch Linux you can install ActivityWatch directly from `the AUR <https://aur.archlinux.org/packages/activitywatch-bin/>`_.

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

Autostart
=========

.. note::
    Autostart is set up automatically by the Windows installer and for Arch Linux by the AUR package (if your desktop environment supports `XDG Autostart <https://wiki.archlinux.org/index.php/XDG_Autostart>`_).

You probably want to make ActivityWatch start automatically on login using your operating system's autostart settings.
For some installation methods (Windows installer, AUR package) this is done automatically, but if you don't use those methods you'll have to do it yourself. Searching the web for "autostart application <your operating system>" should get you some good results that don't take long. You want to start the ``aw-qt`` executable in the application directory.
