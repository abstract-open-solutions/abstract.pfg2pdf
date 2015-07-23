# -*- coding: utf-8 -*-
"""Installer for the abstract.pfg2pdf package."""

from setuptools import find_packages
from setuptools import setup


long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')


setup(
    name='abstract.pfg2pdf',
    version='0.1',
    description="PFG form data to PDF action",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.2.7",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='Python Plone',
    author='Simone Orsi',
    author_email='simone.orsi@abstract.it',
    url='http://pypi.python.org/pypi/abstract.pfg2pdf',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['abstract'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.api',
        'setuptools',
        'Products.PloneFormGen',
        'Products.TemplateFields',
        'abstract.wkhtmltopdf',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
            'Products.PloneFormGen',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
