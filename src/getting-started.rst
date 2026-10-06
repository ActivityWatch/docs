.. _getting-started:

***************
Getting started
***************

Getting started with ActivityWatch is as easy as installing, starting it, and setting up autostart (if your installation method doesn't do it for you).

System requirements
===================

The release builds are produced and tested on the following platforms. Older systems may work, but are not tested.

- **Windows**: Windows 10 or later (x64; ARM64 builds are available for Windows 11).
- **macOS**: macOS 12 (Monterey) or later. Releases are built with a deployment target of 12.0, so older versions fail at launch with errors such as ``dyld: Library not loaded: libswift_Concurrency.dylib``.
- **Linux**: a distribution with glibc 2.35 or newer (the release is built on Ubuntu 22.04, so e.g. Ubuntu 22.04+, Debian 12+, Fedora 36+). Older distributions fail with ``GLIBC_2.xx not found`` errors; use a newer distribution or `build from source <installing-from-source>`_.
- **Android**: see the `Play Store listing <https://play.google.com/store/apps/details?id=net.activitywatch.android>`_ for the supported Android versions.

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

      Install it from the `Play Store <https://play.google.com/store/apps/details?id=net.activitywatch.android>`_, `F-Droid <https://f-droid.org/packages/net.activitywatch.android/>`_, or using the APK from the `aw-android releases page <https://github.com/ActivityWatch/aw-android/releases>`_.


.. note::
   Starting with ``v0.14``, each release also offers an experimental Tauri distribution (files named ``activitywatch-tauri-*``). It replaces the ``aw-qt`` tray app, embeds ``aw-server-rust``, and on Linux bundles `awatcher <https://github.com/2e3s/awatcher>`_ for native Wayland support. The classic distribution remains the default.


Usage
=====

The aw-qt application is the easiest way to use ActivityWatch. It creates a trayicon and automatically starts the server and the default watchers.

If you've installed by extracting a zip archive, simply run the ``./aw-qt`` binary in the installation directory (either from your terminal or on Windows by double-clicking). You now should see an icon appear in your system tray.

You should now also have the web interface running at `<http://localhost:5600>`_ and within a few minutes be able to view your data in the Activity view!

If you want more advanced ways to run ActivityWatch (including running it without aw-qt), check out the "Running" section of `installing-from-source`.

.. note::
   If you are running GNOME or another desktop environment that does not show system tray icons, install the `AppIndicator and KStatusNotifierItem Support <https://extensions.gnome.org/extension/615/appindicator-support/>`_ extension to get the tray icon back. If that is not an option, or if for some reason Qt can't be used on your machine, read `Running on GNOME`.

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
