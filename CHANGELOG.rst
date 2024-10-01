Summary Changelog
=================

This Changelog is for ``minchin.pelican.plugins.summary``.

- :release`1.3.0 <2024-09-30>`
- :support:`-` remove namespace ``__init__.py`` files; otherwise ``setuptools``
  is a required dependency.
- :bug:`7 major` get unittests running again.
- :bug:`5 major` require Pelican 4.10 or later. Keeps internal link indicators
  (like ``{filename}``) from leaking into summaries. C.f. `Pelican Issue #3265
  <https://github.com/getpelican/pelican/issues/3265>`_.
- :support:`-` swap from ``setup.py`` to ``pyproject.toml``
- :feature:`-` add (basic) test site.
- :bug:`- major` logging now has the right prefix.
- :release`1.2.1 <2023-08-09>`
- :bug:`-` blacklist ``autoloader`` v1.2.0
- :release`1.2.0 <2022-06-10>`
- :feature:`-` set up for autoloading
- :feature:`1` add support for Pelican 4. Thanks `Henry Swanson
  <https://github.com/HenrySwanson/>`_!
- :release:`1.1.1 <2017-04-18>`
- :bug:`-` add Pelican trove classifier
- :release:`1.1.0 <2017-01-29>`
- :support:`-` first release to PyPI
- :support:`-` add release machinery
- :support:`-` move package to ``minchin.pelican.plugins.summary``
- :release:`1.0.0 <2017-01-29>`
- :support:`-` extract existing code from
  https://github.com/getpelican/pelican-plugins
