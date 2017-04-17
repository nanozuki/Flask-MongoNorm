"""
Flask-MongoNorm
-------------

MongoNorm support for Flask applications.
"""
from setuptools import setup

setup(
    name='Flask-MongoNorm',
    version='0.1.0',
    url='https://github.com/CrowsT/Flask-MongoNorm',
    license='BSD',
    author='Crows',
    author_email='pt.wenhan@gmail.com',
    description='MongoNorm support for Flask applications',
    long_description=__doc__,
    zip_safe=False,
    platforms='any',
    packages=['flask_mongonorm'],
    install_requires=[
        'Flask(>=0.10)',
        'MongoNorm(>=2.0)',
        'PyMongo(>=3.0)'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
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
