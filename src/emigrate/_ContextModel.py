#

from __future__ import absolute_import

from ._ContextModelConnection import ContextModelConnection


class ContextModel(object):
    def __init__(self):
        self.connections = []


    def create_new_connection(self, name):
        """ Create new connection model

        @param str name:
        """
        result = connection_model = ContextModelConnection()
        connection_model.name = name
        self.connections.append(connection_model)
        return result
