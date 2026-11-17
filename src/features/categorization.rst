Categorization
==============

When you look at the "Activity" view in the ActivityWatch UI you will see that there are some visualizations based on "categories".

Categories are used to group together multiple events, which create more easily understandable labels for the data such as "Work", "Gaming" or "Social Media".

Categorized summaries are also the safest starting point for AI-assisted
analysis. See :doc:`../examples/agents-and-ai` for a workflow that shares
category and app totals with an assistant while avoiding raw titles and URLs by
default.

Each category has a title, a parent category (optional), child categories (optional), and a categorization rule which is used to match events on window titles and application names.

A category can have child categories ("Work" might have "Mail", "Gaming" might have "Minecraft", etc). Child categories have independent categorization rules, but the time attributed to the children of a parent category is often added to the parent category in visualizations.

Adding and editing categories
-----------------------------

If you go to the "Settings" page in the ActivityWatch UI, there is a section called "Categorization" which lists all the current categories and its respective sub-categories.
You can add new categories and edit existing categories in this view.
When editing categories you have the option to name them, change their parent category, set a rule for them, and (for regex rules) set an optional priority.

Rules
-----

A rule decides what text will match in an event.
If several rules match the same event, the highest-ranking one is chosen (see `Priority`_ below). When no priority is set, that is the deepest matching subcategory.

Currently there are only two rule options for categories: "Regex" or "No rule".

Regular expressions (RegEx)
***************************

"RegEx" is short for "Regular Expression" and is a way to express a text pattern. The regular expression is matched on the 'app' and 'title' value of events (not yet URLs).

.. note::
    We do not support matching URLs from the web watcher yet, but it is a planned feature. You can work around this by using a browser extensions that adds the URL to the window title (`Chrome <https://chrome.google.com/webstore/detail/url-in-title/ignpacbgnbnkaiooknalneoeladjnfgb>`_, `Firefox <https://addons.mozilla.org/en-US/firefox/addon/add-url-to-window-title/>`_).

There are lots of great guides online where you can learn to write regular expressions. There are also sites like `regex101.com <https://regex101.com/>`_ where you can easily try out patterns.

Note that some characters have special meaning in regular expressions, notably: ``.`` (period, acts as wildcard for any character), ``$`` (matches end of string), ``^`` (matches start of string), ``+``, ``*``, ``?``, and brackets of all kinds.

With some care, these can be escaped (often by wrapping them in a 'character class', like this: ``[.]``).

Examples:

- ``Gmail|Thunderbird`` will match events *containing* either ``Gmail`` or ``Thunderbird``
- ``^Settings$`` will match events with app or title being *exactly* ``Settings``
- An empty string will match *everything*, so be careful!

  - If you want a category without a rule, use the 'No rule' rule type instead.

The regex engine used by ActivityWatch is the one from the Python programming language (of if you use aw-server-rust, the engine provided by the ``regex`` crate).

No rule
*******

"No rule" simply means that the category will not match anything (but its child categories still might). You can use this to create category groups which won't get matched themselves, but only be used as 'folders' for child categories.

In the future we might take a look at adding some other rule type to more easily express text patterns.

Priority
********

When more than one regex rule matches the same event, ActivityWatch picks the highest-ranking match.

A rule's rank is:

- the **Priority** field, if you set one (an integer; higher wins)
- otherwise ``10 × depth``, where a top-level category has depth 1 (rank 10) and a child has depth 2 (rank 20)

Leaving Priority blank keeps the historical "deepest matching subcategory wins" behavior. An explicit value *replaces* that default; it does not add to it.

To deprioritize a fallback or catch-all relative to unprioritized rules, set its Priority to ``0``. That ranks below every default (the smallest default is 10). You do not need a negative priority for that.

Examples:

- Unprioritized ``Work`` (rank 10) loses to unprioritized ``Work > Programming`` (rank 20).
- A catch-all with Priority ``0`` loses to both of those.
- A shallow override with Priority ``25`` beats an unprioritized child (20).

The editor accepts a blank default or a non-negative integer. Negative priorities are understood by the categorization engine but are not offered in the editor, and older servers fail to parse them (see :issue:`1539`).
