#

from emigrate import BaseAction


class ActionConfig(BaseAction):
    HELP = "update database connection settings"

    def run(self):
        print "Yep."
