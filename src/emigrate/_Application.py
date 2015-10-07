#
import os
import sys
import logging

from emigrate.actions import ActionCreate, ActionStatus, ActionHelp, ActionList, ActionUp, ActionDown, ActionRedo, ActionConfig, ActionInfo
from emigrate import OptionsReader


class Application(object):
    VERSION = "0.2.1"
    
    """ Migrate is database update tools
    """

    def __init__(self):
        #
        self._params = None
        #
        self.__log = logging.getLogger("emigrate")
        #
        self._readingOptions()
        #
        self.__actions = {
            "create"  : ActionCreate,
            "help"    : ActionHelp,
            "up"      : ActionUp,
            "down"    : ActionDown,
            "list"    : ActionList,
            "redo"    : ActionRedo,
            "config"  : ActionConfig,
            "info"    : ActionInfo,
            "status"  : ActionStatus,
        }

    def actions(self):
        return self.__actions

    def _readingOptions(self):
        #
        currentDirectory = os.getcwd()
        currentPath = os.path.join(currentDirectory, ".emigraterc")
        #
        optionsReader = OptionsReader()
        self._params = optionsReader.read(currentPath)

    def invokeAction(self, actionName):
        actionType = self.__actions.get(actionName)
        if actionType is not None:
            action = actionType(app=self)
            action.run()
        else:
            self.unknowCommand(actionName)

    def usage(self):
        self.invokeAction('help')

    def unknowCommand(self, name):
        content = "No action {name!r}. Please use 'help' to more info.\n".format(name=name)
        sys.stdout.write(content)

    def dispose(self):
        pass

    def run(self, argv):
        argc = len(argv)
        if argc > 1:
            actionName = str(argv[1])
            self.invokeAction(actionName)
        else:
            self.usage()
        #
        return 0


def main():
    app = Application()
    app.run(sys.argv)


if __name__ == "__main__":
    sys.exit(main())
