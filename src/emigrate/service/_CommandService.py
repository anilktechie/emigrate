#

from __future__ import absolute_import

from logging import getLogger
from sys import stdout


class CommandService(object):
    def __init__(self, context):
        self.__log = getLogger('emigrate.service.command')
        self._context = context
        self._actions = []

    def initialize(self, **kwargs):
        pass

    @property
    def actions(self):
        return self._actions

    def register_action(self, action):
        """ Register actions
        """
        self._actions.append(action)

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

    def _process_action(self, action):
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
            self._process_action(action)
        else:
            self.no_action(action_name)

    def usage(self):
        self.invokeAction('help')

    def no_action(self, action_name):
        content = "'{action_name}' is not emigrate command. See 'emigrate help'\n".format(action_name=action_name)
        stdout.write(content)
