from setuptools import setup

setup(
    name='beatbox',
    version='37.0',  # be sure to update the version in _beatbox.py too
    package_dir={'': 'src'},
    packages=['beatbox'],
    author="Simon Fell et al",
    author_email='plonesf@googlegroups.com',
    description="A Python library for querying/updating Saleforce.com data via SOAP API",
    long_description=open('README.rst').read() + "\n" + open('CHANGES.rst').read(),
    license="GNU GENERAL PUBLIC LICENSE Version 2",
    keywords="python salesforce salesforce.com",
    url="http://code.google.com/p/salesforce-beatbox/",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
