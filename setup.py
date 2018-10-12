#!/usr/bin/env python
# coding:utf-8

from setuptools import setup, find_packages

setup(
    name='poeditorcli',
    version='0.7',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click', 'PyYAML', 'Jinja2'
    ],
    entry_points='''
        [console_scripts]
        yamlsite=yamlsite.main:cli
    ''',
)
