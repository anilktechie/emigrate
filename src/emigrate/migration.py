#
from abc import ABCMeta, abstractmethod

from database_client import DatabaseClient


class Migration(object):
    __metaclass__ = ABCMeta

    def __init__(self, dbClient):
        """
        :type dbClient: DatabaseClient
        """
        isinstance(dbClient, DatabaseClient)
        self._dbClient = dbClient

    def _execute(self, query, params):
        self._dbClient.execute(query, params)

    def _query(self, query, params):
        return self._dbClient.query(query, params)

    @abstractmethod
    def up(self):
        pass

    @abstractmethod
    def down(self):
        pass
