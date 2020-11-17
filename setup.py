"""
DineTrack python package configuration.

Adopted from EECS 485 Project 3 setup written by Andrew DeOrio <awdeorio@umich.edu>
"""

from setuptools import setup

setup(
    name='dinetrack',
    version='0.1.0',
    packages=['dinetrack'],
    include_package_data=True,
    install_requires=[
        'arrow',
        'bs4',
        'Flask',
        'html5validator',
        'nodeenv',
        'pycodestyle',
        'pydocstyle',
        'pylint',
        'pytest',
        'requests',
        'selenium',
    ],
    python_requires='>=3.6',
)
