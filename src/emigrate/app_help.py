#
import sys

from app_base import ApplicationCommand


class ApplicationCommandHelp(ApplicationCommand):
    
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
        items.append("    create    - create migration in .migration directory")
        items.append("    up        - upgrade migration operation")
        items.append("    down      - downgrade migration operation")
        items.append("    redo      - redo migration operation (when previous is with exception)")
        items.append("    history   - show migration operation")
        items.append("    new       - show new migration")
        items.append("")
        items.append("Emigrate is a tool for database schema version control.")
        items.append("For additional information, see http://www.github.com/vit1251/emigrate")
        content = "\n".join(items)
        return content
    
    def run(self):
        """ Main entry point
        """
        help_message = self.__create_help_message()
        sys.stdout.write(content)
