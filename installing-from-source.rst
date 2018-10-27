Installing from source
======================

Here's the guide to installing ActivityWatch from source. If you are just looking to try it out, see the getting started guide instead.

.. note::
   This is written for Linux and macOS. For Windows the build process is more complicated and we therefore suggest using the pre-built packages instead on that operating system.

Cloning the submodules
----------------------

Since the ActivityWatch bundlerepo uses submodules, you first need to clone the submodules.

This can either be done at the cloning stage with:

.. code-block:: sh

   git clone --recursive https://github.com/ActivityWatch/activitywatch.git

Or afterwards (if you've already cloned normally) using:

.. code-block:: sh

   git submodule update --init --recursive


Checking dependencies
---------------------

You need to ensure you have:

- Python 3.5 or later, check with :code:`python3 -V` (required to build the core components)
- Node 5 or higher, check with :code:`node -v` and :code:`npm -v` (required to build the web UI)


Using a virtualenv
------------------

.. note::
   If you don't want to use a virtualenv you could instead set the environment variable :code:`PIP_USER=true` when building in the next step.
   But make sure that the folder :code:`~/.local/bin` (on Linux) or :code:`~/Library/Python/<version>/bin` (on macOS) is in your PATH.

It is recommended to use a virtualenv in order to avoid polluting your system with ActivityWatch-specific Python packages.
It also makes it easier to uninstall since all you have to do is remove the virtualenv folder.

.. code-block:: sh

    python3 -m venv venv

Now activate the virtualenv in your current shell session:

.. code-block:: sh

    # For bash/zsh users:
    source ./venv/bin/activate
    # For Windows git bash users:
    source ./venv/Scripts/activate
    # For fish users:
    source ./venv/bin/activate.fish
    


Building and installing
-----------------------

Build and install everything into the virtualenv:

.. code-block:: sh

    make build

.. note::
   If you're building from source to develop we suggest building/installing using :code:`make build DEV=true` which installs all Python packages with pip's handy :code:`--editable` flag.
   By doing this you wont have to reinstall everything whenever you want to try out a code change.

Running
-------

Now you should be able to start ActivityWatch **from the terminal where you've activated the virtualenv**. Or, if you were using the :code:`PIP_USER` trick, from any terminal with a correctly configured PATH.
You have two options:

1. Use the trayicon manager (Recommended for normal use)

   - Run from your terminal with: :code:`aw-qt`

2. Start each module separately (Recommended for developing)

   - Run from your terminal with: :code:`aw-server`, :code:`aw-watcher-afk`, and :code:`aw-watcher-window`

Both methods take the :code:`--testing` flag as a command line parameter to run in testing mode. This runs the server on a different port (5666) and uses a separate database file to avoid mixing your important data with your testing data.

Now everything should be running!
Check out the web UI at http://localhost:5600/

If anything doesn't work, let us know!

.. note::
   On Linux, if you want to run from source using a :code:`.desktop` file launcher, see `this issue <https://github.com/ActivityWatch/activitywatch/issues/176>`_.

Updating from source
--------------------

First pull the latest version of the repo with :code:`git pull` then get the updated submodules with :code:`git submodule update --init --recursive`. All that's needed then is a :code:`make build`.

If it doesn't work, you can first try to run :code:`make uninstall` and then do a fresh :code:`make build`. If that fails as well, remove the virtualenv and start over.

Please report all issues you might have so we can make things easier for future users.

Packaging your changes
----------------------

If you made some changes and want to run your code as you would normally do outside of the development environment you will need to install pyinstaller and python3-dev and package activitywatch

.. code-block:: sh

   pip3 install pyinstaller
   apt install python3-dev
   
Then package it

.. code-block:: sh
   
   make package
   
When the packaging is done you will have :code:`./dist` folder where you can find a zipped version and an unzipped :code:`activitywatch` folder, you can move or copy that folder anywhere you need and set :code:aw-qt to run from startup.


