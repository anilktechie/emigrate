#

from __future__ import absolute_import

from sys import exit, argv

from ._Application import Application


def main():
    app = Application()
    app.initialize()
    rc = app.run(argv)
    return rc


if __name__ == "__main__":
    exit(main())
