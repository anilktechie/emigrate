#
import logging

from emigrate import Migration


class MigrationActor(object):
    class Direction(object):
        UP   = 1
        DOWN = 2

    def __init__(self, dbClient):
        self._dbClient = dbClient
        self.__log = logging.getLogger("emigrate")

    def makeMigrate(self, migrationCls, direction):
        """ Make migration
        :type migrationCls: Migration
        :type direction: Direction
        :rtype: bool
        """
        assert issubclass(migrationCls, Migration)  # WARNING - subclass is not check that is it instance
        # Step 1. Create migration instance
        migrationInst = migrationCls(dbClient=self._dbClient)
        # Step 2. Make migration
        if direction == MigrationActor.Direction.UP:
            migrationInst.up()
        elif direction == MigrationActor.Direction.DOWN:
            migrationInst.down()
        else:
            raise ValueError("Wrong direction.")
