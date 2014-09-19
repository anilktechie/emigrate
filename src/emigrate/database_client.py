#
import sys

import mysql.connector
from mysql.connector import errorcode


class DatabaseClient(object):
    def __init__(self, params):
        self._params = params
        self._cnx = None

    def makeConnect(self):
        # Step 1. Prepare connection params
        kwargs = {
            "host": self._params.get("host", '127.0.0.1'),
            "user": self._params.get("user", "root"),
            "password": self._params.get("password", ""),
            "raise_on_warnings": self._params.get("raise_on_warnings", False),
            "charset": self._params.get("charset", "utf8"),
            "autocommit": self._params.get("autocommit", True),
        }
        # Step 2. Create connection
        try:
            self._cnx = mysql.connector.connect(**kwargs)
        except mysql.connector.Error as err:
            raise err
        # Step 3. Select database
        dbName = self._params.get("database", "test")
        self.selectDatabase(dbName, withCreate=True)

    def selectDatabase(self, dbName, withCreate):
        assert isinstance(withCreate, bool)
        if withCreate is True:
            # Step 1. Create database
            self.createDatabase(dbName, ifNotExists=True)
        # Step 2. Select this database
        query = "USE `{dbName}`".format(dbName=dbName)
        self.execute(query)

    def createDatabase(self, dbName, charset="utf8", collation="utf8_general_ci", ifNotExists=False):
        assert isinstance(ifNotExists, bool)
        if ifNotExists is True:
            query = "CREATE DATABASE IF NOT EXISTS `{dbName}` CHARACTER SET {charset} COLLATE {collation}".format(dbName=dbName, charset=charset, collation=collation)
        else:
            query = "CREATE DATABASE `{dbName}` CHARACTER SET {charset} COLLATE {collation}".format(dbName=dbName, charset=charset, collation=collation)
        self.execute(query)

    def dropDatabase(self, dbName, ifExists=False):
        assert isinstance(ifExists, bool)
        #
        if ifExists is True:
            query = "DROP DATABASE IF EXISTS `{dbName}`".format(dbName=dbName)
        else:
            query = "DROP DATABASE `{dbName}`".format(dbName=dbName)
        self.execute(query)

    def close(self):
        if self._cnx is not None:
            self._cnx.close()
            self._cnx = None

    def execute(self, query, params=None):
        dbCursor = self._cnx.cursor()
        if params is None:
            dbCursor.execute(query)
        else:
            dbCursor.execute(query, params)
        dbCursor.close()

    def commit(self):
        self._cnx.commit()

    def rollback(self):
        self._cnx.rollback()

    def query(self, query, params=None, named_tuple=False):
        """
        """
        result = []
        # Step 1. Create cursor
        dbCursor = self._cnx.cursor()
        # Step 2. Create request
        if params is None:
            dbCursor.execute(query)
        else:
            dbCursor.execute(query, params)
        # Step 3. Loading result
        column_names = dbCursor.column_names
        for row in dbCursor:
            if named_tuple is True:
                row = zip(column_names, row)
            result.append(row)
        # Step 4. Close cursor
        dbCursor.close()
        #
        return result

    def showTables(self):
        result = []
        query = "SHOW TABLES"
        params = {}
        rows = self.query(query, params)
        return result
