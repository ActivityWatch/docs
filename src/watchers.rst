Watchers
========

Watchers are the parts of ActivityWatch that do all the data collecting.

ActivityWatch comes bundled with two watchers by default:

- :gh-aw:`aw-watcher-afk` - Watches for mouse & keyboard activity to detect if the user is active (by default, an inactive period of at least 3 minutes is flagged as AFK: away from keyboard).
- :gh-aw:`aw-watcher-window` - Watches the active window, its title, and it's url (on Chrome-based browsers & Safari).

The default watchers are collecting some of the most important data.
But there is more to collect, so here are some other watchers that let you do so.

Browser watchers
----------------

Watches properties of the active tab like title, URL, and incognito state.

- :gh-aw:`aw-watcher-web` - The official browser extension, supports Chrome, Edge, and Firefox.

Editor watchers
---------------

Watches the actively edited file and associated metadata like path, language, and project name (folder name of git root)

- :gh-aw:`aw-watcher-vim` - vim extension, by :gh-user:`johan-bjareholt` and :gh-user:`ahnlabb`.
- :gh-aw:`aw-watcher-vscode` - Visual Studio Code extension, by :gh-user:`Otto-AA`.
- :gh:`pauldub/activity-watch-mode` - emacs mode forked from wakatime-mode, by :gh-user:`pauldub`.
- :gh:`OlivierMary/aw-watcher-jetbrains` - For all JetBrains editors IDEA/Goland/Android Studio/PyCharm/WebStorm/DataGrip/RubyMine/... `See compatibility/Download <https://plugins.jetbrains.com/plugin/11361-activity-watcher>`_, by :gh-user:`OlivierMary`.
- :gh:`LaggAt/ActivityWatchVS` - Visual Studio extension, by :gh-user:`LaggAt`
- :gh:`pascalwhoop/aw-idea` - (WIP) JetBrains IntelliJ IDEA/PyCharm/WebStorm/etc extension forked from wakatime, by :gh-user:`pascalwhoop`
- :gh:`kostasdizas/aw-watcher-sublime` - Sublime Text 3, by :gh-user:`kostasdizas`, and others
- :gh:`NicoWeio/aw-watcher-atom` - Atom, by :gh-user:`NicoWeio`
- :gh:`pytlus93/AwWatcherNetBeans82` - NetBeans 8.2, by :gh-user:`pytlus93`
- :gh:`LordGrimmauld/aw-watcher-obsidian` - Obsidian.md extension, by :gh-user:`LordGrimmauld`

Media watchers
--------------

If you want to more accurately track media consumption.

- :gh-aw:`aw-watcher-spotify` - (Beta) Uses the Spotify Web API to get the active track.
- :gh-aw:`aw-watcher-chromecast` - (not working yet) Watches what is playing on you Chromecast device.
- :gh-aw:`aw-watcher-openvr` - (not working yet) Watches active VR applications.
- :gh:`RundownRhino/aw-watcher-mpv-sender` - (WIP) Watches mpv and reports the currently playing video.
- :gh:`2e3s/aw-watcher-media-player` - Watches the currently playing media which is reported by most players to the system.

.. _other-watchers:

Other watchers
--------------

Other watchers to collect all kinds of data.

- :gh:`Alwinator/aw-watcher-table` - Monitors whether you have set your height-adjustable table to sitting or standing, by :gh-user:`Alwinator`
- :gh-aw:`aw-watcher-input` - (WIP) Tracks the number of keypresses and distance that mouse is moved.
- :gh:`akohlbecker/aw-watcher-tmux` - A plugin for tmux that allows monitoring activity in sessions and panes, by :gh-user:`akohlbecker`
- :gh:`bcbernardo/aw-watcher-ask` - (WIP) Periodically poses questions to the user and records her answers.
- :gh:`Alwinator/aw-watcher-utilization` - Monitors CPU, RAM, disk, network, and sensor usage, by :gh-user:`Alwinator`
- :gh:`abdnh/aw-watcher-anki` - An add-on for Anki that tracks time spent reviewing cards.
- :gh:`Edwardsoen/aw-watcher-steam` - A Watcher to monitor current game being played.
- :gh:`2e3s/awatcher` - A compiled watcher for X11 and Wayland to replace the original active window and AFK watchers, with workarounds for KDE and Gnome on Wayland.
- :gh:`RTnhN/aw-watcher-toggl` - A Watcher to import time entries from Toggl.
- :gh:`sameersismail/aw-watcher-netstatus` - Monitors if you're connected to a network, by :gh-user:`sameersismail`.

Custom visualizations
---------------------

Custom watchers might not be supported by the default visualizations, but ActivityWatch offers a way for watchers to provide their own visualizations. It is currently an experimental feature, but the following watchers have experimental custom visualizations:

- :gh-aw:`aw-watcher-input`
- :gh:`Alwinator/aw-watcher-utilization`

Custom watchers
---------------

For help on how to write your own watcher, see `examples/writing-watchers`.

Have you written one yourself? Send us a PR to have it included!
