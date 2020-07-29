Development
===========

.. note::
    This part is a work in progress, reach out to the maintainers if you have any questions!

We recommend you follow Kenneth Reitz folder structure guide when writing Python programs which will be under the control of the ActivityWatch organisation: http://docs.python-guide.org/en/latest/writing/structure/

Working with submodules
-----------------------

Working with submodules comes with some complexity, here are a few neat tricks to make things easier:

 - We recommend configuring git to include submodule changes in :code:`git status`, you can do so with the following: :code:`git config --global status.submoduleSummary true`
 - If you want the latest committed version of all submodules, use: :code:`git submodule update --recursive`
 - If you want the latest master branch on all submodules, use: :code:`git submodule update --recursive --remote`
 - If you want to ensured you've pushed all commits in the submodules, use: :code:`git submodule foreach 'git push'`

A longer guide to git submodules can be found `here <https://medium.com/@porteneuve/mastering-git-submodules-34c65e940407>`_.

Making a release
----------------

#. Close `milestone on GitHub <https://github.com/ActivityWatch/activitywatch/milestones>`_ if one exists.
#. Ensure that all the tests pass: ``make test && make test-integration``
#. Test the latest build and check that it works correctly
    - Travis artifacts are available in S3 at the base URL: https://activitywatch-builds.s3.amazonaws.com/
    - Appveyor artifacts are available on Appveyor.
#. Write a changelog entry in ``docs/changelog.rst``
#. Sign the commit: ``git commit -a -S -m "bumped version"``
#. Create a signed tag: ``git tag -s v0.7.1``
#. Push the commit and tag: ``git push origin refs/tags/v0.7.1``
#. Create a release on GitHub
    - Generate commit changelog with ``python3 scripts/build_changelog.py``
    - Clean it a bit (remove non-user-affecting changes, merge commits etc)
#. Wait for the builds to finish
#. Post about it online: Twitter, the forum, mailinglist (if major)
