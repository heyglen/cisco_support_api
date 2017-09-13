#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

REQUIRED = [
    'colorlog',
    'requests',
    'appdirs',
    'pyyaml',
    'pathlib',
    'Click>=6.0',
]

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='cisco_api',
    version='0.1.0',
    description="Project",
    long_description=readme + '\n\n' + history,
    author="Glen Harmon",
    author_email='glencharmon@gmail.com',
    url='https://github.com/heyglen/cisco_api',
    packages=find_packages(exclude=['contrib', u'docs', u'tests']),
    package_dir={'cisco_api':
                 'cisco_api'},
    entry_points={
        'console_scripts': [
            'cisco_api=cisco_api.cli:commands'
        ]
    },
    include_package_data=True,
    install_requires=REQUIRED,
    license="MIT license",
    zip_safe=False,
    keywords='cisco_api',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
