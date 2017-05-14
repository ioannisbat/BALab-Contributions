#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'sta'
SITENAME = 'new'
SITEURL = ''

PATH = 'content'

PUBLICATIONS_SRC = 'content/pubs.bib'

TIMEZONE = 'Europe/Athens'

DEFAULT_LANG = 'Greek'

THEME = 'theme'

# static files to copy into root, very useful for robots.txt
FILES_TO_COPY = (
   ('extra/robots.txt', 'robots.txt'),
   ('extra/humans.txt', 'humans.txt'),
)
# directories to be copied into output/static/
STATIC_PATHS = ['img', 'css', 'js']
# very useful for debugging purposes
DELETE_OUTPUT_DIRECTORY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
