#

from __future__ import absolute_import

from os.path import abspath


class Context(object):
    def __init__(self, app=None):
        self.app = app
        self.repository_path = abspath(".emigrate")
