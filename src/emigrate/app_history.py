#
import sys
import logging
import datetime

from app_base import ApplicationCommand


class ApplicationCommandHistory(ApplicationCommand):
    def __init__(self, app):
        ApplicationCommand.__init__(self, app)
        #
        self.__log = logging.getLogger("emigrate.history")

    def run(self):
        dbClient = self.createDatabaseClient(autoConnect=True)
        query = "SELECT * FROM `emigrate_log` ORDER BY `id` DESC LIMIT %(limit)s"
        params = {
            "limit": 100
        }
        #
        sys.stdout.write(" %20s %s\n" % ("Date", "Name", ))
        rows = dbClient.query(query, params)
        for row in rows:
            currentDateTime = row.get("date")
            migrationName = row.get("name")
            myDateTime = ""
            if isinstance(currentDateTime, datetime.datetime):
                myDateTime = currentDateTime.strftime("Y-m-d H:i:s")
            sys.stdout.write(" %20s %s\n" % (myDateTime, migrationName))
