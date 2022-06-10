=======
Summary
=======

``Summary`` is a plugin for `Pelican <http://docs.getpelican.com/>`_,
a static site generator written in Python.

``Summary`` allows easy, variable length summaries directly embedded into
the body of your articles.

.. image:: https://img.shields.io/pypi/v/minchin.pelican.plugins.summary.svg?style=flat
    :target: https://pypi.python.org/pypi/minchin.pelican.plugins.summary/
    :alt: PyPI version number

.. image:: https://img.shields.io/badge/-Changelog-success
   :target: https://github.com/MinchinWeb/minchin.pelican.plugins.summary/blob/master/CHANGELOG.rst
   :alt: Changelog

.. image:: https://img.shields.io/pypi/pyversions/minchin.pelican.plugins.summary?style=flat
    :target: https://pypi.python.org/pypi/minchin.pelican.plugins.summary/
    :alt: Supported Python version

.. image:: https://img.shields.io/pypi/l/minchin.pelican.plugins.summary.svg?style=flat&color=green
    :target: https://github.com/MinchinWeb/minchin.pelican.plugins.summary/blob/master/LICENSE
    :alt: License

.. image:: https://img.shields.io/pypi/dm/minchin.pelican.plugins.summary.svg?style=flat
    :target: https://pypi.python.org/pypi/minchin.pelican.plugins.summary/
    :alt: Download Count


Installation
============

The easiest way to install ``Summary`` is through the use of pip. This
will also install the required dependencies automatically.

.. code-block:: sh

  pip install minchin.pelican.plugins.summary

If you are using Pelican 4.5, it should automatically be activated (through my
AutoLoader plugin). 

If you are using an earlier version of Pelican or autoloading isn't working,
then in your ``pelicanconf.py`` file, add ``Summary`` to your list of plugins:

.. code-block:: python

  PLUGINS = [
      # others...
      'minchin.pelican.plugins.summary',
      # ...
  ]

You may also need to configure the summary start and end markers (see
Configuration below).


Requirements
============

``Summary`` depends on (and is really only useful with) Pelican; it also
depends on ``semantic-version`` and ``minchin.pelican.plugins.autoloader``.
These can be manually installed with pip (but are automatically installed if
the plugin is installed with pip):

.. code-block:: sh

   pip install pelican semantic-version minchin.pelican.plugins.autoloader


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

ReST example
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


Pelican 3 Support
=================

The plugin also includes support for Pelican 3, however general support for
Pelican 3 is somewhat limited. In particular, Python 3.9 or earlier is needed,
and the most recent version dependencies include ``pelican==3.7.1``,
``jinja2==2.11.3``, and ``markupsafe==1.1.1``.

For extra clarity, the plugins to designed to support Pelican 4 as well.


Test Suite
==========

There is an included test suite, available at
``minchin\pelican\plugins\summary\test_summary.py``. The plugin itself doesn't
need to be installed for the suite to run, but the plugin dependencies do need
to be installed.


Credits
=======

Original plugin from the `Pelican-Plugins repo
<https://github.com/getpelican/pelican-plugins>`_.


License
=======

The plugin code is assumed to be under the AGPLv3 license (this is the
license of the Pelican-Plugins repo).
