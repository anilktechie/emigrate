#

from __future__ import absolute_import

from logging import getLogger


class MigrationRegistryManager(object):

    def __init__(self, context):
        self.__log = getLogger('emigrate.migration_registry_manager')
        self._context = context


    def create_migration_registry_scheme(self):
        """ Create new migration scheme
        """
        conn = self.createDatabaseClient(autoConnect=True)
        query = "CREATE DATABASE `{db}`".format(db=db) # TODO - implement also parameters `CHARACTER SET` and `COLLATE` ...
        conn.execute(query)
        conn.close()


    def get_database_generation_history(self):
        """ Return database generation history
        """
        conn = self._context.search_connection('default')
        try:
            conn.begin()
            query = "SELECT * FROM `emigrate_log` ORDER BY `id` DESC"
            params = {}

            conn.query(query, params)

            conn.commit()
        except Exception as err:
            self.__log.exception(err)
        finally:
            conn.rollback()

        # Show migrations
        #rows = dbClient.query(query, params)
        #for row in rows:
        #    currentDateTime = row.get("date")
        #    migrationName = row.get("name")
        #    myDateTime = ""
        #    if isinstance(currentDateTime, datetime.datetime):
        #        myDateTime = currentDateTime.strftime("Y-m-d H:i:s")
        #    sys.stdout.write(" %20s %s\n" % (myDateTime, migrationName))
