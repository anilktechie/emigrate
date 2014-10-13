#
from abc import ABCMeta, abstractmethod

from database_client import DatabaseClient


class ApplicationCommand(object):
    __metaclass__ = ABCMeta

    def __init__(self, app):
        """
        :type app: Application
        """
        self._app = app
        
    def getApplication(self):
        """
        :rtype app: Application
        """
        return self._app

    def createDatabaseClient(self, autoConnect=False):
        result = DatabaseClient(self._app._params)
        if autoConnect:
            result.makeConnect()
        return result

    @abstractmethod
    def run(self):
        pass
