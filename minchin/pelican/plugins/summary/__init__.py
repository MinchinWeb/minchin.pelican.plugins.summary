__title__ = "minchin.pelican.plugins.summary"
__version__ = "1.3.1-dev"
__description__ = "This Pelican plugin allows easy, variable length summaries directly embedded into the body of your articles."
__author__ = "William Minchin"
__email__ = "w_minchin@hotmail.com"
__url__ = "https://github.com/MinchinWeb/minchin.pelican.plugins.summary"
__license__ = "GNU Affero General Public License v3"

from pelican import signals

from .summary import extract_summary, initialized, run_plugin


def register():
    signals.initialized.connect(initialized)
    try:
        signals.all_generators_finalized.connect(run_plugin)
    except AttributeError:
        # NOTE: This results in #314 so shouldn't really be relied on
        # https://github.com/getpelican/pelican-plugins/issues/314
        # Fixed in Pelican 3.6
        signals.content_object_init.connect(extract_summary)
