#

from __future__ import absolute_import

import os
import imp
import inspect
import logging


class MigrationLoader(object):

    def __init__(self, base_path, class_prefix="Migration_"):
        self._base_path = base_path
        self._class_prefix = class_prefix
        self.__log = logging.getLogger("emigrate.MigrationLoader")


    def _search_modules(self):
        result = []
        items = os.listdir(self._base_path)
        items.sort()
        for item in items:
            mod_name, file_ext = os.path.splitext(os.path.split(item)[-1])
            if file_ext.lower() == '.py':
                path = os.path.join(self._base_path, item)
                migration = imp.load_source(mod_name, path)
                result.append(migration)
        return result


    def _search_classes(self):
        result = []
        modules = self._search_modules()
        for module in modules:
            items = dir(module)
            for item in items:
                self.__log.debug("item = %r", item)
                if item.startswith(self._class_prefix):
                    attr = getattr(module, item)
                    if inspect.isclass(attr):
                        self.__log.debug("item is class = %r", attr)
                        result.append(attr)
        return result


    def search(self):
        classes = self._search_classes()
        return classes


    def discover(self):
        migrationPath = self.migrationPath()
        migrationLoader = MigrationLoader(migrationPath)
        migrations = migrationLoader.search()
        for migration in migrations:
            #
            name = str(getattr(migration, "__module__", ""))
            docs = str(getattr(migration, "__doc__", ""))
            doc_lines = docs.split("\n")
            #
            short_doc = ""
            for doc_line in doc_lines:
                doc_line = doc_line.strip()
                short_doc = doc_line
                break
            #
