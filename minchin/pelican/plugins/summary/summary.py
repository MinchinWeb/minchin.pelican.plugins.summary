"""
Summary
-------

This plugin allows easy, variable length summaries directly embedded into the
body of your articles.
"""

import logging
import re

import semantic_version

from pelican import __version__ as pelican_version
from pelican.generators import ArticlesGenerator, PagesGenerator

LOG_PREFIX = "[Summary]"

logger = logging.getLogger(__name__)


def _pelican_summary_as_metadata():
    """
    Determine if the installed version of Pelican stores the summary in the
    metadata table.

    In short, the Pelican version must be greater than or equal to 4.0.0.

    Pelican switched from `instance._summary` to `instance.metadata["summary"]`
    in preparation for the release of Pelican 4. (Actual commit is 06fd9b dated
    2018-02-09).

    Return:
        bool: if summary is stored in the metadata table.
    """

    pelican_semver = semantic_version.Version(pelican_version)
    if pelican_semver.major >= 4:
        return True
    else:
        return False


def initialized(pelican_instance):
    from pelican.settings import DEFAULT_CONFIG

    DEFAULT_CONFIG.setdefault("SUMMARY_BEGIN_MARKER", "<!-- PELICAN_BEGIN_SUMMARY -->")
    DEFAULT_CONFIG.setdefault("SUMMARY_END_MARKER", "<!-- PELICAN_END_SUMMARY -->")
    DEFAULT_CONFIG.setdefault("SUMMARY_USE_FIRST_PARAGRAPH", False)
    if pelican_instance:
        pelican_instance.settings.setdefault(
            "SUMMARY_BEGIN_MARKER", "<!-- PELICAN_BEGIN_SUMMARY -->"
        )
        pelican_instance.settings.setdefault(
            "SUMMARY_END_MARKER", "<!-- PELICAN_END_SUMMARY -->"
        )
        pelican_instance.settings.setdefault("SUMMARY_USE_FIRST_PARAGRAPH", False)

    logger.debug("%s initalized", LOG_PREFIX)

    logger.debug("%s FORMATTED_FIELDS=%s", LOG_PREFIX, pelican_instance.settings["FORMATTED_FIELDS"])


def extract_summary(instance):
    # if summary is already specified, use it
    # if there is no content, there's nothing to do
    if (
        "summary" in instance.metadata.keys() and instance.metadata["summary"]
    ) or hasattr(instance, "_summary"):
        instance.has_summary = True
        return

    if not instance._content:
        instance.has_summary = False
        return

    begin_marker = instance.settings["SUMMARY_BEGIN_MARKER"]
    end_marker = instance.settings["SUMMARY_END_MARKER"]
    use_first_paragraph = instance.settings["SUMMARY_USE_FIRST_PARAGRAPH"]
    remove_markers = True

    content = instance.content
    begin_summary = -1
    end_summary = -1
    if begin_marker:
        begin_summary = content.find(begin_marker)
    if end_marker:
        end_summary = content.find(end_marker)

    if begin_summary == -1 and end_summary == -1 and use_first_paragraph:
        begin_marker, end_marker = "<p>", "</p>"
        remove_markers = False
        begin_summary = content.find(begin_marker)
        end_summary = content.find(end_marker)

    if begin_summary == -1 and end_summary == -1:
        instance.has_summary = False
        return

    # skip over the begin marker, if present
    if begin_summary == -1:
        begin_summary = 0
    else:
        begin_summary = begin_summary + len(begin_marker)

    if end_summary == -1:
        end_summary = None

    summary = content[begin_summary:end_summary]

    if remove_markers:
        # remove the markers from the content
        if begin_summary:
            content = content.replace(begin_marker, "", 1)
        if end_summary:
            content = content.replace(end_marker, "", 1)

    summary = re.sub(r"<div.*>", "", summary)
    summary = re.sub(r"</div>", "", summary)

    instance._content = content
    if _pelican_summary_as_metadata():
        # Pelican >= 4.0.0
        instance.metadata["summary"] = summary
    else:
        instance._summary = summary
    instance.has_summary = True


def run_plugin(generators):
    # Pelican >= 3.6
    for generator in generators:
        if isinstance(generator, ArticlesGenerator):
            for article in generator.articles:
                extract_summary(article)
        elif isinstance(generator, PagesGenerator):
            for page in generator.pages:
                extract_summary(page)
