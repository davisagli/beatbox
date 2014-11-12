
from setuptools import setup

setup(
    name='beatbox',
    version='20.1',  # be sure to update the version in _beatbox.py too
    package_dir={'': 'src'},
    packages=['beatbox'],
    author="Simon Fell et al",
    author_email='plonesf@googlegroups.com',
    description="A Python library for querying/updating Saleforce.com data via SOAP API",
    long_description=open('README.rst').read() + "\n" + open('CHANGES.rst').read(),
    license="GNU GENERAL PUBLIC LICENSE Version 2",
    keywords="python salesforce salesforce.com",
    url="http://code.google.com/p/salesforce-beatbox/",
    classifiers=["Development Status :: 5 - Production/Stable"]
    )
