#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Alexandra'
SITENAME = 'The Data Curious'
SITEURL = ''
FAVICON = '/images/favicon.ico'
PATH = 'content'

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


# Social widget
SOCIAL = (('tableau', 'https://public.tableau.com/profile/alexandra2756#!/'),
('linkedin', 'https://linkedin.com/in/alexandra-khoo-15517557'))

DEFAULT_PAGINATION = 5

HEADER_COVERS_BY_TAG = {'about': 'images/about_cover.jpg'}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
