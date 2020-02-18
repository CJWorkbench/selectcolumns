#!/usr/bin/env python

from setuptools import setup

setup(
    name="selectcolumns",
    version="0.0.1",
    description="Retain or delete columns from the table",
    author="Adam Hooper",
    author_email="adam@adamhooper.com",
    url="https://github.com/CJWorkbench/selectcolumns",
    packages=[""],
    py_modules=["selectcolumns"],
    install_requires=["pandas==0.25.0", "cjwmodule>=1.4.0"],
)
