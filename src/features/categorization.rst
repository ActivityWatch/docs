Categorization
==============

When you look at the "Activity" view in the ActivityWatch web-ui you will see that there are some visualizations based on "categories".
A category is defined by a set of rules which can match window titles and application names.
Each category helps with grouping together multiple events in the past which create more easily understandable categories such as "Working", "Gaming" or "Social Media".
A category can then in turn also have sub-categories such as "Mail", "Minecraft" and "Facebook".

.. note::
    We do not support matching URLs yet, but it is a planned feature.

Adding and editing categories
-----------------------------

If you go to the "Settings" page in the ActivityWatch web-ui, there is a section called "Categorization" which lists all the current categories and its respective sub-categories.
You can add new categories and edit existing categories in this view.
When editing categories you have the option to name them, change their parent category and set a rule for them.


Rules
-----

A rule decides what text will match in an event.
If there are multiple categories matching the same event then the deepest sub-category will be chosen.

Currently there are only two rule options for categories, "Regex" or "No rule".

"No rule" means that the category will not match anything.

"Regex" means "Regular Expression" and is a format for expressing a text pattern.
There are a lot of great guides online on how to learn to use regular expressions.
The regex engine used by ActivityWatch right now is the one from the Python programming language.

In the future we might take a look at adding some other rule type to more easily express text patterns.
