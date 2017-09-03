#

from __future__ import absolute_import

from ._Context import Context
from ._ContextModel import ContextModel
from ._ContextModelReader import ContextModelReader


class ContextManager(object):
    def __init__(self):
        pass


    def create_new_model(self):
        """ Create new context model
        """
        result = ContextModel()
        return result


    def recover(self, path, context=None):
        """ Recover context

        @param str path:
        """
        if context is None:
            result = Context()

        # Step 1. Recover context model
        cmr = ContextModelReader()
        cm = cmr.read(path)

        # Step 2. Create connection
        for conn in cm.connections:
            print(conn)
