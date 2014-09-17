#!/usr/bin/python

from setuptools import setup

setup(
    name = "emigrate",
    version = "0.2",
    packages = ['emigrate'],
    package_dir = {'': 'src'},
    entry_points = {
        'console_scripts': [
            'emig = emigrate.app:main',
        ],
    },
    install_requires=[
    ],
)
