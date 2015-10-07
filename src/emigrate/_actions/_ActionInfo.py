#

import sys

from emigrate import BaseAction


class ActionInfo(BaseAction):
    HELP = "migrator information"

    def __init__(self, app):
        BaseAction.__init__(self, app)
        self.__app = app

    def run(self):
        params = self.__app._params
        #
        items = []
        items.append("Host: {host!r}".format(host=params.get('host')))
        items.append("Password: {password!r}".format(password=params.get('password')))
        items.append("User: {user!r}".format(user=params.get('user')))
        items.append("Port: {port!r}".format(port=params.get('port')))
        items.append("Database: {database!r}".format(database=params.get('database')))
        items.append("")
        #
        sys.stdout.write("\n".join(items))
