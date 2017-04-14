"""
Flask-MongoNorm
-------------

MongoNorm support for Flask applications.
"""
from setuptools import setup

setup(
    name='Flask-MongoNorm',
    version='0.0.1',
    url='https://github.com/CrowsT/Flask-MongoNorm',
    license='BSD',
    author='Crows',
    author_email='pt.wenhan@gmail.com',
    description='MongoNorm support for Flask applications',
    long_description=__doc__,
    platforms='any',
    packages=['flask_mongonorm'],
    install_requires=[
        'Flask(>=0.10)',
        'MongoNorm(>=2.0)',
        'PyMongo(>=3.0)'
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
