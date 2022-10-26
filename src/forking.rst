Forking ActivityWatch
=====================

**How to fork ActivityWatch, the right way.**

This document is intended for people who want to fork ActivityWatch and make changes to it. It is not intended for people who want to contribute to the main ActivityWatch project.

ActivityWatch is licensed under the Mozilla Public License v2 (MPLv2), which means (simplified):

 - You can fork it, make changes to it, and distribute it under the same license.
 - You must publish changes you make to the source code (if you intend to distribute it)
 - You must not use the name "ActivityWatch" for your fork
 - You must not use the ActivityWatch logo for your fork
 - You must clearly mention that your fork is a fork of ActivityWatch, and that it is not otherwise affiliated with the main ActivityWatch project

**TL;DR: Forking is fine, but please don't use the name "ActivityWatch" for your fork, if you intend to distribute it.**


Working with a fork
-------------------

When forking the main ActivityWatch repo, you will notice that it uses git submodules for each of the modules. You therefore need to also fork the individual modules you wish to modify, and retarget the ``git submodule`` to use your forked repo.

This is a bit of a pain, but it's the only way to make sure that your forked repo can be built and run without any changes to the build system.

To minimize the headache of keeping your fork up to date with the main repo, we recommend you submit as many generally-useful PRs to the main ActivityWatch project as possible, then rebase or merge in upstream changes onto your fork.


Examples of forks
-----------------

These are just to serve as reference, and to keep track of forks.

 - :gh:`doubledashio/activitywatch` - Fork of ActivityWatch with internationalization support (French) among other changes, likely for some research purpose.
 - :gh:`simonperneel/activitywatch` - Fork used by a `EU-funded study on digital wellbeing <https://cordis.europa.eu/project/id/950635>`_.

If you fork ActivityWatch, please add your fork to this list.
