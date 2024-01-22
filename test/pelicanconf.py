# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARCHIVES_SAVE_AS = 'pages/archives.html'
MENUITEMS = [ ('All posts', '/pages/archives.html') ]

SITENAME = 'Summary Test Site'
SITESUBTITLE = 'minchin.pelican.plugins.summary'
# SITEURL = 'https://abcdef.com'
SITEURL = ""

PATH = 'content'
# OUTPUT_PATH = "output"

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_MAX_ITEMS = 5
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'

CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "themes/Peli-Kiera"

DEFAULT_PAGINATION = 10

DEFAULT_CATEGORY = 'Misc'

USE_FOLDER_AS_CATEGORY = False #otherwise year categories will appear

PLUGINS = ['sitemap', 'more_categories', 'minchin.pelican.plugins.summary']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.5,
        'pages': 0.4
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'weekly',
        'pages': 'monthly'
    }
}

MARKDOWN = {
  'extension_configs': {
    'markdown.extensions.codehilite': {'css_class': 'highlight', 'linenums': True},
    'markdown.extensions.extra': {},
    'markdown.extensions.meta': {},
  },
  'output_format': 'html5',
}
