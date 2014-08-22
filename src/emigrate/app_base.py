#
from abc import ABCMeta, abstractmethod


class ApplicationCommand(object):
    __metaclass__ = ABCMeta

    def __init__(self, app):
        self._app = app

    @abstractmethod
    def run(self):
        pass
