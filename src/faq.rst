FAQ
===

..
   Some of this should probably be moved to a development FAQ.

.. note::
   Some of these questions are technically not frequently asked.

Where is my data stored?
------------------------

All your data is stored in a SQLite database in the :ref:`data directory <data-directory>`.

How do I interpret the raw data?
--------------------------------

First, familiarize yourself with the `data model <buckets-and-events>`. After that, you might want to have a look at the `Examples`.

How can I use ActivityWatch with my own code?
---------------------------------------------

See the `Examples` for different ways to use ActivityWatch programmatically.

.. _how-does-aw-know-when-im-afk:

How does ActivityWatch know when I am AFK?
------------------------------------------

On Windows and macOS, we use functionality offered by those platforms to give us the
time since last input.

On Linux, we monitor all mouse and keyboard activity to calculate the time
since last input. We do not store what that activity was, just that it happened.

Using this data (seconds since last input) we check if more than 3 minutes have passed without any input. If that is the case, we assume that you've been AFK since the last input was received. You'll be assumed to be active again on next input.

If the browser watcher is running, the user will also by default be considered to not be AFK when the active browser tab has sound playing from it. This helps when the user for example watches a video or is in a video/audio meeting.

Why is the active window logged as "unknown" when using Wayland?
----------------------------------------------------------------

The Wayland protocol does not have a notion of an active window, and it is unlikely to ever have.
Wayland is also developed with security in mind, so access should be handed out on an app-by-app basis.
This is a good idea, any application shouldn't just give that privacy-sensitive information away freely.

Unfortunately, in Wayland compositors like Gnome's Mutter there is no way at all to get the current window, this leaves the window watcher completely disabled in Wayland.

*Solutions:*
- Switch to using X11.
- Try an alternative AFK and window :ref:`watcher <other-watchers>` which supports Wayland.

You can see the general status of the ability of `getting the active window in Wayland on StackOverflow <https://stackoverflow.com/questions/45465016/how-do-i-get-the-active-window-on-gnome-wayland>`_ or follow `the issue for ActivityWatch tracking the problem <https://github.com/ActivityWatch/activitywatch/issues/92>`_.

How accurate is ActivityWatch?
------------------------------

The design of ActivityWatch is that it consists of multiple watchers which report different types of activities.
Each watcher has its own flaws in accuracy for different reasons.
An example is the window watcher, which could be reporting that the user's activity is on a certain window, while the user is looking at another window and not the one that is currently in focus.
Another example, but for the AFK watcher would be that the user might be engaged in something on the computer without using the mouse or keyboard (see :ref:`How does ActivityWatch know when I am AFK? <how-does-aw-know-when-im-afk>`).
These examples are not a comprehensive list of all flaws in the accuracy of these watchers.

The data that ActivityWatch collects and the stats it can present can only be seen as an estimate.
The accuracy will vary depending on use-case and depending on what data you are looking at.
Even if the tracking was perfect, what should be considered being "active" is subjective.

What happens if it is down or crashes?
--------------------------------------

ActivityWatch consists of several processes running independently, so one thing crashing will have limited impact on the rest of the system.

If the server crashes or is unavailable, watchers which use the `heartbeat <heartbeats>` queue will queue heartbeats until the server becomes available.

If a watcher crashes, its bucket will simply remain untouched until it is restarted.

..
    What happens when my computer is off or asleep?
    -----------------------------------------------

    If your computer is off or asleep, watchers will usually record nothing. i.e. one events ending (:code:`timestamp + duration`) will not match up with the following event's beginning (:code:`timestamp`).

Some events have 0 duration. What does this mean?
-------------------------------------------------

`Watchers` most commonly use a polling method called `heartbeats` in order to store information on the server.
Heartbeats are received regularly with some data, and when two consecutive heartbeats have identical data, they get merged and the duration of the new one becomes the time difference between the previous two.
Sometimes, a single heartbeat doesn't get a following event with identical data. It is then impossible to know the exact duration of that event, so the assumption about when it really started/ended will be postponed until the analysis stage (usually handled with :py:func:`flooding <aw_transform.flood>`).

The assumption could be made to consider all zero-duration events actually have a duration equal to the time of the next event, but all such assumptions are left to the analysis stage.
