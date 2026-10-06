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

      Download the ``.dmg`` for the `latest release from GitHub <https://github.com/ActivityWatch/activitywatch/releases/latest>`_ and drag the ``.app`` to your Applications folder as usual. See `Autostart`_ for how to start it at login.

      Starting with ``v0.14``, there are separate downloads for Apple Silicon (``arm64``) and Intel (``x86_64``) Macs. Pick the one matching your Mac.

   .. group-tab:: Linux

      The `latest release on GitHub <https://github.com/ActivityWatch/activitywatch/releases/latest>`_ is available in several formats:

      - ``.zip``: unzip the archive into an appropriate directory, and run the ``aw-qt`` executable. See `Autostart`_ for how to start it at login.
      - ``.AppImage``: make the file executable (``chmod +x``) and run it.
      - ``.deb`` (Debian, Ubuntu, and derivatives): install it with your package manager, e.g. ``sudo apt install ./activitywatch-<version>-linux-x86_64.deb``.

      .. note::
         If you are using Arch Linux you can install using the official ``activitywatch-bin`` package in `the AUR <https://aur.archlinux.org/packages/activitywatch-bin/>`_.

   .. group-tab:: Android

      Install it from the `Play Store <https://play.google.com/store/apps/details?id=net.activitywatch.android>`_ or using the APK from the `aw-android releases page <https://github.com/ActivityWatch/aw-android/releases>`_.

      .. note::
         Getting it to F-droid is a work-in-progress, see `this PR <https://gitlab.com/fdroid/fdroiddata/-/merge_requests/5502>`_.


.. note::
   Starting with ``v0.14``, each release also offers an experimental Tauri distribution (files named ``activitywatch-tauri-*``). It replaces the ``aw-qt`` tray app, embeds ``aw-server-rust``, and on Linux bundles `awatcher <https://github.com/2e3s/awatcher>`_ for native Wayland support. The classic distribution remains the default.


Usage
=====

The aw-qt application is the easiest way to use ActivityWatch. It creates a trayicon and automatically starts the server and the default watchers.

If you've installed by extracting a zip archive, simply run the ``./aw-qt`` binary in the installation directory (either from your terminal or on Windows by double-clicking). You now should see an icon appear in your system tray.

You should now also have the web interface running at `<http://localhost:5600>`_ and within a few minutes be able to view your data in the Activity view!

If you want more advanced ways to run ActivityWatch (including running it without aw-qt), check out the "Running" section of `installing-from-source`.

.. note::
   If you are running GNOME 3 or another desktop environment that does not support system trays, or if for some reason Qt can't be used on your machine, read `Running on GNOME`.

.. note::
   If you are using a proxy ActivityWatch might not work out of the box. To fix this you can set the environment variable ``NO_PROXY`` to include ``127.0.0.1`` before starting aw-qt. How to set an environment variable depends on your operating system; use Google if you are unsure how to do this.

Autostart
=========

Both desktop apps, aw-qt and the newer aw-tauri, have a **Start at login** checkbox in their tray menu.
Ticking it registers ActivityWatch with your operating system so it starts when you log in; unticking it removes that registration.
The change takes effect from your next login.

.. note::
   The checkbox was added in v0.14.0. On older versions, add ActivityWatch to your system's startup applications yourself: the Windows installer's "Start ActivityWatch when Windows starts" option, *Login Items* on macOS, or your desktop environment's startup settings on Linux (pointing at the ``aw-qt`` executable).

.. list-table:: What the "Start at login" checkbox creates
   :header-rows: 1

   * -
     - aw-qt
     - aw-tauri
   * - Windows
     - Registry value ``ActivityWatch`` under ``HKCU\Software\Microsoft\Windows\CurrentVersion\Run``
     - Registry value ``aw-tauri`` under the same ``Run`` key
   * - macOS
     - LaunchAgent ``~/Library/LaunchAgents/net.activitywatch.aw-qt.plist``
     - A Login Item for the app (macOS may ask to let ActivityWatch control "System Events")
   * - Linux
     - ``~/.config/autostart/aw-qt.desktop``
     - ``~/.config/autostart/aw-tauri.desktop``
   * - Default
     - Off (except the Research Edition, which turns it on the first time it runs)
     - On

