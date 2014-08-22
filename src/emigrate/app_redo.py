#
from app_base import ApplicationCommand

from migration_actor import MigrationActor
from migration_loader import MigrationLoader


class ApplicationCommandRedo(ApplicationCommand):
    def run(self):
        migrationLoader = MigrationLoader(".migration")
        migrations = migrationLoader.search()
        dbClient = self.createDatabaseClient(autoConnect=True)
        migrationActor = MigrationActor(dbClient=dbClient)

        #migrationActor
