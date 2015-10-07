#


class MySQLTransaction(object):

    def __init__(self, dbClient):
        self._dbClient = dbClient
        self._progress = True
        self._operationCount = 0

    def _execute(self, query, params=None):
        self._dbClient.execute(query, params)

    def _query(self, query, params=None):
        return self._dbClient.query(query, params)

    def insert(self, tableName, values):
        """ Insert new record in database
        :type name:  str
        :type vals: dict
        :rtype:
        """
        assert self._progress == True
        assert isinstance(values, dict)
        # Step 1. Prepare name & value
        cols = []
        placeHolder = []
        vals = []
        for name, value in values.items():
            cols.append("`" + name + "`")
            vals.append(value)
            placeHolder.append("%s")
        #
        cols_str = ",".join(cols)
        placeHolder_str = ",".join(placeHolder)
        #
        query = "INSERT INTO `" + tableName + "` (" + cols_str + ") VALUES (" + placeHolder_str + ")"
        params = vals
        #
        print("Query %s with params %r" % (query, params))
        #
        self._operationCount += 1
        #
        self._execute(query, params)

    def rollback(self):
        """ Commit transaction
        :rtype:
        """
        # Step 1. Commit changes
        if self._dbClient is not None:
            self._dbClient.rollback()
            self._dbClient = None
        # Step 2. Invalidate object
        self._progress = False

    def commit(self):
        """ Commit transaction
        :rtype:
        """
        # Step 1. Commit changes
        if self._dbClient is not None:
            self._dbClient.commit()
            self._dbClient = None
        # Step 2. Invalidate object
        self._progress = False
