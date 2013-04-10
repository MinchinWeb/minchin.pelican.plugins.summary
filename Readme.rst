Summary
-------

This plugin allows easy, variable length summaries directly embedded into the 
body of your articles. It introduces two new settings: ``SUMMARY_BEGIN_MARKER``
and ``SUMMARY_END_MARKER``: strings which can be placed directly into an article
to mark the beginning and end of a summary. When found, the standard 
``SUMMARY_MAX_LENGTH`` setting will be ignored. The markers themselves will also
be removed from your articles before they are published. The default values
are ``<!-- PELICAN_BEGIN_SUMMARY -->`` and ``<!-- PELICAN_END_SUMMARY -->``.
For example::

    Title: My super title
    Date: 2010-12-03 10:20
    Tags: thats, awesome
    Category: yeah
    Slug: my-super-post
    Author: Alexis Metaireau
    
    This is the content of my super blog post.
    <!-- PELICAN_END_SUMMARY -->
    and this content occurs after the summary.

Here, the summary is taken to be the first line of the post. Because no
beginning marker was found, it starts at the top of the body. It is possible
to leave out the end marker instead, in which case the summary will start at the
beginning marker and continue to the end of the body.