#

from __future__ import absolute_import

from .._BaseAction import BaseAction


class ActionList(BaseAction):
    NAME = "list"
    DESC = "show all assets migrations (list all migrations)"


    def run(self):

        # Step 1. Search migrations
        ml = self._context.migration_loader
        migrations = ml.discover()

        # Step 2 Show migrations
        for migration in migrations:
            row = "| {migrationName:<20s} | {migrationDesc:<20s} | {migrationStatus:<20s} |\n".format(migrationName=name, migrationDesc=short_doc, migrationStatus="???")
            self.report(row)
