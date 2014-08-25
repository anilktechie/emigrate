#
import sys

from app_base import ApplicationCommand

from migration_loader import MigrationLoader


class ApplicationCommandNew(ApplicationCommand):
    def run(self):
        migrationLoader = MigrationLoader(".migration")
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
            sys.stdout.write("%-20s - %-20s\n" % (name, short_doc))
