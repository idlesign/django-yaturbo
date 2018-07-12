# -*- encoding: utf-8 -*-
from __future__ import unicode_literals


VERSION = (0, 1, 0)
"""Application version number tuple."""

VERSION_STR = '.'.join(map(str, VERSION))
"""Application version number string."""


default_app_config = 'yaturbo.config.YaturboConfig'