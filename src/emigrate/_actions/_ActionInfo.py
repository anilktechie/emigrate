#

from emigrate import BaseAction


class ActionInfo(BaseAction):
    HELP = "migrator information"

    def run(self):
        print "Yep."
