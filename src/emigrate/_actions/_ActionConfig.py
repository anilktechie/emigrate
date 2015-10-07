#

from emigrate import BaseAction


class ActionConfig(BaseAction):
    HELP = "update database connection settings"

    def _makeOptions(self):
        #
        lines = []
        lines.append("[database]")
        lines.append("host=127.0.0.1")
        lines.append("database=test")
        lines.append("user=root")
        lines.append("password=1111")
        #
        content = "\n".join(lines)
        with open(".emigraterc", "w") as stream:
            stream.write(content)
            stream.close()

    def run(self):
        print("[+] Create default settings.")
        # Step 1. Create settings
        if not os.path.isfile(".emigraterc"):
            self._makeOptions()
