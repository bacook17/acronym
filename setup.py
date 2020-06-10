#!/usr/bin/env python
# -*- coding: utf-8 -*-

# To use: python setup.py install

import os
import re
import codecs
from setuptools import setup, Command
from setuptools.command.install import install

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


# https://packaging.python.org/guides/single-sourcing-package-version/
def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


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

        
entry_points = {
    'console_scripts': ['acronym = acronym.acronym:main']
}

description = """ACRONYM (Acronym CReatiON for You and Me)"""

setup(
    name='acronym',
    version=find_version('acronym', '__init__.py'),
    author='Ben Cook',
    author_email='bcook@cfa.harvard.edu',
    entry_points=entry_points,
    packages=['acronym'],
    url='https://github.com/bacook17/acronym',
    license='LICENSE',
    description=description,
    long_description=description,
    install_requires=['numpy', 'tqdm', 'nltk'],
    cmdclass={'clean': CleanCommand, 'install': CustomInstall},
    classifiers=[
        "Topic :: Scientific/Engineering :: Astronomy",
    ]
)
