#
import sys
import logging

from app_base import ApplicationCommand

from migration_actor import MigrationActor
from migration_loader import MigrationLoader


class ApplicationCommandUp(ApplicationCommand):

    def __init__(self, app):
        ApplicationCommand.__init__(self, app)
        self.__log = logging.getLogger("emigrate.up")

    def _migrationProcess(self, migration):
        migrationName = migration.getName()
        sys.stdout.write("Migration up %s..." % (migrationName, ))

    def run(self):
        migrationLoader = MigrationLoader(".migration")
        migrations = migrationLoader.search()
        dbClient = self.createDatabaseClient(autoConnect=True)
        #
        migrationActor = MigrationActor(dbClient=dbClient)
        for migration in migrations:
            migrationActor.makeMigrate(migration=migration, direction=MigrationActor.Direction.UP, cb=self._migrationProcess)
        #
        dbClient.close()
