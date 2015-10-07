#

import sys


from emigrate import BaseAction


class ActionHelp(BaseAction):
    def __init__(self, app):
        BaseAction.__init__(self, app)
        self.__app = app
                            
    def __get_version(self, default="UNKNOWN"):
        result = default
        #
        app = self.getApplication()
        if hasattr(app, "VERSION"):
            result = app.VERSION
        #
        return result

    def __create_help_message(self):
        """ Create help message
        """
        items = []
        items.append("Usage: {cmd} [command]".format(cmd=sys.argv[0]))
        items.append("Emigrate command-line client, version {version}.".format(version=self.__get_version()))
        items.append("")
        items.append("The most commonly used commands are:")
        items.append("")
        #
        for actionName, actionType in self.__app.actions().items():
            if hasattr(actionType, 'HELP'):
                actionHelp = actionType.HELP
                items.append("    {actionName:<10s} - {actionHelp:s}".format(actionName=actionName, actionHelp=actionHelp))
        #
        items.append("")
        items.append("Emigrate is a tool for database schema version control.")
        items.append("For additional information, see http://www.github.com/vit1251/emigrate")
        content = "\n".join(items)
        return content
    
    def run(self):
        """ Main entry point
        """
        help_message = self.__create_help_message()
        sys.stdout.write(help_message)
