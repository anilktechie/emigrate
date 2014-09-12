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

    def insert(self, tableName, values):
        """ Insert value to database
        @type tableName: str
        @type values: dict
        """
        assert isinstance(tableName, str)
        assert isinstance(values, dict)
        #
        params = {}
        #
        columnNames = []
        columnValues = []
        currentParamCount = 1
        #
        for name, value in values.items():
            #
            paramName = "param%d" % (currentParamCount, )
            currentParamCount += 1
            #
            columnNames.append( "`" + name + "`" )
            columnValues.append( "%(" + paramName + ")s" )
            #
            params[paramName] = value
        #
        query = "INSERT INTO `" + tableName + "` (" + (", ".join(columnNames)) + ") VALUES ("  + (", ".join(columnValues)) + ")"
        print("Execute: %r with %r" % (query, params, ))
        self._execute(query, params)

    def drop(self, tableName):
        assert isinstance(tableName, (str, unicode))
        #self.__log.debug("Drop table " + tableName + "...")
        query = "DROP TABLE " + "`" + tableName + "`"
        self._execute(query)

    def dropIfExists(self, tableName):
        assert isinstance(tableName, (str, unicode))
        #self.__log.debug("Drop table " + tableName + "...")
        query = "DROP TABLE IF EXISTS " + "`" + tableName + "`"
        self._execute(query)

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


if __name__ == "__main__":
    class Migration1(Migration):
        def up(self):
            pass
        def down(self):
            pass 
    conn = None
    m = Migration1(conn)
    m.insert("abc", {"name": "Vitold S", "id": 1, "value": "132.23"})

