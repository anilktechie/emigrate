#

import os
import sys

from emigrate import BaseAction


class ActionInit(BaseAction):
    NAME = "init"
    DESC = "update database connection settings"


    def __init__(self, app):
        BaseAction.__init__(self, app)
        self._default_settings = (
            ("host", "127.0.0.1"),
            ("user", "root"),
            ("passwd", ""),
            ("db", "test"),
            ("port", 3306),
            ("connect_timeout", 5),
            ("encoding", "utf8"),
            ("collation", "utf8_general_ci"),
        )


    def writeSettings(self):
        lines = []
        for k,v in self._default_settings:
            lines.append("{k}: {v}".format(k=k, v=v))
        #
        lines.append("")
        #
        content = "\n".join(lines)
        with open(".emigraterc", "w") as stream:
            stream.write(content)
            stream.close()


    def run(self):
        sys.stdout.write("==> Write default settings in `.emigraterc`.\n")
        #
        if os.path.isfile(".emigraterc"):
            sys.stderr.write("error: File `.emigraterc` already exist.\n")
        else:
            self.writeSettings()
