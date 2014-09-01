#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='stlsort',
    version='0.0.1',
    description='Sort ASCII STL files for better version control',
    long_description=''.join(open('README.rst').readlines()),
    keywords='STL, mesh, 3D, sort, git',
    author='nop head',
    author_email='nop.head@gmail.com',
    maintainer='Miro Hrončok',
    maintainer_email='Miro Hrončok',
    license='GPLv2',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
