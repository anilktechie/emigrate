#!/usr/bin/python

import os
import sys
import time

from twisted.enterprise import adbapi
from twisted.internet import reactor


class Application(object):
    def __init__(self, database=None):
        self._dbpool = adbapi.ConnectionPool("mysql.connector", database='', host='', port=3306, user="root", password='')
        self._result = 0
        self._table_count = None

    def _query(self, query, params):
       """
       :rtype: Future<ResultSet<HasMap<String, Object>>>
       """
       return self._dbpool.runQuery(query, params)

    def _showCreateTableResult(self, rows, table_name):
        #print table_name
        for row in rows:
            (table_name, text) = row
            print("%s;\n\n" % text)
        # Step 2. Done
        self._table_count -= 1
        if self._table_count == 0:
            reactor.stop()

    def _showTablesResult(self, rows):
        self._table_count = len(rows)
        for row in rows:
            (table_name, ) = row
            #print("Dump %s..." % table_name)
            self.showCreateTable(table_name)

    def showTables(self):
        query = "SHOW TABLES";
        params = ()
        return self._query(query, params).addCallback(self._showTablesResult)

    def showCreateTable(self, table_name):
        query = "SHOW CREATE TABLE `%s`" % table_name;
        params = ()
        return self._query(query, params).addCallback(self._showCreateTableResult, table_name)

    def _internalError(self, reason):
        reactor.stop()

    def _restoreMigration(self):
        # Step 1. Reading migration
        currentDirectory = os.getcwd()
        currentMigrationsDirectory = os.path.join(currentDirectory, ".migrations")
        migrationNameList = os.listdir(currentMigrationsDirectory)
        migrationNameList = sort(migrationNameList) # TODO - check sorting ...
        for migrationName in migrationNameList:
        
        self.showTables()

    def run(self):
        reactor.callLater(0.0, self._restoreMigration)
        reactor.run()
        return self._result


def main():
    app = Application()
    app.run()


if __name__ == "__main__":
    sys.exit(main())