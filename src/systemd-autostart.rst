.. _systemd-autostart:

***********************************
Autostart on Linux with systemd
***********************************

Linux systems that use systemd can run ActivityWatch as user services. This
avoids the tray application, keeps logs in the user journal, and restarts a
component if it fails. Do not run these services and ``aw-qt`` at the same
time: disable the existing ActivityWatch desktop autostart entry first.

The examples assume that the extracted ActivityWatch directory is at
``~/.local/opt/activitywatch``. Adjust the ``ExecStart`` paths if you installed
it elsewhere. Create the unit directory with::

   mkdir -p ~/.config/systemd/user

X11: server and default watchers
================================

The default AFK and window watchers support X11. Create
``~/.config/systemd/user/activitywatch-server.service``:

.. code-block:: ini

   [Unit]
   Description=ActivityWatch server
   Documentation=https://docs.activitywatch.net/
   After=graphical-session.target
   PartOf=graphical-session.target

   [Service]
   Type=notify
   ExecStart=%h/.local/opt/activitywatch/aw-server-rust/aw-server-rust
   Restart=on-failure
   RestartSec=5

   [Install]
   WantedBy=graphical-session.target

Create ``~/.config/systemd/user/activitywatch-afk.service``:

.. code-block:: ini

   [Unit]
   Description=ActivityWatch AFK watcher
   Documentation=https://docs.activitywatch.net/
   Requires=activitywatch-server.service
   After=graphical-session.target activitywatch-server.service
   PartOf=graphical-session.target

   [Service]
   Type=simple
   ExecStart=%h/.local/opt/activitywatch/aw-watcher-afk/aw-watcher-afk
   Restart=on-failure
   RestartSec=5
   KillSignal=SIGINT

   [Install]
   WantedBy=graphical-session.target

Create ``~/.config/systemd/user/activitywatch-window.service``:

.. code-block:: ini

   [Unit]
   Description=ActivityWatch X11 window watcher
   Documentation=https://docs.activitywatch.net/
   Requires=activitywatch-server.service
   After=graphical-session.target activitywatch-server.service
   PartOf=graphical-session.target

   [Service]
   Type=simple
   ExecStart=%h/.local/opt/activitywatch/aw-watcher-window/aw-watcher-window
   Restart=on-failure
   RestartSec=5
   KillSignal=SIGINT

   [Install]
   WantedBy=graphical-session.target

Then validate and start the units::

   systemd-analyze --user verify ~/.config/systemd/user/activitywatch-*.service
   systemctl --user daemon-reload
   systemctl --user enable --now activitywatch-server.service activitywatch-afk.service activitywatch-window.service

GNOME/Wayland: awatcher bundle
================================

The default Linux watchers require X11. On GNOME/Wayland, install the
`Focused Window D-Bus extension <https://extensions.gnome.org/extension/5592/focused-window-d-bus/>`_
and the bundled `awatcher <https://github.com/2e3s/awatcher/releases>`_ package.
The bundle supplies its own Rust server and replaces both default watchers, so
do not start the three X11 services above.

The current bundle installs the executable as ``awatcher``. Older releases may
call it ``awatcher-bundle``; check with ``command -v awatcher || command -v
awatcher-bundle`` and adjust ``ExecStart`` if needed.

Create ``~/.config/systemd/user/activitywatch-wayland.service``:

.. code-block:: ini

   [Unit]
   Description=ActivityWatch for GNOME/Wayland (awatcher bundle)
   Documentation=https://docs.activitywatch.net/
   After=graphical-session.target
   PartOf=graphical-session.target
   StartLimitIntervalSec=300
   StartLimitBurst=5

   [Service]
   Type=simple
   # Wait up to 30 seconds for the GNOME extension's D-Bus interface.
   # This is reliable across machines; a fixed sleep is not.
   ExecStartPre=/bin/sh -c 'i=0; while [ $$i -lt 30 ]; do /usr/bin/busctl --user introspect org.gnome.Shell /org/gnome/shell/extensions/FocusedWindow org.gnome.shell.extensions.FocusedWindow >/dev/null 2>&1 && exit 0; i=$$((i + 1)); sleep 1; done; exit 1'
   ExecStart=/usr/bin/awatcher -vv --no-tray
   Restart=on-failure
   RestartSec=10

   [Install]
   WantedBy=graphical-session.target

Do not hardcode ``DISPLAY`` or ``WAYLAND_DISPLAY=wayland-0``: display names
vary, and a graphical session should import the correct values into the user
manager. Check them with::

   systemctl --user show-environment | grep -E '^(DISPLAY|WAYLAND_DISPLAY|XAUTHORITY)='

If the values are missing, import the current session before starting the
service::

   dbus-update-activation-environment --systemd DISPLAY WAYLAND_DISPLAY XAUTHORITY

Then validate and start the service::

   systemd-analyze --user verify ~/.config/systemd/user/activitywatch-wayland.service
   systemctl --user daemon-reload
   systemctl --user enable --now activitywatch-wayland.service

Verify and troubleshoot
========================

The server should answer on ``127.0.0.1:5600``::

   curl --fail http://127.0.0.1:5600/api/0/info

Inspect status and logs with::

   systemctl --user status 'activitywatch-*'
   journalctl --user -u 'activitywatch-*' --boot

After changing a unit, run ``systemctl --user daemon-reload`` and restart it.
To test the X11 services without touching your normal database or server, add
``--testing --port 5660`` to their ``ExecStart`` commands temporarily.
Stop and disable a setup with::

   systemctl --user disable --now activitywatch-server.service activitywatch-afk.service activitywatch-window.service
   systemctl --user disable --now activitywatch-wayland.service
