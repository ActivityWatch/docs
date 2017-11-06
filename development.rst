Development
===========

.. note::
    This part is a work in progress, reach out to the maintainers if you have any questions!

We recommend you follow Kenneth Reitz folder structure guide when writing Python programs which will be under the control of the ActivityWatch organisation: http://docs.python-guide.org/en/latest/writing/structure/

Dependency graph
----------------

.. graphviz:: dependency.dot

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

1. Ensure that all the tests pass: :code:`make test && make test-integration`
2. Test the latest build and check that it works correctly
3. Write a changelog entry in :code:`docs/changelog.rst`
4. Sign the commit: :code:`git commit -a -S -m "bumped version"`
5. Create a signed tag: :code:`git tag -s v0.7.1`
6. Push the commit and tag: :code:`git push origin refs/tags/v0.7.1`
7. Create a release on GitHub
8. Wait for the builds to finish
9. Post about it online: Twitter, the forum, mailinglist (if major)
