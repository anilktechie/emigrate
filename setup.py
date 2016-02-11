#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name="emigrate",
    version="0.4",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'emig=emigrate._Application:main',
        ],
    },
    install_requires=["apipkg", "mysqlclient", "PyYAML"],
    zip_safe=True,
)
