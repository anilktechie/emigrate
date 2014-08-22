#
import logging

from app_base import ApplicationCommand


class ApplicationCommandHistory(ApplicationCommand):
    def __init__(self, app):
        ApplicationCommand.__init__(self, app)
        #
        self.__log = logging.getLogger("emigrate.history")

    def run(self):
        dbClient = self.createDatabaseClient(autoConnect=True)
