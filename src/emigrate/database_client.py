class DatabaseClient(object):

    def execute(self, query, params):
        pass

    def query(self, query, params):
        """
        """
        return []

    def showTables(self):
        result = []
        query = "SHOW TABLES"
        params = {}
        rows = self.query(query, params)
        return result
