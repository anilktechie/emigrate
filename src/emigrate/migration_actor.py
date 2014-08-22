#
import logging


class MigrationActor(object):
    class Direction(object):
        UP   = 1
        DOWN = 2

    def __init__(self, dbClient):
        self._dbClient = dbClient
        self.__log = logging.getLogger("emigrate.MigrationActor")

    def _migrate(self, migration_cls, op, cb=None):
        """
        :type migration_cls: type
        :type op: int
        :type cb: callable
        :rtype: bool
        """
        result = None
        #if isi
        inst = migration_cls(self._dbClient)
        if callable(cb):
            cb(migration=inst, op=op)
        if op == MigrationActor.Direction.UP:
            inst.up()
        elif op == MigrationActor.Direction.DOWN:
            inst.down()
        else:
            raise Exception("Unknown operation.")
        return result

    def migrate(self, operation, step=None, cb=None):
        if operation == MigrationDispatcher.Operation.UP:
            self._migrate_up(step, cb=cb)
        elif operation == MigrationDispatcher.Operation.DOWN:
            self._migrate_down(step, cb=cb)
        else:
            raise Exception("Not yet implemented")
