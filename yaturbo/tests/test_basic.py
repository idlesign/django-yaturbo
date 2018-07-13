# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from yaturbo import YandexTurboFeed


class MyFeed(YandexTurboFeed):

    title = 'title'
    link = '/here/'
    description = 'descr'

    turbo_sanitize = True

    def __init__(self, items):
        super(MyFeed, self).__init__()
        self.items = items

    def item_title(self, item):
        return item['title']

    def item_description(self, item):
        return item['descr']

    def item_link(self, item):
        return item['link']

    def item_turbo_source(self, item):
        return item.get('source')

    def item_turbo_topic(self, item):
        return item.get('topic')


class MyFeedDefaults(YandexTurboFeed):

    title = 'title1'
    link = '/there/'
    description = 'descr'

    def __init__(self, items):
        super(MyFeedDefaults, self).__init__()
        self.items = items

    def item_title(self, item):
        return item['title']

    def item_description(self, item):
        return item['descr']

    def item_link(self, item):
        return item['link']


def test_feed(request_get):

    feed = MyFeed([
        {
            'title': 'a',
            'descr': 'turbo!',
            'link': 'd',
            'source': 'http://some.com',
            'topic': 'Title',
        },
        {
            'title': 'b',
            'descr': '<span><div data-x="y">sanitized</div></span>',
            'link': 'link_b',
        }
    ])

    feed.configure_ad_yandex('A-123', 'page-top')
    feed.configure_ad_yandex('B-123', 'page-bottom')

    feed.configure_analytics_yandex('12345', params={'key': 'value'})
    feed.configure_analytics_google('7890')

    content = feed(request_get('/')).content.decode('utf-8')

    chunks = [
        'xmlns:turbo="http://turbo.yandex.ru"',
        'xmlns:yandex="http://news.yandex.ru"',
        'turbo:analytics',
        'id="12345"',
        'id="7890"',
        'turbo:adNetwork',
        'id="A-123"',
        'turbo-ad-id="page-top"',
        'id="B-123"',
        'turbo-ad-id="page-bottom"',
        'item turbo="true"',
        '<turbo:content><![CDATA[turbo!]]></turbo:content>',
        '<turbo:source>http://some.com</turbo:source>',
        '<turbo:topic>Title</turbo:topic>',
        '<turbo:content><![CDATA[<div>sanitized</div>]]></turbo:content>',
    ]

    for chunk in chunks:
        assert chunk in content


def test_noturbo(request_get):

    feed = MyFeedDefaults([
        {
            'title': 'a',
            'descr': '',
            'link': 'd',
        }
    ])

    content = feed(request_get('/')).content.decode('utf-8')

    assert 'turbo="true"' not in content
