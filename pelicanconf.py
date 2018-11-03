#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Alexandra'
SITENAME = 'The Data Curious'
SITEURL = 'https://thedatacurious.github.io'
PATH = 'content'
STATIC_PATHS = ['extra', 'images']

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extra/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extra/android-chrome-144x144.png': {'path': 'android-chrome-144x144.png'},
    'extra/safari-pinned-tab.svg': {'path': 'safari-pinned-tab.svg'},
    'extra/site.webmanifest': {'path': 'site.webmanifest'},
    'extra/mstile-150x150.png': {'path': 'mstile-150x150.png'},
    'extra/apple-touch-icon.png': {'path': 'apple-touch-icon.png'}
}

TIMEZONE = 'Asia/Singapore'

DEFAULT_LANG = 'en'

DATE_FORMATS = {
    'en': '%B %d, %Y',}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'attila'
HEADER_COVER = 'images/main_cover.jpg'
COLOR_SCHEME_CSS = 'monokai.css'
LOAD_CONTENT_CACHE = False
CSS_OVERRIDE = ['myblog.css']

# Social widget
SOCIAL = (('tableau', 'https://public.tableau.com/profile/alexandra2756#!/'),
('linkedin', 'https://linkedin.com/in/alexandra-khoo-15517557'))

DEFAULT_PAGINATION = 5

HEADER_COVERS_BY_TAG = {'about': 'images/about_cover.jpg'}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
