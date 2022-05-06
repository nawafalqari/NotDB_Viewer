'''
NotDB Viewer
------------

Simple viewer for NotDB Databases

   $ pip install notdb-viewer

Full documentation is avaliable on [Github](https://github.com/nawafalqari/NotDB_Viewer#readme)
'''

from .app import create_app, viewer_html

__version__ = '1.2.5'
__all__ = ['create_app', 'viewer_html']