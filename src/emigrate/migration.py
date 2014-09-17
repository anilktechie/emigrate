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

    def dropTable(self, tableName, ifExists=True):
        # Step 0. Check contract
        assert isinstance(tableName, (str, unicode))
        assert isinstance(ifExists, bool)
        #
        if ifExists is True:
            query = "DROP TABLE IF EXISTS `{tableName}`".format(tableName=tableName)
        else:
            query = "DROP TABLE `{tableName}`".format(tableName=tableName)
        self._execute(query)

    def dropTrigger(self, triggerName, ifExists=True):
        assert isinstance(triggerName, (str, unicode))
        assert isinstance(ifExists, bool)
        #
        if ifExists is True:
            query = "DROP TRIGGER IF EXISTS `{triggerName}`".format(triggerName=triggerName)
        else:
            query = "DROP TRIGGER `{triggerName}`".format(triggerName=triggerName)
        self._execute(query)

    def _execute(self, query, params=None):
        self._dbClient.execute(query, params)

    def getVersion(self):
        result = None
        col_name = "version"
        query = "SELECT VERSION() AS `{col_name}`".format(col_name=col_name)
        rows = self._query(query, named_tuple=True)
        for row in rows:
            item = dict(row)
            result = str(item.get(col_name))
        return result

    def getVariables(self):
        result = {}
        query = "SHOW VARIABLES"
        rows = self._query(query, named_tuple=True)
        for row in rows:
            item = dict(row)
            name = str(item.get("Variable_name"))
            value = str(item.get("Value"))
            result[name] = value
        return result

    def _query(self, query, params=None, named_tuple=False):
        return self._dbClient.query(query, params, named_tuple)

    def _debug(self, *args, **kwargs):
        pass

    def _warn(self, *args, **kwargs):
        pass

    def _error(self, *args, **kwargs):
        pass

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

