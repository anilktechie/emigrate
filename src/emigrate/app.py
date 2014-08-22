#

import sys
import logging

from app_create import ApplicationCommandCreate
from app_help import ApplicationCommandHelp
from app_up import ApplicationCommandUp
from app_down import ApplicationCommandDown
from app_history import ApplicationCommandHistory
from app_redo import ApplicationCommandRedo

from options_reader import OptionsReader


class Application(object):
    """ Migrate is database update tools
    """

    def __init__(self):
        #
        self._params = None
        #
        self.__log = logging.getLogger("emigrate")
        #
        self._readingOptions()

    def _readingOptions(self):
        optionsReader = OptionsReader()
        self._params = optionsReader.read(".emigraterc")

    def _do_CREATE(self, name):
        commandCreate = ApplicationCommandCreate(app=self)
        commandCreate.run()

    def _do_UP(self, step=None):
        commandUp = ApplicationCommandUp(app=self)
        commandUp.run()

    def _do_DOWN(self, step=None):
        commandDown = ApplicationCommandDown(app=self)
        commandDown.run()

    def _do_REDO(self, name):
        commandRedo = ApplicationCommandRedo(app=self)
        commandRedo.run()

    def _do_HISTORY(self):
        commandHistory = ApplicationCommandHistory(app=self)
        commandHistory.run()

    def _do_HELP(self):
        commandHelp = ApplicationCommandHelp(app=self)
        commandHelp.run()

    def _do_UNKNOWN(self):
        content = "Unknown command.\n"
        sys.stdout.write(content)

    def dispose(self):
        pass

    def run(self, argv):
        argc = len(argv)
        if argc > 1:
            if argv[1] == "create":
                name = ""
                if argc > 2:
                    name = argv[2]
                self._do_CREATE(name)
            elif argv[1] == "redo":
                name = ""
                if argc > 2:
                    name = argv[2]
                self._do_REDO(name)
            elif argv[1] == "up":
                step = None
                if argc > 2:
                    step = argv[2]
                self._do_UP(step)
            elif argv[1] == "down":
                step = None
                if argc > 2:
                    step = argv[2]
                self._do_DOWN(step)
            elif argv[1] == "history":
                self._do_HISTORY()
            elif argv[1] == "help":
                self._do_HELP()
            else:
                self._do_UNKNOWN()
        else:
            self._do_HELP()
        return 0


def main():
    app = Application()
    app.run(sys.argv)


if __name__ == "__main__":
    sys.exit(main())
