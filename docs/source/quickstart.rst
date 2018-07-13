Quickstart
==========


1. Inherit your feed class from **YandexTurboFeed**:

.. code-block:: python

    # feeds.py
    from yaturbo import YandexTurboFeed

    class TurboFeed(YandexTurboFeed):
        """
        More information on Django Syndication Feed Framework configuration:
        https://docs.djangoproject.com/en/2.0/ref/contrib/syndication/
        """

        turbo_sanitize = True  # Let's strip HTML tags unsupported by Turbo pages.

        def item_turbo(self, item):
            # By default Turbo contents is taken from `item_description`.
            # Here we take turbo page contents from `html` attribute of an item.
            # Since we have `turbo_sanitize = True`, our HTML will be sanitized
            # automatically.
            #
            # Take a note, that if we return falsy item would be considered
            # as not having turbo contents at all.
            #
            return item.get('html', '')

           # You can also override other item_turbo_* family members.


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

