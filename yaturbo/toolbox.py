# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.syndication.views import Feed as _Feed
from django.utils.feedgenerator import Rss201rev2Feed as FeedType


class YandexTurboFeedType(FeedType):

    def __init__(self, *args, **kwargs):

        self._analytics = kwargs.pop('ya_analytics', [])
        self._ads = kwargs.pop('ya_ads', [])

        super(YandexTurboFeedType, self).__init__(*args, **kwargs)

    def rss_attributes(self):
        attrs = super(YandexTurboFeedType, self).rss_attributes()

        attrs.update({
            'xmlns:turbo': 'http://turbo.yandex.ru',
            'xmlns:yandex': 'http://news.yandex.ru',
        })

        return attrs

    def item_attributes(self, item):
        attrs = super(YandexTurboFeedType, self).item_attributes(item)

        if not item['ya_contents']:
            # No turbo content available.
            return attrs

        attrs.update({
            'turbo': 'true',
        })

        return attrs

    def add_root_elements(self, handler):
        super(YandexTurboFeedType, self).add_root_elements(handler)

        for params in self._analytics:
            handler.startElement('turbo:analytics', params)
            handler.endElement('turbo:analytics')

        for params in self._ads:
            handler.startElement('turbo:adNetwork', params)
            handler.endElement('turbo:adNetwork')

    def add_item_elements(self, handler, item):
        super(YandexTurboFeedType, self).add_item_elements(handler, item)

        # todo maybe
        # turbo:source
        # turbo:topic
        # yandex:related

        turbo_contents = item['ya_contents']

        if not turbo_contents:
            return

        handler.startElement('turbo:content', {})
        handler.ignorableWhitespace('<![CDATA[%s]]>' % turbo_contents)
        handler.endElement('turbo:content')


class YandexTurboFeed(_Feed):
    """Yandex Turbo Pages Feed.

    .. code-block:: python

        from yaturbo.toolbox import YandexTurboFeed

        class TurboFeed(YandexTurboFeed):
            '''
            More information on Django Syndication Feed Framework configuration:
            https://docs.djangoproject.com/en/2.0/ref/contrib/syndication/

            '''

            def item_turbo(self, item):
                return 'turbo contents'


        feed = TurboFeed()

        # configure Yandex Metrika counter
        feed.configure_analytics_yandex('123456789')

        # configure Yandex Advertisement Network
        feed.configure_ad_yandex('A-123', 'page-top')


        urlpatterns = [
            ...
            path('turbo/', feed),
            ...
        ]


    """
    feed_type = YandexTurboFeedType

    def __init__(self):
        super(YandexTurboFeed, self).__init__()
        self.analytics = []
        self.ads = []

        # Django < 1.10 has obfuscated __get_dynamic_attr
        if not hasattr(self, '_get_dynamic_attr'):
            self._get_dynamic_attr = getattr(self, '_Feed__get_dynamic_attr')

    def configure_ad_yandex(self, ident, turbo_id=''):
        """Configure Yandex Advertisement Network.

        :param str|unicode ident: Ad ID.

        :param str|unicode turbo_id: ID of a place (figure) on Turbo page where to put an Ad block.

        """
        self.ads.append({
            'type': 'Yandex',
            'id': ident,
            'turbo-ad-id': turbo_id,
        })

    def configure_analytics_yandex(self, ident, params=None):
        """Configure Yandex Metrika analytics counter.

        :param str|unicode ident: Metrika counter ID.

        :param dict params: Additional params.

        """
        params = params or {}

        data = {
            'type': 'Yandex',
            'id': ident,
        }

        if params:
            data['params'] = '%s' % params

        self.analytics.append(data)

    def configure_analytics_google(self, ident):
        """Configure Google Analytics counter.

        :param str|unicode ident: Counter ID.

        """
        self.analytics.append({
            'type': 'Google',
            'id': ident,
        })

    def item_turbo(self, item):
        """This can be overridden to set turbo contents.

        :param item:

        :rtype: str|unicode

        """
        # todo maybe automatic html transform, e.g. with bleach
        return self.item_description(item)

    def item_extra_kwargs(self, item):
        kwargs = super(YandexTurboFeed, self).item_extra_kwargs(item)
        kwargs['ya_contents'] = self._get_dynamic_attr('item_turbo', item)
        return kwargs

    def feed_extra_kwargs(self, obj):
        kwargs = super(YandexTurboFeed, self).feed_extra_kwargs(obj)

        kwargs.update({
            'ya_analytics': self.analytics,
            'ya_ads': self.ads,
        })

        return kwargs
