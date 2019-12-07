django-yaturbo
==============
https://github.com/idlesign/django-yaturbo

.. image:: https://idlesign.github.io/lbc/py2-lbc.svg
   :target: https://idlesign.github.io/lbc/
   :alt: LBC Python 2

----

|release| |lic| |ci| |coverage|

.. |release| image:: https://img.shields.io/pypi/v/django-yaturbo.svg
    :target: https://pypi.python.org/pypi/django-yaturbo

.. |lic| image:: https://img.shields.io/pypi/l/django-yaturbo.svg
    :target: https://pypi.python.org/pypi/django-yaturbo

.. |ci| image:: https://img.shields.io/travis/idlesign/django-yaturbo/master.svg
    :target: https://travis-ci.org/idlesign/django-yaturbo

.. |coverage| image:: https://img.shields.io/coveralls/idlesign/django-yaturbo/master.svg
    :target: https://coveralls.io/r/idlesign/django-yaturbo


Description
-----------

*Reusable Django app to enable Yandex Turbo Pages for your site*

This app allows you to define Yandex Turbo pages feeds in term similar to those
of Django Syndication Feed Framework contrib:

1. Inherit your feed class from **YandexTurboFeed**:

.. code-block:: python

    # feeds.py
    from yaturbo import YandexTurboFeed

    class TurboFeed(YandexTurboFeed):
        """
        More information on Django Syndication Feed Framework configuration:
        https://docs.djangoproject.com/en/2.0/ref/contrib/syndication/
        """

2. Pass an instantiated (and optionally configured) feed object to `urlpatterns`:

.. code-block:: python

    # urls.py
    from .feeds import TurboFeed

    urlpatterns = [
        ...
        path('feeds/turbo/', TurboFeed()),
        ...
    ]


Read the docs for further information.


Documentation
-------------

http://django-yaturbo.readthedocs.org/
