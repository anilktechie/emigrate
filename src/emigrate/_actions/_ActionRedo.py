#

from emigrate import BaseAction


class ActionRedo(BaseAction):
    NAME = "redo"
    DESC = "redo migration operation (when previous is with exception)"

    def run(self):
        migrationLoader = MigrationLoader(".migration")
        migrations = migrationLoader.search()
        dbClient = self.createDatabaseClient(autoConnect=True)
        migrationActor = MigrationActor(dbClient=dbClient)
