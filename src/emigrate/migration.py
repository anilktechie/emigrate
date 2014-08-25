#
from abc import ABCMeta, abstractmethod

from database_client import DatabaseClient
from emigrate.database_transaction import DatabaseClientTransaction


class Migration(object):
    __metaclass__ = ABCMeta

    def __init__(self, dbClient):
        """
        :type dbClient: DatabaseClient
        """
        isinstance(dbClient, DatabaseClient)
        self._dbClient = dbClient

    def _execute(self, query, params=None):
        self._dbClient.execute(query, params)

    def _query(self, query, params=None):
        return self._dbClient.query(query, params)

    def createTransaction(self):
        return DatabaseClientTransaction(dbClient=self._dbClient)

    def dropTable(self, tableName):
        query = "DROP TABLE `" + tableName + "`"
        self._execute(query)

    @abstractmethod
    def up(self):
        pass

    @abstractmethod
    def down(self):
        pass
