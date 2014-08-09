#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'digitalvapor'
AUTHOR_FULLNAME = u'Tom Spalding'
AUTHOR_EMAIL = 'antivapor@gmail.com' #gravatar
SITENAME = u'Field Notes'
SITEURL = 'http://digitalvapor.github.io/fieldnotes'
SITETAGLINE = 'nature + code + blog'
TWITTER_USERNAME = 'antivapor'
GOOGLE_ANALYTICS = 'UA-44642246-7'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('iNaturalist/digitalvapor', 'http://www.inaturalist.org/observations/digitalvapor'),
          ('iNaturalist/star_bit', 'http://www.inaturalist.org/observations/star_bit'),
          ('Digital Vapor and Star Bits', 'http://antivapor.net'),)

# Social widget
SOCIAL = (('github/digitalvapor', 'https://github.com/digitalvapor'),
          ('github/star-bit', 'https://github.com/star-bit'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PATH = 'content'
OUTPUT_PATH = 'output'
PLUGIN_PATH = 'plugins'
PLUGINS = ['assets']
THEME = 'themes/burrito'
WEBASSETS = True

NATURALISTS = ['digitalvapor','star_bit']

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

OUTPUT_RETENTION = ("keybase.txt")

DEFAULT_DATE_FORMAT = ('%Y-%m-%d')

# add paths to pelican
#STATIC_PATHS = ['img']

# Thumbnailer plugin options
# IMAGE_PATH = 'img'
# THUMBNAIL_DIR = 'thumbs'
# THUMBNAIL_SIZES = {
#     'thumbnail_square': '317',
#     'thumbnail_wide': '635x?',
# }

# markdown extensions for syntax highlighting
MD_EXTENSIONS = ['codehilite(css_class=highlight, linenums=False)','extra']

ARTICLE_URL = 'posts/{date:%Y}{date:%m}{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}{date:%m}{date:%d}/{slug}/index.html'
