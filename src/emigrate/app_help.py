#
import sys

from app_base import ApplicationCommand


class ApplicationCommandHelp(ApplicationCommand):
    def run(self):
        content = "Usage: %s [command]\n" % (sys.argv[0], )
        content += "Emigrate command-line client, version %s.\n" % ("0.1", )    # TODO - how to get that version form __init__
        content += "\n"
        content += "The most commonly used commands are:\n"
        content += "\n"
        content += "    create    - create migration in .migration directory\n"
        content += "    up        - upgrade migration operation\n"
        content += "    down      - downgrade migration operation\n"
        content += "    redo      - redo migration operation (when previous is with exception)\n"
        content += "    history   - show migration operation\n"
        content += "    new       - show new migration\n"
        content += "\n"
        content += "Emigrate is a tool for database schema version control.\n"
        content += "For additional information, see http://www.github.com/vit1251/emigrate\n"
        #
        sys.stdout.write(content)
