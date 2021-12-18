from .toolbox import YandexTurboFeed, sanitize_turbo


VERSION = (1, 0, 1)
"""Application version number tuple."""

VERSION_STR = '.'.join(map(str, VERSION))
"""Application version number string."""


default_app_config = 'yaturbo.apps.YaturboConfig'