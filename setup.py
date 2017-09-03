#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name="emigrate",
    version="0.5",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=["pymysql"],
    zip_safe=True,
)
