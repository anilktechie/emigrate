#

from __future__ import absolute_import

from logging import getLogger


class ActionStatus(object):
    NAME = "status"
    DESC = "show update status"

    def __init__(self, context):
        self.__log = getLogger('emigrate.actions.status')
        self._context = context


    def run(self):
        """ Show difference between current registry and actual migrations
        """
        # Step 1. Read migration(s)
        migration_service = self._context.get_object('MigrationService')
        migrations = []

        # Step 2. Retreive migrations
        reg_service = self._context.get_object('RegService')
        regs = []

        # Step 3. Compare migrations
        for migration in migrations:
            for reg in regs:
                if migration.name == reg.name:
                    migration.apply = True

        # Step 4. Output migration(s)
        for migration in migrations:
            stdout.write("Migration: {name} Status: {status!r}".format(name=migration.name, status=migration.apply))
