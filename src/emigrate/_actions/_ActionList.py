#

import sys

from emigrate import BaseAction
from emigrate import MigrationLoader


class ActionList(BaseAction):
    NAME = "list"
    DESC = "show all assets migrations (list all migrations)"


    def run(self):
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
            sys.stdout.write("| {migrationName:<20s} | {migrationDesc:<20s} | {migrationStatus:<20s} |\n".format(migrationName=name, migrationDesc=short_doc, migrationStatus="???"))
