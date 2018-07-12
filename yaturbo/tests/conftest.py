# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from pytest_djangoapp import configure_djangoapp_plugin


pytest_plugins = configure_djangoapp_plugin({
    'INSTALLED_APPS': ['django.contrib.sites'],
    'SITE_ID': 1,
})
