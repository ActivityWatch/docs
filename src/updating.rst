Updating
========

Updating ActivityWatch is generally an uncomplicated process.

If you've installed using an installer or package you can simply update by installing the new installer or package.

If you've installed by extracting a folder (Windows/Linux) or ``.app`` bundle (on macOS) then you can simply move or remove the old folder and replace with a new one.

You do not need to worry about your data disappearing, as it's stored in a separate location (see the :doc:`directories`).

Stop ActivityWatch before updating
----------------------------------

Always quit ActivityWatch **before** replacing any files. The bundled ``aw-server`` is a running process that holds the SQLite database open; overwriting its binary or library files while it is running will, on most operating systems, fail silently (or worse, leave you with a half-updated install that crashes on next start).

How to stop it depends on how you started it:

.. tabs::

   .. group-tab:: aw-qt (default)

      Right-click the ActivityWatch tray icon and choose **Quit** (on macOS the tray lives in the menu bar). This stops ``aw-qt`` and the ``aw-server`` it launched.

   .. group-tab:: Linux / systemd --user

      If you started ActivityWatch as a systemd user service, stop it with::

          systemctl --user stop activitywatch.target

      (or whatever unit name you used; ``systemctl --user list-units | grep activitywatch`` will list them).

   .. group-tab:: Linux / manual

      From a terminal::

          pkill -f aw-qt
          pkill -f aw-server

      Both should exit within a second or two; ``pgrep -f aw-server`` returning nothing confirms the server is stopped.

   .. group-tab:: macOS

      Click the ActivityWatch menu bar icon and choose **Quit**. If the menu bar icon is missing (or you started it from a terminal), run::

          killall ActivityWatch
          killall aw-qt

   .. group-tab:: Windows

      Right-click the ActivityWatch tray icon and choose **Quit**. If the tray icon is not visible, open **Task Manager** (``Ctrl+Shift+Esc``), find the ``aw-qt`` and ``aw-server`` processes, and **End task** each of them before replacing the files.

After the update, just start ``aw-qt`` (or your usual autostart entry) again — your existing data and buckets are picked up automatically because they live in the standard user data directory (see :doc:`directories`).

macOS
-----

When updating on macOS, you may need to remove and readd ActivityWatch to your accessibility permissions. If you don't do this, you may end up with empty window titles, or worse.

.. note::
    You need to actually remove the ActivityWatch entry in the list and readd it (rechecking the checkbox isn't enough).
