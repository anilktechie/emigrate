#
import sys

import mysql.connector
from mysql.connector import errorcode


class DatabaseClient(object):
    def __init__(self, params):
        self._params = params
        self._cnx = None

    def makeConnect(self, raiseOnWarnings=True):
        kwargs = {
            "host": self._params.get("host", '127.0.0.1'),
            "database": self._params.get("database", "test"),
            "user": self._params.get("user", "root"),
            "password": self._params.get("password", ""),
        }
        #
        if raiseOnWarnings:
            kwargs['raise_on_warnings'] = True
        #
        try:
            self._cnx = mysql.connector.connect(**kwargs)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                sys.stderr.write("Database does not exists... create here...\n")
            else:
                raise err

    def close(self):
        if self._cnx is not None:
            self._cnx.close()
            self._cnx = None

    def execute(self, query, params):
        dbCursor = self._cnx.cursor()
        dbCursor.close()

    def query(self, query, params):
        """
        """
        assert(self._cnx, )
        result = []
        dbCursor = self._cnx.cursor()
        dbCursor.close()
        return result

    def showTables(self):
        result = []
        query = "SHOW TABLES"
        params = {}
        rows = self.query(query, params)
        return result
