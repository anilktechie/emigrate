#

from __future__ import absolute_import

from os import mkdir
from os.path import exists, join, abspath

from .._BaseAction import BaseAction

from .._ContextModelWriter import ContextModelWriter
from .._ContextManager import ContextManager



class ActionInit(BaseAction):
    NAME = "init"
    DESC = "initialize emigrate repository"


    def update_context_model(self, cm_model):
        """ Update context model
        """
        cm_model_conn = cm_model.create_new_connection(name="default")
        cm_model_conn.host = "127.0.0.1"
        cm_model_conn.port = 3306
        cm_model_conn.username = "root"
        cm_model_conn.password = ""
        cm_model_conn.schema = "test"
        cm_model_conn.encoding = "utf8"
        cm_model_conn.collation = "utf8_general_ci"


    def initialize_repository(self, path):
        """ Initialize repository
        """
        # Step 1. Create directory
        if not exists(path):
            mkdir(path)

        # Step 2 Write version

        # Step 3. Write settings
        cmw = ContextModelWriter()
        cm = ContextManager()
        cm_model = cm.create_new_model()
        self.update_context_model(cm_model)
        cmw.write(join(path, 'emigrate.xml'), cm_model)


    def run(self):

        # Step 1. Check environment parameters
        path = self._context.repository_path
        conditions = [
            exists(path),
        ]
        initialized = all(conditions)

        # Step 2. Initialize new repository
        if not initialized:
            self.report("Initializing empty emigrate repository in {path}".format(path=path))

            self.initialize_repository(path=path)
        else:
            self.report("Reinitialized existing emigrate repository in {path}".format(path=path))

            self.initialize_repository(path=path)
