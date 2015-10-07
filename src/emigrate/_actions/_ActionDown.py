#
import sys
import logging

from emigrate import BaseAction, MigrationActor, MigrationLoader


class ActionDown(BaseAction):
    HELP = "downgrade migration operation"

    def __init__(self, app):
        BaseAction.__init__(self, app)
        self.__log = logging.getLogger("emigrate.actions.down")

    def run(self):
        migrationPath = self.migrationPath()
        migrationLoader = MigrationLoader(migrationPath)
        migrations = migrationLoader.search()
        #
        migrations.sort(key=lambda item: getattr(item, "__module__"), reverse=True)
        #
        dbClient = self.createDatabaseClient(autoConnect=True)
        #
        migrationActor = MigrationActor(dbClient=dbClient)
        for migration in migrations:
            migrationName = getattr(migration, "__module__", "")
            sys.stdout.write("Reject migration %s ...\n" % (migrationName, ))
            migrationActor.makeMigrate(migrationCls=migration, direction=MigrationActor.Direction.DOWN)
        #
        dbClient.close()