Only enable start-at-login in one of the two apps.
They use the same port (5600), so if both start at login, one of them will fail to start its server (aw-tauri shows a "port already in use" error).

.. note::
   aw-tauri stores the setting as ``enabled`` in the ``[autostart]`` section of its ``config.toml``, and applies it every time it starts.
   If you remove the login entry using your operating system's settings instead of the checkbox, aw-tauri adds it back the next time it starts.
   To turn it off for good, untick the checkbox or set ``enabled = false`` there.

If you run several instances side by side with ``--profile``, each profile gets its own autostart entry, so the checkbox in one does not affect the others.

Existing autostart entries
--------------------------

If you set up autostart before these checkboxes existed, read the section for your system so you don't end up with an entry you can't turn off.
A duplicate entry is harmless on its own: both apps only allow one running instance, so the second copy quits quietly.

.. tabs::

   .. group-tab:: Windows

      The installers have a "Start ActivityWatch when Windows starts" option, ticked by default.
      It puts a shortcut in your Startup folder (open it by typing ``shell:startup`` in the Run dialog, :kbd:`Win+R`).

      - **aw-qt:** the checkbox recognizes the installer's ``ActivityWatch`` shortcut. It shows as ticked, and unticking it deletes the shortcut.
        The installer remembers your choice from the last install, so when you upgrade, untick the option in the installer too, otherwise it recreates the shortcut.
      - **aw-tauri:** the checkbox does not know about the installer's ``ActivityWatch (Tauri)`` shortcut.
        To stop aw-tauri from starting at login, untick the checkbox *and* delete that shortcut from the Startup folder.

   .. group-tab:: macOS

      Earlier versions of these docs said to add ActivityWatch to your Login Items by hand (`Apple's guide <https://support.apple.com/guide/mac-help/open-items-automatically-when-you-log-in-mh15189/mac>`_).

      - **aw-qt:** the checkbox uses a LaunchAgent and does not see a Login Item you added by hand.
        Before ticking the checkbox, remove ActivityWatch from *System Settings → General → Login Items*. If you keep the manual Login Item instead, leave the checkbox unticked.
        macOS lists the LaunchAgent under "Allow in the Background" in the same settings page. If you turn it off there, it won't start, even if the checkbox is ticked.
      - **aw-tauri:** the checkbox manages the Login Item itself and recognizes an existing ``ActivityWatch`` Login Item, so you don't need to do anything.

   .. group-tab:: Linux

      - **Packages (.deb, AUR):** these install a system-wide autostart entry, ``/etc/xdg/autostart/aw-qt.desktop``, so aw-qt starts at login even though the checkbox shows unticked.
        Unticking the checkbox cannot turn that entry off. To disable it, use your desktop environment's startup settings, or override it for your user:

        .. code-block:: sh

           mkdir -p ~/.config/autostart
           sed 's/^Hidden=.*/Hidden=true/' /etc/xdg/autostart/aw-qt.desktop > ~/.config/autostart/aw-qt.desktop

      - **Manual entries:** if you created ``~/.config/autostart/aw-qt.desktop`` yourself (``make install`` in aw-qt does this, and GNOME's "Startup Applications" usually names the entry after the command), that is the same file the aw-qt checkbox manages. An entry with any other name, such as a line in your i3 or sway config, is separate: remove it if you switch to the checkbox.
      - **aw-qt AppImage:** don't use the checkbox. It currently records the temporary path the AppImage is mounted at, which is gone after a reboot. Add the ``.AppImage`` file to your startup applications instead. The aw-tauri AppImage is not affected.

      Window managers and desktop environments that don't support `XDG Autostart <https://wiki.archlinux.org/title/XDG_Autostart>`_ ignore ``~/.config/autostart``.
      There, start ``aw-qt`` (or ``aw-tauri``) from wherever you keep your startup commands, or use `dex <https://github.com/jceb/dex>`_ to run XDG autostart entries.
