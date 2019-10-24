# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from .toolbox import YandexTurboFeed, sanitize_turbo


VERSION = (0, 3, 0)
"""Application version number tuple."""

VERSION_STR = '.'.join(map(str, VERSION))
"""Application version number string."""


default_app_config = 'yaturbo.config.YaturboConfig'