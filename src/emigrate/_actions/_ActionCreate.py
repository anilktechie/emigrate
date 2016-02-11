#

import sys

from emigrate import BaseAction


class ActionCreate(BaseAction):
    NAME = "create"
    DESC = "create database"


    def createDatabase(self, db):
        conn = self.createDatabaseClient(autoConnect=True)
        query = "CREATE DATABASE `{db}`".format(db=db) # TODO - implement also parameters `CHARACTER SET` and `COLLATE` ...
        conn.execute(query)
        conn.close()


    def run(self):
        """ Create database
        """
        db = self.app.settings.get('db')
        if not isinstance(db, str):
            db = ""
        #
        sys.stdout.write("==> Create database {db!r}...\n".format(db=db))
        #
        if db == "":
            sys.stderr.write("error: can not setup database name.\n")
        else:
            self.createDatabase(db)
