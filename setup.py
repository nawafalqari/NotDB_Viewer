'''
NotDB Viewer
------------

Simple viewer for NotDB Databases

    $ pip install notdb-viewer

Full documentation is avaliable on `Github <https://github.com/nawafalqari/NotDB_Viewer#readme>`_.
'''

from setuptools import setup, find_packages
import os.path

# got these 2 functions from https://packaging.python.org/en/latest/guides/single-sourcing-package-version/
def read(rel_path):
    import codecs
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

packages = [
    *find_packages()
]

setup(
    name='notdb_viewer',
    packages=packages,
    include_package_data=True,
    install_requires=[
        'notdb>=1.2.6',
        'pyonr>=1.0.0',
        'bcrypt>=3.2.0',
        'flask',
        'flask-minify'
    ],
    version=get_version('notdb_viewer/__init__.py'),
    description='Viewer for NotDB Databases',
    author='Nawaf Alqari',
    author_email='nawafalqari13@gmail.com',
    keywords=['notdb', 'db', 'database', 'notdatabsae', 'simple database'],
    long_description=__doc__,
    long_description_content_type='text/x-rst',
    entry_points={
        'console_scripts': ['notdb_viewer=notdb_viewer.__main__:main']
    },
    license='MIT',
    zip_safe=False,
    url='https://github.com/nawafalqari/NotDB_Viewer/',
    project_urls={
        'Documentation': 'https://github.com/nawafalqari/NotDB_Viewer#readme',
        'Bug Tracker': 'https://github.com/nawafalqari/NotDB_Viewer/issues',
        'Source Code': 'https://github.com/nawafalqari/NotDB_Viewer/',
        'Discord': 'https://discord.gg/cpvynqk4XT',
        'Donate': 'https://paypal.me/NawafHAlqari'
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Database'
    ],
)