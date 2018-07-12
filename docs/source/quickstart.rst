Quickstart
==========


1. Inherit your feed class from **YandexTurboFeed**:

.. code-block:: python

    # feeds.py
    from yaturbo.toolbox import YandexTurboFeed

    class TurboFeed(YandexTurboFeed):
        """
        More information on Django Syndication Feed Framework configuration:
        https://docs.djangoproject.com/en/2.0/ref/contrib/syndication/
        """

        def item_turbo(self, item):
            # By default Turbo contents is taken from `item_description`.
            # Here we take turbo page contents from `turbo` attribute of an item.
            #
            # Take a note, that if we return falsy item would be considered
            # as not having turbo contents at all.
            #
            return item.get('turbo', '')


2. Pass an instantiated (and optionally configured) feed object to `urlpatterns`:

.. code-block:: python

    # urls.py
    from .feeds import TurboFeed

    feed = TurboFeed()

    # configure Yandex Metrika counter
    feed.configure_analytics_yandex('123456789')

    # configure Yandex Advertisement Network
    feed.configure_ad_yandex('A-123', 'page-top')

    urlpatterns = [
        ...
        path('feeds/turbo/', feed),
        ...
    ]

