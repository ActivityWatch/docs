Watchers
========

Watchers are the parts of ActivityWatch that do all the data collecting.

ActivityWatch comes bundled with two watchers by default:

 - :gh-aw:`aw-watcher-afk` - Watches for mouse & keyboard activity to detect if the user is active.
 - :gh-aw:`aw-watcher-window` - Watches the active window and its title.

The default watchers are collecting some of the most important data.
But there is more to collect, so here are some other watchers that let you do so.

Browser watchers
----------------

Watches properties of the active tab like title, URL, and incognito state.

 - :gh-aw:`aw-watcher-web` - The official browser extension, supports Chrome and Firefox.

Editor watchers
---------------

Watches the actively edited file and associated metadata like path, language, and project name (folder name of git root)

 - :gh-aw:`aw-watcher-vim` - vim extension, by :gh-user:`johan-bjareholt` and :gh-user:`ahnlabb`.
 - :gh-aw:`aw-watcher-vscode` - Visual Studio Code extension, by :gh-user:`Otto-AA`.
 - :gh:`pauldub/activity-watch-mode` - emacs mode forked from wakatime-mode, by :gh-user:`pauldub`.
 - :gh:`OlivierMary/aw-watcher-jetbrains` - JetBrains IntelliJ plugin, by :gh-user:`OlivierMary`.
 - :gh:`LaggAt/ActivityWatchVS` - Visual Studio extension, by :gh-user:`LaggAt`
 - :gh:`pascalwhoop/aw-idea` - (WIP) JetBrains IntelliJ IDEA/PyCharm/WebStorm/etc extension forked from wakatime, by :gh-user:`pascalwhoop`
 - :gh:`kostasdizas/aw-watcher-sublime` - Sublime Text 3, by :gh-user:`kostasdizas`

Media watchers
--------------

If you want to more accurately track media consumption.

 - :gh-aw:`aw-watcher-spotify` - (Beta) Uses the Spotify Web API to get the active track.
 - :gh-aw:`aw-watcher-chromecast` - (not working yet) Watches what is playing on you Chromecast device.
 - :gh-aw:`aw-watcher-openvr` - (not working yet) Watches active VR applications.

Custom watchers
---------------

For help on how to write your own watcher, see `writing-watchers`.

Have you written one yourself? Send us a PR to have it included!
