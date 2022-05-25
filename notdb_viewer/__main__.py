import argparse
import notdb
import pyonr
import os
from getpass import getpass
from bcrypt import checkpw as _checkpw
from app import create_app

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

v = get_version('__init__.py')

def main():
   pass

def refresh_data(file:pyonr.Read):
   return file.readfile

def get_password():   
   return getpass('Database password: ').encode('utf-8')

def get_port():
   inp = input('Server PORT (default=5000): ')
   if inp:
      return int(inp)
   return 5000

def is_taken_port(port: int):
   # got this from https://stackoverflow.com/questions/2470971/fast-way-to-test-if-a-port-is-in-use-using-python
   import socket
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      return s.connect_ex(('localhost', port)) == 0

parser = argparse.ArgumentParser('NotDB Viewer', 'notdb_viewer [filename]', f'NotDB Viewer tool v{v}')
parser.add_argument('filename', nargs=1, type=str, help='Run a webapp to view your database data', metavar='filename')
parser.add_argument('-v', '--version', action='version', version=f'notdb_viewer {v}', help='Show the notdb_viewer version')

args = parser.parse_args()

if __name__ == '__main__' or __name__ == 'notdb_viewer.__main__':
   if len(args.filename) != 0:
      filename = args.filename[0]
      
      if not os.path.isfile(filename):
         parser.error('Invalid filename/path')
      

      file = pyonr.Read(filename)
      filedata = refresh_data(file)
      db = None
      if filedata.get('__password'):
         _p = get_password()
         if not _checkpw(_p, filedata.get('__password')):
            parser.error('Wrong password.')

         db = notdb.NotDBClient(filename, password=_p)
      else:
         db = notdb.NotDBClient(filename)
            
      
      port = get_port()
      if is_taken_port(port):
         parser.error('Used port')

      wa = create_app()

      wa.db = db
      wa.file = file

      wa.run(port=port)