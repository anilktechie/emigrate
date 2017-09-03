#

from __future__ import absolute_import

from uuid import uuid4
from os.path import join
from datetime import datetime

from .._BaseAction import BaseAction


class ActionCreate(BaseAction):
    NAME = "create"
    DESC = "create new migration"


    def _createFileName(self, utc_datetime):
        """ Make new migration name
        """

        result = "Migration_{utc_datetime}.py".format(utc_datetime=utc_datetime)
        return result


    def _createClassName(self, utc_datetime):
        result = "Migration_{utc_datetime}".format(utc_datetime=utc_datetime)
        return result


    def _createUniqueHash(self):
        result = uuid4().hex
        return result


    def _createTemplate(self):
        result  = "# -*- coding: utf-8 -*-\n"
        result += "\n"
        result += "from emigrate import Migration\n"
        result += "\n"
        result += "class {{CLASSNAME}}(Migration):\n"
        result += "    HASH = '{{HASH}}'\n"
        result += "    COMMENT = 'no description'\n"
        result += "\n"
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
            subName = "{{" + name + "}}"
            result = result.replace(subName, value)
        return result


    def _makeContent(self, params):
        templateContent = self._createTemplate()
        result = self._prepareTemplate(templateContent, params)
        return result


    def make_current_datetime(self):
        """ Current datetime
        """
        utc_datetime = datetime.utcnow()
        datetime_pattern = "%Y%m%d%H%M%S"
        result = utc_datetime.strftime(datetime_pattern)
        return result


    def run(self):
        # Step 0. Prepare parameters
        utc_datetime = self.make_current_datetime()
        migration_name = self._createFileName(utc_datetime)
        params = {
            "CLASSNAME": self._createClassName(utc_datetime),
            "HASH": self._createUniqueHash(),
        }
        # Step 2. Create content
        content = self._makeContent(params)
        # Step 3. Create path
        path = join(self._context.repository_path, migration_name)
        # Step 4. Write content
        self.report("Create new migration {migration_name!r} ...".format(migration_name=migration_name))
        self.write_migration(path, content)


    def write_migration(self, path, content):
        with open(path, "w") as stream:
            stream.write(content)
            stream.close()


