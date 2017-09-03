#

from __future__ import absolute_import

from sys import stdout

import os
import logging


class BaseAction(object):
    def __init__(self, context):
        """
        :type app: Application
        """
        self.__log = logging.getLogger('emigrate.actions')
        self._context = context


    def report(self, msg, error=False):
        """ Report message
        """
        stdout.write("{msg}\n".format(msg=msg))


    def migrationPath(self):
        base_path = os.getcwd()
        migration_path = os.path.join(base_path, ".migration")
        #
        self.__log.info("Migration search directory: {migration_path!r}".format(migration_path=migration_path))
        #
        if not os.path.isdir(migration_path):
            raise RuntimeError("No migration directory exists.")
        #
        return migration_path


    def createDatabaseClient(self, autoConnect=False):
        result = MySQLClient(self._app._params)
        if autoConnect is True:
            result.makeConnect()
        return result


    def run(self):
        raise NotImplementedError()
