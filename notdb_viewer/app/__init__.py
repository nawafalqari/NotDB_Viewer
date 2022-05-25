from flask import Flask, render_template, request, jsonify, Response, make_response
import pyonr
import notdb
from flask_minify import minify

def refresh_data(file:pyonr.Read) -> dict:
   return file.readfile

def get_class(obj):
   return type(obj)

def get_obj_class_name(obj):
   return type(obj)().__class__.__name__

def create_app():

   app = Flask(__name__)
   app.url_map.strict_slashes = False

   minify(app, html=True, js=True, cssless=True, fail_safe=True)

   @app.route('/')
   def documents_route():
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
                              get_class=get_class)

   @app.route('/files')
   def files_route():
      db = app.db
      webAppURL = str(request.url_root)

      return render_template('files.html',
                        files=db.files.getFiles({}),
                        host=db.host,
                        webAppURL=webAppURL,
                        get_obj_class_name=get_obj_class_name,
                        get_class=get_class)

   @app.route('/cdn/<name>')
   def cdn_loader(name):
      try:
         db = app.db

         file = db.files.getFile({'name': name})
         file = db.files.getFile({'name': name})
         err = {}

         if not file:
            err['success'] = False
            err['err'] = 'INVALID_NAME'
            err['msg'] = f'{name} is not in the database'
            return jsonify(err)

         return Response(file['data'], mimetype=file['mimetype'])
      except Exception as e:
         err['err'] = str(e)
         return jsonify(err)


   @app.route('/cdn')
   def cdn_route():
      err = {}
      err['success'] = False
      err['err'] = 'INVALID_NAME'
      err['msg'] = 'add a name after (/cdn/<name>)'

      return jsonify(err)

   return app