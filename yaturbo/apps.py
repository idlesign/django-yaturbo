from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class YaturboConfig(AppConfig):
    """Application configuration."""

    name = 'yaturbo'
    verbose_name = _('Yandex Turbo Pages')
