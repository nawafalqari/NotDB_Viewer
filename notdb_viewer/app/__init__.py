from flask import Flask, render_template, request
import pyonr
import notdb
from requests import get

def refresh_data(file:pyonr.Read) -> dict:
   return file.readfile

def get_class(obj):
   return type(obj)

def get_obj_class_name(obj):
   return type(obj)().__class__.__name__

def create_app():

   app = Flask(__name__)

   @app.route('/')
   def index():
      db = app.db
      file = app.file

      data = refresh_data(file)
      db_info = {}

      db_info['Secured with password'] = True if data.get('__password') else False
      db_info['documents'] = db.documents

      return render_template('viewer.html',
                              documents=db.get({}),
                              db_info=db_info,
                              host=db.host,
                              get_obj_class_name=get_obj_class_name,
                              get_class=get_class,
                              f=file)

   return app