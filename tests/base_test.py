# -*- coding: utf-8 -*-
"""
    test
    ~~~~
    Flask-CORS is a simple extension to Flask allowing you to support cross
    origin resource sharing (CORS) using a simple decorator.

    :copyright: (c) 2014 by Cory Dolphin.
    :license: MIT, see LICENSE for more details.
"""

try:
    import unittest2 as unittest
except ImportError:
    import unittest

try:
    # this is how you would normally import
    from flask.ext.cors import *
except:
    # support local usage without installed package
    from flask_cors import *


class FlaskCorsTestCase(unittest.TestCase):
    def iter_verbs(self, c):
        ''' A simple helper method to iterate through a range of
            HTTP Verbs and return the test_client bound instance,
            keeping writing our tests as DRY as possible.
        '''
        for verb in ['get', 'head', 'options']:
            yield getattr(c, verb)

    def iter_responses(self, path, verbs=['get', 'head', 'options'], **kwargs):
        with self.app.test_client() as c:
            for verb in verbs:
                yield getattr(c, verb.lower())(path, **kwargs)


class AppConfigTest(object):
    def setUp(self):
        self.app = None

    def tearDown(self):
        self.app = None
