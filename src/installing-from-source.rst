Installing from source
======================

Here's the guide to building ActivityWatch from source. If you are just looking to try it out, see the :doc:`getting started guide <getting-started>` instead.

.. contents::

Cloning the repository and submodules
-------------------------------------

Since the main ActivityWatch repository uses git submodules to manage its modules, you first need to clone the repo and then the submodules.

You can do both in one step with:

.. code-block:: sh

   git clone --recursive https://github.com/ActivityWatch/activitywatch.git

Or, if you've already cloned normally, you can clone the submodules using:

.. code-block:: sh

   git submodule update --init --recursive

If you want to ensure you have the latest version of all submodules, preserving any feature branches you have:

.. code-block:: sh

   git submodule foreach --recursive git pull

Checking dependencies
---------------------

You need:

- `Git <https://git-scm.com/downloads>`_
- `Python 3.7 to 3.9 <https://www.python.org/downloads/>`_, check with :code:`python3 -V` (required to build the core components)
- `Poetry 1.2 <https://python-poetry.org/docs/#installation>`_, check with :code:`poetry -V` (can be installed like this: :code:`python3 -m pip install poetry`)
- `Node 12 or higher <https://www.npmjs.com/get-npm>`_, check with :code:`node -v` and :code:`npm -v` (required to build the web UI)
- `Rust nightly <https://doc.rust-lang.org/cargo/getting-started/installation.html>`_ (nightly can be installed using :code:`rustup update`), check with :code:`rustc -V` and :code:`cargo -V` (for building aw-server-rust)

**For Windows users:**

- `gnuwin32 <http://gnuwin32.sourceforge.net/packages/make.htm>`_, to get the make command on Windows.
- (optional) `7 Zip <https://www.7-zip.org/>`_, for packaging the zip.
- (optional) `InnoSetup 6 <https://chocolatey.org/packages/InnoSetup>`_, for packaging the installer, can be installed using `Chocolatey <https://chocolatey.org/docs/installation>`_.

**Commands which should work before building:**

- :code:`git --version`
- :code:`make --version`
- :code:`python --version`
- :code:`poetry --version`
- :code:`node --version` / :code:`npm --version`
- :code:`rustc --version` / :code:`cargo --version`
- :code:`7z` (optional)

If any of these don't work, make sure you've correctly installed them and have them in your PATH variable.

Using a virtualenv
------------------

It is highly recommended to use a virtualenv <https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/> in order to minimize problems and avoid polluting your system with ActivityWatch-specific Python packages. It also makes it easier to uninstall since all you have to do is remove the virtualenv folder.

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

All the modules need to be installed in the same env in order to avoid build issues. This is why creating a single venv for all activitywatch repos is important and why relying on poetry to setup a per-folder venv is not an option.

The watchers all use the published versions of :code:`aw-client`. If you want to use a development version of this client, you'll need to override the definition in the :code:`pyproject.toml` file via :code:`aw-client = {path = "../aw-client" }`.

Building and installing
-----------------------

Build and install everything into the virtualenv:

.. code-block:: sh

    make build

Running
-------

Now you should be able to start ActivityWatch **from the terminal where you've activated the virtualenv**.

There are two ways to run ActivityWatch:

1. Use the trayicon manager (Recommended for normal use)

   - Run from your terminal with: :code:`aw-qt`

2. Start each module separately (Recommended for developing)

   - Run from your terminal with: :code:`aw-server`, :code:`aw-watcher-afk`, and :code:`aw-watcher-window`
   - For the rust server, run with: :code:`aw-server-rust/target/package/aw-server-rust`

Both methods take the :code:`--testing` flag as a command line parameter to run in testing mode. This runs the server on a different port (5666) and uses a separate database file to avoid mixing your important data with your testing data.

Now everything should be running!
Check out the web UI at http://localhost:5600/

If anything doesn't work, let us know!

.. note::
   On Linux, if you want to run from source using a :code:`.desktop` file launcher, see :issue:`176`.

Updating from source
--------------------

First pull the latest version of the repo with :code:`git pull` then get the updated submodules with :code:`git submodule update --init --recursive`. All that's needed then is a :code:`make build`.

If it doesn't work, you can first try to run :code:`make uninstall` and then do a fresh :code:`make build`. If that fails as well, remove the virtualenv and start over.

Please report all issues you encounter so we can make things easier for future users.

Packaging your changes
----------------------

If you made some changes and want to create a proper build with portable executables (like normal ActivityWatch releases) you need to install :code:`pyinstaller` (and on Debian-like distros :code:`python3-dev`).

.. code-block:: sh

   apt install python3-dev  # Or equivalent for your Linux distribution
   pip3 install --user pyinstaller

Then simply run the following to package it:

.. code-block:: sh

   make package

When the packaging is done you will have a :code:`./dist` folder where you can find:

 - A :code:`activitywatch` folder, you can move or copy that folder anywhere you need and set :code:`aw-qt` to run from startup.
 - A zipped version of the folder.
 - (on Windows) An installer.
