#!/usr/bin/python

import os
from setuptools import setup
import sys

version = '0.2.4.1'

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

reqs = []
 # for python2.4
if sys.version_info[:2] < (2, 5):
    reqs += ['pycrypto']

setup(
    name = 'python-amazon-product-api',
    version = version,
    author = 'Sebastian Rahlf',
    author_email = 'basti AT redtoad DOT de',
    url="http://bitbucket.org/basti/python-amazon-product-api/downloads/",
    license='bsd',

    description = 'A Python wrapper for the Amazon Product Advertising API.',
    long_description=read('README'),
    keywords = 'amazon product advertising api wrapper signed requests',

    packages = ['amazonproduct'],
    install_requires=reqs,

    test_suite = 'tests',
    test_loader = 'tests:XMLResponseTestLoader',
    tests_require = ['nose', 'lxml>=2.1.5'],

    classifiers = [
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
