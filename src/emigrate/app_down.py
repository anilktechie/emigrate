#
import logging
from app_base import ApplicationCommand

from migration_actor import MigrationActor
from migration_loader import MigrationLoader


class ApplicationCommandDown(ApplicationCommand):
    def __init__(self, app):
        ApplicationCommand.__init__(self, app)
        self.__log = logging.getLogger("emigrate.down")

    def run(self):
        migrationLoader = MigrationLoader(".migration")
        migrations = migrationLoader.search()
        #
        dbClient = self.createDatabaseClient()
        #
        try:
            migrationActor = MigrationActor(dbClient=dbClient)
            migrationActor.migrate(MigrationActor.Direction.DOWN, cb=self._show_progress)
        except Exception as err:
            self.__log.exception(err)
        finally:
            dbClient.close()
