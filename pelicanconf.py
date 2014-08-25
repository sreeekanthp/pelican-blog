#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sreekanth'
SITENAME = u'Sreekanth\'s Blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

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
#RELATIVE_URLS = True


#Navigation sections and relative URL:
SECTIONS = [('Blog', 'index.html'),
        ('Archive', 'archives.html'),
        # ('Tags', 'tags.html'),
        # ('Projects', 'pages/projects.html'),
        # ('Talks', 'pages/talks.html'),
        ('About', 'pages/about.html')]

DEFAULT_CATEGORY = 'Uncategorized'
DATE_FORMAT = {
'en': '%d %b %Y'
}
DEFAULT_DATE_FORMAT = '%d %b, %Y'

DISQUS_SITENAME = "sreekanth_p"
TWITTER_USERNAME = 'sreekanthp91'
LINKEDIN_URL = 'https://www.linkedin.com/profile/view?id=96839960'
GITHUB_URL = 'http://github.com/you'
FACEBOOK_URL = 'http://www.facebook.com/sreekanthkaralmanna'
GOOGLEPLUS_URL = 'https://plus.google.com/u/0/106300911869415325463/posts'
# PINTEREST_URL = 'http://pinterest.com/you'

PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = ""

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

OUTPUT_PATH = 'output'

# GOOGLE_ANALYTICS_ACCOUNT = 'UA-00000000-1'

# PIWIK_URL = 'myurl.com/piwik'
# PIWIK_SSL_URL = 'myurl.com/piwik'
# PIWIK_SITE_ID = '1'

MAIL_USERNAME = 'sreekanthkaralmanna'
MAIL_HOST = 'gmail.com'

# static paths will be copied under the same name
STATIC_PATHS = ["images"]

# A list of files to copy from the source to the destination
#FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)

THEME = "themes/flasky"