#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from captainwebhook import __version__


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='captainwebhook',
    version=__version__,
    description="Captain Webhook runs your scripts when it receives a webhook.",
    long_description=readme + '\n\n' + history,
    author="Stavros Korokithakis",
    author_email='hi@stavros.io',
    url='https://github.com/skorokithakis/captainwebhook',
    packages=[
        'captainwebhook',
    ],
    package_dir={'captainwebhook':
                 'captainwebhook'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    entry_points={
        'console_scripts': ['cptwebhook=captainwebhook.captainwebhook:main'],
    },
    keywords='captainwebhook',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
