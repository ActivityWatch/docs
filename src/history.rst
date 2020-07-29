History
=======

It all started in 2013 when I, the founder of this project, was just about to start university. I had been soaked in hacker and transhumanism culture for most of my adolescent life, and was eager to put my programming abilities to good use. I had many interests, among others in neuroscience, biohacking, and Quantified Self. A pivotal moment in my interest was when when I one day, long after first reading about `brain computer interfaces <https://en.wikipedia.org/wiki/Brain%E2%80%93computer_interface>`_, suddenly realized the implications of the future generations of the technology: We would be able to record our own thoughts and frictionlessly communicate them to others. I wrote a private note to myself, stating an intent that once the field has advanced sufficiently for research to start getting interesting I should make it a priority to contribute as much as I can.

Around the same time, I was obsessively collecting data on my behavior (then known as `lifelogging <https://en.wikipedia.org/wiki/Lifelog>`_, now more commonly known as `Quantified Self <https://en.wikipedia.org/wiki/Quantified_Self>`_). This included automated time-trackers (like ActivityWatch), a massive spreadsheet, a diary, location tracking, a step/sleep-tracker (Fitbit at the time), extensive use of version control, etc.

While unexpected, the similarities between brain computer interfaces and the behavioral aspects of Quantified Self became apparent over time. After all, the best approximation of our thoughts is our behavior. While we aren't yet able to automatically record our own thoughts, we are able to record our behaviors and what occupies our attention, such as which projects we work on, the ideas we read about, and the culture we consume.

So on Dec 30th, 2014, I started building a prototype. In April 2016 I started working on a rewrite (that included the client-server model) which became the foundation for what ActivityWatch is today. Some time in 2016, my brother :gh-user:`johan-bjareholt` became a regular contributor, and has since become the second largest contributor to the project by a wide margin.


Present
-------

Development is slowly but steadily moving forward as lead developer Erik Bjäreholt finishes his degree.

Focus currently lies on building tools for data exploration, building an `Android app <https://github.com/ActivityWatch/aw-android>`_, as well as making it easier to import and export data to and from ActivityWatch.


Future
------

There's much to be said here, and while the future is inherently unpredictable we've slowly started outlining `our vision for ActivityWatch <https://github.com/ActivityWatch/activitywatch/issues/236>`_.

Among other things, we're trying to `secure funding to ensure financial sustainability and accelerate development <https://github.com/ActivityWatch/activitywatch/issues/259>`_. In the meanwhile, we get some support from our wonderful users through `donations <https://activitywatch.net/donate/>`_.


Building new types of privacy-aware services which require data collection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many services rely on the collection of data in order to function, but the more data they need to collect the greater the privacy implications. One way to get around this is to never have a third party get access to the data at all, and keep the user in exclusive control of their data.

Examples:

 - :gh:`Thankful <SuperuserLabs/thankful>`, an application that tracks the users culture consumption, and allows them to automatically donate cryptocurrency to the creators of it.
 - Proposal for a `self-hosted newsfeed aggregator, with a highly customizable recommendation engine <https://erik.bjareholt.com/wiki/importance-of-open-recommendation-systems/>`_.


Ubiquitous recording for meaningful information about the past
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    "We live in an interesting time when more and more of our actions can be in some way recorded and played back without our intervention. \[...] There's voice recording technology. Web browsing history. Live desktop video recording and playback. Heck, some folks \[...] have shown us a taste of the future as power-users of autonomous or assisted self-recording technologies. Go-pro and other consumer tech products are thriving as they discover / cherry-pick / surface compelling use cases. I haven't experienced general-purpose AI which is quite up to the job of organizing my notes for me. But we're close to having ubiquitous recording (and storing bits is the important part -- facebook didn't start with entity tags on day 1 but has been able to retroactively infer and index these). There's no way to record everything with perfect fidelity, because that would require us to preserve as many bits as there are in reality (which violates physical constraints) but there's a lot we can do to improve. There are still unexplored frontiers, like recording, transmitting, and playing back one's thoughts (which I don't think we should consider science fiction, just somewhat expensive and contentious to make viable). Suffice to say, interfaces (there aren't great memex-like ways to create graph based notes with semantic, taggable entities), politics and logistics of services competing to silo our information, and insufficient AI to infer our meaning and, in fact, to de-duplicate our thoughts and those of others (read: https://distill.pub/2017/research-debt) are major barriers which conspire against making mind-mapping and organizing one's life's work frictionless."

    :gh-user:`mekarpeles` in a `comment on Facebook <https://www.facebook.com/michael.karpeles/posts/10103225650726950?comment_id=10103225680237810>`_.


