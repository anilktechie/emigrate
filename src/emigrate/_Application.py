#

import os
import sys
import logging

import yaml

from emigrate.actions import ActionCreate, ActionStatus, ActionHelp, ActionList, ActionUp, ActionDown, ActionRedo, ActionInit, ActionInfo, ActionGenerate


class Application(object):
    VERSION = "0.4"

    """ Migrate is database update tools
    """

    def __init__(self):
        #
        self._settings = {}
        #
        self.__log = logging.getLogger("emigrate")
        #
        self._readSettings()
        #
        self._actions = (
            ActionCreate,
            ActionGenerate,
            ActionHelp,
            ActionUp,
            ActionDown,
            ActionList,
            ActionRedo,
            ActionInit,
            ActionInfo,
            ActionStatus,
        )


    @property
    def settings(self):
        """ Returns settings (read-only)
        """
        return self._settings


    @property
    def actions(self):
        """ Returns actions (read-only)
        """
        return self._actions


    def _readSettings(self):
        #
        basepath = os.getcwd()
        filename = os.path.join(basepath, ".emigraterc")
        #
        if os.path.isfile(filename):
            with open(filename, "rb") as stream:
                self._settings = yaml.load(stream)


    def invokeAction(self, action_name):
        executed = False
        for action in self._actions:
            cur_action_name = action.NAME
            if cur_action_name == action_name:
                a = action(app=self)
                a.run()
                executed = True
        #
        if executed is False:
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
