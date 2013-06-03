# -*- coding: utf-8 -*-
from setuptools import setup
import os.path


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    f = open(filename, 'r')
    try:
        return f.read()
    finally:
        f.close()


classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: Implementation :: CPython',
]

setup(name='unittest2xmlreport',
      version='0.0',
      license='GNU AGPL v3+',
      description='A unittest2-based test runner with JUnit XML reporting',
      long_description=read('README'),
      author='mete0r',
      author_email='mete0r@sarangbang.or.kr',
      url='https://github.com/mete0r/unittest2xmlreport',
      classifiers=classifiers,
      keywords='unittest2 JUnit XML Report Test Runner',
      py_modules=['unittest2xmlreport'],
      install_requires=['unittest2', 'unittest-xml-reporting'],
      entry_points = {
            'console_scripts': [
                  'unittest2xmlreport = unittest2xmlreport:main',
            ]
      },
      zip_safe=True)
