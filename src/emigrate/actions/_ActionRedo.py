#

from __future__ import absolute_import

from .._BaseAction import BaseAction


class ActionRedo(BaseAction):
    NAME = "redo"
    DESC = "redo migration operation (when previous is with exception)"

    def run(self):
        migrationLoader = MigrationLoader(".migration")
        migrations = migrationLoader.search()
        dbClient = self.createDatabaseClient(autoConnect=True)
        migrationActor = MigrationActor(dbClient=dbClient)
