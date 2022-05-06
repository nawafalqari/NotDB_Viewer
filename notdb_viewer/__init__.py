'''
NotDB Viewer
-----

NotDB Simple viewer for NotDB Databases

   $ pip install notdb-viewer

Full documentation is avaliable on `Github <https://github.com/nawafalqari/NotDB_Viewer#readme>`_.
'''

from .app import create_app, viewer_html

__version__ = '1.2.4'
__all__ = ['create_app', 'viewer_html']