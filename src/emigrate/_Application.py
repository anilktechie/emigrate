# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
from sys import exit, argv, stdout
from logging import getLogger

from ._Context import Context

from ._BaseAction import BaseAction

from .actions import ActionHelp
from .actions import ActionInit
from .actions import ActionCreate
from .actions import ActionList
from .actions import ActionVerify
from .actions import ActionUp
from .actions import ActionDown
from .actions import ActionRedo
from .actions import ActionStatus

from .service import CommandService


class Application(object):
    """ Migrate is database update tools
    """

    def __init__(self):
        self.__log = getLogger("emigrate")
        self._settings = {}
        self._context = None


    def initialize(self, **kwargs):

        # Step 1. Create context
        self._context = Context()

        command_service = CommandService(self._context)
        command_service.initialize()
        command_service.register_action(ActionHelp)
        #command_service.register_action(ActionInit)
        #command_service.register_action(ActionCreate)
        #command_service.register_action(ActionList)
        #command_service.register_action(ActionVerify)
        #command_service.register_action(ActionUp)
        #command_service.register_action(ActionDown)
        command_service.register_action(ActionStatus)
        self._context.register('CommandService', command_service)


    def _readSettings(self):
        #
        basepath = os.getcwd()
        filename = os.path.join(basepath, ".emigraterc")
        #
        if os.path.isfile(filename):
            with open(filename, "rb") as stream:
                self._settings = yaml.load(stream)


    def dispose(self):
        pass


    def run(self, argv):
        """ Main process
        """
        rc = 1

        command_service = self._context.get_object('CommandService')

        argc = len(argv)
        if argc > 1:
            action_name = str(argv[1])
            rc = command_service.invoke_action(action_name)
        else:
            command_service.usage()

        return rc

