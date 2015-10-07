#

import sys
import logging
import datetime

from emigrate import BaseAction


class ActionStatus(BaseAction):
    HELP = "show migration status"

    def __init__(self, app):
        BaseAction.__init__(self, app)
        #
        self.__log = logging.getLogger("emigrate.actions.status")

    def run(self):
        dbClient = self.createDatabaseClient(autoConnect=True)
        query = "SELECT * FROM `emigrate_log` ORDER BY `id` DESC LIMIT %(limit)s"
        params = {
            "limit": 100
        }
        # Show headerws
        sys.stdout.write(" %20s %s\n" % ("Date", "Name", ))
        # Show migrations
        rows = dbClient.query(query, params)
        for row in rows:
            currentDateTime = row.get("date")
            migrationName = row.get("name")
            myDateTime = ""
            if isinstance(currentDateTime, datetime.datetime):
                myDateTime = currentDateTime.strftime("Y-m-d H:i:s")
            sys.stdout.write(" %20s %s\n" % (myDateTime, migrationName))
