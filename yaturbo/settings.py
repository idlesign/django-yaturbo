# -*- encoding: utf-8 -*-
from __future__ import unicode_literals


TURBO_ALLOWED_TAGS = [
    'header',
    'figure',
    'figcaption',
    'menu',
    'a',
    'img',
    'h1',
    'h2',
    'p',
    'br',
    'hr',
    'ol',
    'ul',
    'li',
    'strong',
    'i',
    'em',
    'sup',
    'sub',
    'ins',
    'del',
    'small',
    'big',
    'pre',
    'abbr',
    'u',
    'div',
    'video',
    'source',
    'blockquote',
    'table',
    'tr',
    'th',
    'td',
    'meta',
    'form',
    'button',
]

TURBO_ALLOWED_ATTRS = {
    'a': [
        'href',
    ],
    'abbr': [
        'title',
    ],
    'img': [
        'src',
    ],
    'source': [
        'src',
        'type',
    ],
    'figure': [
        'data-turbo-ad-id',
    ],
    'div': [
        'data-block',
        'data-view',
        'data-item-view',
        'data-network',
        'data-author',
        'data-avatar-url',
        'data-title',
        'data-subtitle',
        'data-expanded',
        'data-url',
        'data-send-to',
        'data-agreement-company',
        'data-agreement-link',
        'data-stick',
        'data-type',
        'itemscope',
        'itemtype',
    ],
    'table': [
        'data-invisible',
    ],
    'meta': [
        'itemprop',
        'content',
    ],
    'form': [
        'data-type',
        'data-send-to',
        'data-agreement-company',
        'data-agreement-link',

    ],
    'button': [
        'formaction',
        'data-background-color',
        'data-color',
        'data-primary',
        'disabled',
    ],
}
