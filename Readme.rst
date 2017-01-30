=======
Summary
=======

``Summary`` is a plugin for `Pelican <http://docs.getpelican.com/>`_,
a static site generator written in Python.

``Summary`` allows easy, variable length summaries directly embedded into
the body of your articles.


Installation
============

The easiest way to install ``Summary`` is through the use of pip. This
will also install the required dependencies automatically.

.. code-block:: sh

  pip install minchin.pelican.plugins.summary

Then, in your ``pelicanconf.py`` file, add ``Summary`` to your list of
plugins:

.. code-block:: python

  PLUGINS = [
              # ...
              'minchin.pelican.plugins.summary',
              # ...
            ]

You may also need to configure the summary start and end markers (see
Configuration below).


Requirements
============

``Summary`` depends on (and is really only useful with) Pelican. This can
be manually installed with pip:

.. code-block:: sh

   pip install pelican



Configuration and Usage
=======================

This plugin introduces two new settings: ``SUMMARY_BEGIN_MARKER`` and
``SUMMARY_END_MARKER``: strings which can be placed directly into an
article to mark the beginning and end of a summary. When found, the
standard ``SUMMARY_MAX_LENGTH`` setting will be ignored. The markers
themselves will also be removed from your articles before they are
published. The default values are ``<!-- PELICAN_BEGIN_SUMMARY -->`` and
``<!-- PELICAN_END_SUMMARY -->``.

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
beginning marker was found, it starts at the top of the body. It is
possible to leave out the end marker instead, in which case the summary
will start at the beginning marker and continue to the end of the body.

If no beginning or end marker is found, and if
``SUMMARY_USE_FIRST_PARAGRAPH`` is enabled in the settings, the summary
will be the first paragraph of the post.

The plugin also sets a ``has_summary`` attribute on every article. It is
True for articles with an explicitly-defined summary, and False otherwise.
(It is also False for an article truncated by ``SUMMARY_MAX_LENGTH``.)
Your templates can use this e.g. to add a link to the full text at the end
of the summary.

reST example
~~~~~~~~~~~~

Inserting the markers into a reStructuredText document makes use of the
comment directive, because raw HTML is automatically escaped. The reST
equivalent of the above Markdown example looks like this::

    My super title
    ##############

    :date: 2010-12-03 10:20
    :tags: thats, awesome
    :category: yeah
    :slug: my-super-post
    :author: Alexis Metaireau

    This is the content of my super blog post.

    .. PELICAN_END_SUMMARY

    and this content occurs after the summary.

Credits
=======

Original plugin from the `Pelican-Plugins repo
<https://github.com/getpelican/pelican-plugins>`_.

License
=======

The plugin code is assumed to be under the AGPLv3 license (this is the
license of the Pelican-Plugins repo).
