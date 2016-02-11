#

import sys

from emigrate import BaseAction


class ActionInfo(BaseAction):
    NAME = "info"
    DESC = "migrator information"


    def run(self):
        settings = self.app.settings
        #
        items = []
        items.append("Host: {host!r}".format(host=settings.get('host')))
        items.append("Password: {password!r}".format(password=settings.get('password')))
        items.append("User: {user!r}".format(user=settings.get('user')))
        items.append("Port: {port!r}".format(port=settings.get('port')))
        items.append("Database: {database!r}".format(database=settings.get('database')))
        items.append("")
        #
        sys.stdout.write("\n".join(items))
