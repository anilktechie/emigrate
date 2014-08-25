#
import os
import sys
import logging
import uuid
import datetime

from app_base import ApplicationCommand


class ApplicationCommandCreate(ApplicationCommand):
    def __init__(self, app):
        ApplicationCommand.__init__(self, app)
        self.__log = logging.getLogger("emigrate.create")

    def _createClassName(self, currentDateTime):
        dateTimePattern = "%Y%m%d%H%M%S"
        myDateTime = currentDateTime.strftime(dateTimePattern)
        result = "Migration" + "_" + myDateTime
        return result

    def _createTemplate(self):
        result  = "# -*- coding: utf-8 -*-\n"
        result += "\n"
        result += "from emigrate import Migration\n"
        result += "\n"
        result += "class {ClassName}(Migration):\n"
        result += "    def up(self):\n"
        result += "        pass\n"
        result += "\n"
        result += "    def down(self):\n"
        result += "        pass\n"
        result += "\n"
        return result

    def _prepareTemplate(self, templateContent, params):
        """
        :type templateContent: str
        :type params: dict
        :rtype: str
        """
        result = templateContent[:]
        for name, value in params.items():
            subName = "{" + name + "}"
            result = result.replace(subName, value)
        return result

    def _makeContent(self, params):
        templateContent = self._createTemplate()
        result = self._prepareTemplate(templateContent, params)
        return result

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
        # Step 0. Prepare parameters
        currentDateTime = datetime.datetime.today()
        params = {
            "ClassName": self._createClassName(currentDateTime),
            "FileName": self._createFileName(currentDateTime),
        }
        # Step 1. Create settings
        if not os.path.isfile(".emigraterc"):
            self._makeOptions()
        # Step 2. Create content
        content = self._makeContent(params)
        # Step 3. Create path
        basePath = os.path.abspath(".migration")
        path = os.path.join(basePath, params.get("FileName"))
        if not os.path.isdir(basePath):
            sys.stdout.write("Create directory with migration ...")
            os.makedirs(basePath)
        # Step 4. Write content
        sys.stdout.write("Create migration `" + params.get("FileName") + "` ...\n")
        with open(path, "w") as stream:
            stream.write(content)
            stream.close()
        # Step 5. Report result
        sys.stdout.write("Done.\n")

    def _createFileName(self, currentDateTime):
        #if interactive:
        #    migrationName = raw_input()
        #else:
        name = uuid.uuid4().hex
        dateTimePattern = "%Y%m%d%H%M%S"
        myDateTime = currentDateTime.strftime(dateTimePattern)
        result = myDateTime + "_" + name + "." + "py"
        return result
