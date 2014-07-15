#!/usr/bin/python

import sys
import time

from twisted.enterprise import adbapi
from twisted.internet import reactor

from dbadmin.app import Application


def main():
    app = Application()
    rc = app.run()
    return rc


if __name__ == "__main__":
    sys.exit(main())
