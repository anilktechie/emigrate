#

from __future__ import absolute_import

from sys import stdout

from .._BaseAction import BaseAction


class ActionHelp(BaseAction):
    NAME = "help"
    DESC = "show help"


    def make_help_content(self):
        """ Create help message
        """

        items = []
        items.append("Usage: emigrate [command]")
        items.append("")
        items.append("The most commonly used commands are:")
        items.append("")

        for action in self._context.app.actions:
            if hasattr(action, 'DESC'):
                name = action.NAME
                msg = action.DESC
                items.append("    {name:<10s} : {msg:s}".format(name=name, msg=msg))

        items.append("")
        items.append("Emigrate is a tool for database schema version control.")
        items.append("For additional information, see http://www.github.com/vit1251/emigrate")
        items.append("")

        content = "\n".join(items)
        return content


    def run(self):
        """ Main entry point
        """
        help_content = self.make_help_content()
        stdout.write(help_content)
