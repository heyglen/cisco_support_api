#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

REQUIRED = [
    'colorlog',
    'aiohttp',
    'appdirs',
    'pyyaml',
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
    name='cisco_support_api',
    version='0.1.0',
    description="Project",
    long_description=readme + '\n\n' + history,
    author="Glen Harmon",
    author_email='glencharmon@gmail.com',
    url='https://github.com/heyglen/cisco_support_api',
    packages=find_packages(exclude=['contrib', u'docs', u'tests']),
    package_dir={'cisco_support_api':
                 'cisco_support_api'},
    entry_points={
        'console_scripts': [
            'cisco_support_api=cisco_support_api.cli:commands'
        ]
    },
    include_package_data=True,
    install_requires=REQUIRED,
    license="MIT license",
    zip_safe=False,
    keywords='cisco_support_api',
    classifiers=[
        'Environment :: Console',
        'Topic :: System :: Networking',
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 3 :: Only",
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
