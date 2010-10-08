"""
Flask-Restful-Decorators

Adds routing decorators corresponding to the four rest methods:
@app.post, @app.get, @app.put, @app.delete
"""
from setuptools import setup

setup(
    name='Flask-Restful-Decorators',
    version='0.1',
    url='',
    license='BSD',
    author='Ludovico Fischer',
    author_email='livrerie@gmail.com',
    description='',
    packages=['flaskext',],
    namespace_packages=['flaskext',],
    zipsafe=False,
    platforms='any',
    install_requires=[
        'Flask'
        ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ]
)
