#
import ConfigParser as configparser


class OptionsReader(object):


    def read(self, name):
        result = {}
        config = configparser.RawConfigParser()
        config.read(name)
        if config.has_section("database"):
            items = config.items("database")
            for name, value in items:
                result[name] = self._unquote(value)
        return result

    def _unquote(self, value):
        result = str(value) # WARNING - copy instance there ...
        if result.startswith("\"") and result.endswith("\""):
            result = result[1:-1]
        return result
