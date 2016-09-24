#!/usr/bin/env python

from setuptools import setup

setup(name='way2',
      version='1.0',
      description='Command line tool to send SMS(only in India) via way2',
      author='Gurdit Singh Bedi',
      py_modules=['way2'],
      entry_points={
           'console_scripts': [
               'way2=way2:sendSMS'
           ]
      }
      )
