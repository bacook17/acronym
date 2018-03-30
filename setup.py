#!/usr/bin/env python
# -*- coding: utf-8 -*-

# To use: python setup.py install

from setuptools import setup


setup(
    name='acronym',
    version='0.1.0',
    author='Ben Cook',
    author_email='bcook@cfa.harvard.edu',
    packages=['acronym'],
    url='https://github.com/bacook17/acronym',
    license='LICENSE',
    description="""ACRONYM (Acronym CReatiON for You and Me)""",
    scripts=['acronym/acronym.py'],
    install_requires=['numpy', 'tqdm', 'pyenchant'],
)
