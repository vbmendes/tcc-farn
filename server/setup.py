# -*- coding: utf8 -*-

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "rest-demo-server",
    version = "0.0",
    description = "REST demo server.",
    long_description = read('README'),
    author = 'Vinicius Mendes',
    author_email = 'vbmendes@gmail.com',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = [
        'setuptools',
        'web.py',
        'mimerender',
        'cherrypy',
        'suds',
    ],
)

