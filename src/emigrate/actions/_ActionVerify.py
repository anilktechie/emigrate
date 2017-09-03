#

from __future__ import absolute_import

import sys
import logging
import datetime

from .._BaseAction import BaseAction


class ActionVerify(BaseAction):
    NAME = "verify"
    DESC = "verify and show status about each migration"


    def run(self):
        """ Show migrations
        """
        # Step 1. Search current database generation
        mrm = self._context.migration_registry_manager
        generation_history = mrm.get_database_generation_history()

        # Step 2. Search actual migrations
        ml = self._context.migration_loader
        migrations = ml.discover()

        # Step 3. Show differences
        for migration in migrations:
            print(migration)
