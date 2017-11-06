#

from __future__ import absolute_import

from os.path import abspath


class Context(object):
    def __init__(self):
        self.repository_path = abspath(".emigrate")
        self._instances = {}

    def register(self, name, instance):
        self._instances[name] = instance

    def get_object(self, name):
        return self._instances.get(name)
