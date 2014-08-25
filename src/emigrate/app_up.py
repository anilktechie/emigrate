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

    def run(self):
        migrationLoader = MigrationLoader(".migration")
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
