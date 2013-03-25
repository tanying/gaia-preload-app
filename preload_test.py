#!/usr/bin/env python

import preload
import base64
import io
from urlparse import urlparse


def test_convert():
    test_data = 'fakedata'
    encode = base64.b64encode(test_data)
    result = preload.convert(test_data, 'image/png')
    assert result == 'data:image/png;base64,' + encode


def test_has_scheme():
    http_url = urlparse('http://test.com/test.png')
    absolute_path = urlparse('/test.png')
    relative_path = urlparse('test.png')
    assert preload.has_scheme(http_url) == True
    assert preload.has_scheme(absolute_path) == False
    assert preload.has_scheme(relative_path) == False


def test_get_absolute_path():
    origin = urlparse('http://test.com/path-1/path-2/')
    icon1 = urlparse('test.png')
    icon2 = urlparse('/test.png')
    icon3 = urlparse('http://test.com/path-3/test.png')
    assert preload.get_absolute_url(origin, icon1) == \
        'http://test.com/path-1/path-2/test.png'
    assert preload.get_absolute_url(origin, icon2) == \
        'http://test.com/test.png'
    assert preload.get_absolute_url(origin, icon3) == \
        'http://test.com/path-3/test.png'


def test_get_origin():
    print 'http://test.com/path/'
    print preload.get_origin('http://test.com/path/test.manifest')
    assert preload.get_origin('http://test.com/path/test.manifest') == 'http://test.com/path/'
    assert preload.get_origin('http://test.com/test.manifest') == 'http://test.com/'