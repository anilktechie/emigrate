#

import sys

from emigrate import BaseAction


class ActionHelp(BaseAction):
    NAME = "help"
    DESC = "show help message"


    @property
    def version(self):
        result = "UNKNOWN"
        #
        if hasattr(self.app, "VERSION"):
            result = self.app.VERSION
        #
        return result


    def makeUsage(self):
        """ Create help message
        """
        items = []
        items.append("Usage: {cmd} [command]".format(cmd=sys.argv[0]))
        items.append("Emigrate command-line client, version {version}.".format(version=self.version))
        items.append("")
        items.append("The most commonly used commands are:")
        items.append("")
        #
        for action in self.app.actions:
            if hasattr(action, 'DESC'):
                name = action.NAME
                msg = action.DESC
                items.append("    {name:<10s} : {msg:s}".format(name=name, msg=msg))
        #
        items.append("")
        items.append("Emigrate is a tool for database schema version control.")
        items.append("For additional information, see http://www.github.com/vit1251/emigrate")
        items.append("")
        #
        content = "\n".join(items)
        return content


    def run(self):
        """ Main entry point
        """
        msg = self.makeUsage()
        sys.stdout.write(msg)
