#!/usr/bin/env python
# -*- coding: utf-8 -*-

# To use: python setup.py install

import os

from setuptools import setup, Command
from setuptools.command.install import install


class CustomInstall(install):
    """
    """
    def run(self):
        install.run(self)


class CleanCommand(Command):
    
    """Custom clean command to tidy up the project root.
    From https://stackoverflow.com/questions/3779915"""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')


setup(
    name='acronym',
    version='1.0.0',
    author='Ben Cook',
    author_email='bcook@cfa.harvard.edu',
    packages=['acronym'],
    url='https://github.com/bacook17/acronym',
    license='LICENSE',
    description="""ACRONYM (Acronym CReatiON for You and Me)""",
    install_requires=['numpy', 'tqdm', 'nltk'],
    include_package_data=True,
    scripts=['acronym/acronym.py'],
    cmdclass={'clean': CleanCommand, 'install': CustomInstall}
)
