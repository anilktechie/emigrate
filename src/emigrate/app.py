#
import os
import sys
import logging

from app_create import ApplicationCommandCreate
from app_help import ApplicationCommandHelp
from app_up import ApplicationCommandUp
from app_down import ApplicationCommandDown
from app_history import ApplicationCommandHistory
from app_redo import ApplicationCommandRedo
from app_new import ApplicationCommandNew

from options_reader import OptionsReader


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

    def _readingOptions(self):
        #
        currentDirectory = os.getcwd()
        currentPath = os.path.join(currentDirectory, ".emigraterc")
        #
        optionsReader = OptionsReader()
        self._params = optionsReader.read(currentPath)

    def _do_CREATE(self):
        commandCreate = ApplicationCommandCreate(app=self)
        commandCreate.run()

    def _do_UP(self):
        commandUp = ApplicationCommandUp(app=self)
        commandUp.run()

    def _do_DOWN(self):
        commandDown = ApplicationCommandDown(app=self)
        commandDown.run()

    def _do_REDO(self):
        commandRedo = ApplicationCommandRedo(app=self)
        commandRedo.run()

    def _do_NEW(self):
        commandNew = ApplicationCommandNew(app=self)
        commandNew.run()

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
            commandName = str(argv[1])
            methodName = "_" + "do" + "_" + commandName.upper()
            method = getattr(self, methodName, None)
            if method is not None:
                if callable(method):
                    method()
                else:
                    raise Exception('Internal Server Error')
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
