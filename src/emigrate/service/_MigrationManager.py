#

from __future__ import absolute_import

from logging import getLogger


class MigrationManager(object):
    def __init__(self, context):
        self.__log = getLogger('emigrate.service.migration_manager')
        self._context = context


    def restore_migrations(self, path):
        self.__log.info("Restore migration: path = {path!r}".format(path=path))
