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


class Application(object):
    """ Migrate is database update tools
    """

    def __init__(self):
        self.__log = getLogger("emigrate")
        self._settings = {}
        self.actions = []
        self._context = None


    def initialize(self, **kwargs):

        # Step 1. Create context
        self._context = Context(app=self)

        # Step 2. Register action's
        self.register_action(ActionHelp)
        self.register_action(ActionInit)
        self.register_action(ActionCreate)
        self.register_action(ActionList)
        self.register_action(ActionVerify)
        #self.register_action(ActionUp)
        #self.register_action(ActionDown)
        #self.register_action(ActionRedo)


    def register_action(self, action):
        """ Register action (action is type)

        @param BaseAction action:
        """
        assert issubclass(action, BaseAction)
        self.actions.append(action)



    def _readSettings(self):
        #
        basepath = os.getcwd()
        filename = os.path.join(basepath, ".emigraterc")
        #
        if os.path.isfile(filename):
            with open(filename, "rb") as stream:
                self._settings = yaml.load(stream)


    def search_action(self, action_name):
        """ Search action by name

        @param str action_name
        """
        result = None
        for action in self.actions:
            cur_action_name = action.NAME
            if cur_action_name == action_name:
                result = action
                break
        return result


    def process_action(self, action):
        """ Process action
        """
        a_inst = action(context=self._context)
        a_inst.run()


    def invoke_action(self, action_name):
        """ Invoke action

        @param str action_name
        """
        self.__log.debug("invoke_action: action_name = {action_name!r}".format(action_name=action_name))

        # Step 1. Search action
        action = self.search_action(action_name)

        # Step 2. Process action
        if action:
            self.process_action(action)
        else:
            self.no_action(action_name)


    def usage(self):
        self.invokeAction('help')


    def no_action(self, action_name):
        content = "'{action_name}' is not emigrate command. See 'emigrate help'\n".format(action_name=action_name)
        stdout.write(content)


    def dispose(self):
        pass


    def run(self, argv):
        """ Main process
        """
        rc = 1

        argc = len(argv)
        if argc > 1:
            action_name = str(argv[1])
            rc = self.invoke_action(action_name)
        else:
            self.usage()

        return rc

