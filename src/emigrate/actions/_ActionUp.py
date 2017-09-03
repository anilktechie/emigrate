#

from __future__ import absolute_import

import os
import sys
import logging

from .._BaseAction import BaseAction


class ActionUp(BaseAction):
    NAME = "up"
    DESC = "upgrade migration operation"

    def __init__(self, app):
        BaseAction.__init__(self, app)
        self.__log = logging.getLogger("emigrate.actions.up")

    def run(self):
        #
        migrationPath = self.migrationPath()
        migrationLoader = MigrationLoader(migrationPath)
        migrations = migrationLoader.search()
        #
        migrations.sort(key=lambda item: getattr(item, "__module__"))
        #
        dbClient = self.createDatabaseClient(autoConnect=True)
        #
        migrationActor = MigrationActor(dbClient=dbClient)
        for migration in migrations:
            migrationName = getattr(migration, "__module__", "")
            sys.stdout.write("Apply migration %s ...\n" % (migrationName, ))
            migrationActor.makeMigrate(migrationCls=migration, direction=MigrationActor.Direction.UP)
        #
        dbClient.close()
