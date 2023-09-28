Running on GNOME
================

As an alternative for users of GNOME 3 and other desktop environments that don't support app trays, or simply to avoid depending on Qt, you can place two simple workaround scripts in your ActivityWatch install folder:

:code:`start.sh`:
::

  #!/bin/bash

  cd ~/.local/opt/activitywatch         # Put your ActivityWatch install folder here


  ./aw-watcher-afk/aw-watcher-afk &
  ./aw-watcher-window/aw-watcher-window &                 # you can add --exclude-title here to exclude window title tracking for this session only
  notify-send "ActivityWatch started"   # Optional, sends a notification when ActivityWatch is started
  ./aw-server/aw-server;



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
  Exec="~/.local/opt/activitywatch/start.sh"
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
  Exec="~/.local/opt/activitywatch/kill.sh"
  Hidden=false
  Terminal=false
  Type=Application
  Version=1.0
  Icon=activitywatch
  Categories=Utility;
