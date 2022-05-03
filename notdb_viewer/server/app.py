from flask import Flask, render_template_string, request
import pyonr
import notdb
from requests import get
from flask_minify import minify

def refresh_data(file:pyonr.Read) -> dict:
   return file.readfile

def get_class(obj):
   return type(obj)

def get_obj_class_name(obj):
   return type(obj)().__class__.__name__

viewer_html = '''


<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   
   <!-- Bootstrap -->
   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
   <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

   <!-- JQuery -->
   <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>

   <!-- FontAwesome -->
   <link rel="stylesheet" href="https://pro.fontawesome.com/releases/v5.10.0/css/all.css" integrity="sha384-AYmEC3Yw5cVb3ZcuHtOA93w35dYTsvhLPVnYs9eStHfGJvOvKxVfELGroGkvsg+p" crossorigin="anonymous" />
   
   <title>{{ host }}</title>
   <style>
      :root {
         --dark_bg: #0d1b2a;
         --dark_bg2: #293958;
         --main_dark: #415a77;
         --main_light: #778da9;
         --main_almost_super_light: #bdc0c5;
         --main_super_light: #e0e1dd;
      }

      @keyframes rotate {
         from { transform: rotate(0deg) } 
         to { transform: rotate(360deg) } 
      }
      
      body {
         background-color: var(--dark_bg);
         color: var(--main_super_light)
      }

      div.container {
         margin-top: 10px;
      }

      div.host-container {
         margin-top: 20px;
      }
      
      div.host-container div.host-text {
         background-color: var(--dark_bg2);
         padding: 20px;
         border-radius: 10px;
         user-select: all;
      }

      div.info-container {
         margin-top: 20px;
      }

      div.info-container p {
         margin-bottom: 0.3rem;
      }

      div.info-container p .val {
         background-color: var(--dark_bg2);
         padding: 3px;
         border-radius: 5px;
      }

      div.documents-container, .data-h5 {
         margin-top: 20px
      }

      .docs-title {
         display: flex;
         justify-content: space-between;
         align-items: center;
      }

      .refresh svg {
         width: 25px;
         fill: var(--main_super_light);
         cursor: pointer;
      }
      
      .rotate-ani {
            animation: rotate 1.5s;
            animation-timing-function: cubic-bezier( 0.25, 0.82, 1, 1 ) ;
      }

      div.documents-container div.doc-container {
         background-color: var(--dark_bg2);
         padding: 20px;
         border-radius: 10px;
         margin-bottom: 20px;
      }

      div.documents-container div.doc-container .doc-data {
         display: flex;
         justify-content: space-between;
      }

      div.documents-container div.doc-container .doc-data .type {
         opacity: 80%;
      }

      .no-data {
         margin-top: 100px;
         font-size: 30px;
         display: flex;
         justify-content: center;
      }

      nav {
         display: flex;
         justify-content: space-between;
         align-items: center;
      }

      nav a {
         color: var(--main_super_light);
         transition: 0.3s;
         text-decoration: none;
      }

      nav a:hover {
         color: var(--main_almost_super_light);
      }

      nav .discord {
         font-size: 20px;
      }
   </style>
</head>
<body>
   <div class="container">
      <nav>
         <h2>NotDB Viewer</h2>
         <div class="d">
            Join our official 
            <a href="https://discord.gg/Az8McWNAcg" target="_blank">
              <i class="fab fa-discord discord"></i>
              Discord
            </a>
         </div>
      </nav>
      <div class="host-container">
         <h5>Host:</h4>
         <div class="host-text">
            {{ host }}
         </div>
      </div>
      <div class="info-container" id="info-c">
         {% for text, val in db_info.items() %}
            <div class="info">
               <p>
                  {{ text }}: 
                  <b class="val">{{ val }}</b>
               </p>
            </div>
         {% endfor %}
      </div>
      <div class="docs-title">
         <h5 class="data-h5">Data:</h4>
            <div class="refresh" id="refresh" title="Keyboard shortcut: R" onclick="ani();refreshDocuments()">
               <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path d="M468.9 32.11c13.87 0 27.18 10.77 27.18 27.04v145.9c0 10.59-8.584 19.17-19.17 19.17h-145.7c-16.28 0-27.06-13.32-27.06-27.2c0-6.634 2.461-13.4 7.96-18.9l45.12-45.14c-28.22-23.14-63.85-36.64-101.3-36.64c-88.09 0-159.8 71.69-159.8 159.8S167.8 415.9 255.9 415.9c73.14 0 89.44-38.31 115.1-38.31c18.48 0 31.97 15.04 31.97 31.96c0 35.04-81.59 70.41-147 70.41c-123.4 0-223.9-100.5-223.9-223.9S132.6 32.44 256 32.44c54.6 0 106.2 20.39 146.4 55.26l47.6-47.63C455.5 34.57 462.3 32.11 468.9 32.11z"/></svg>
            </div>
         </div>
         <div class="documents-container" id="doc-c">
            {% for document in documents %}
               <div class="doc-container">
                  {% for key, val in document.items() %}
                  <div class="doc-data">
                        <div class="keyval">
                           {{ key }}: <b class="doc-val">{{ val }}</b>
                        </div>
                        <div class="type" title="{{ get_class(val) }}">
                           type: <b>{{ get_obj_class_name(val) }}</b>
                        </div>
                     </div>
                  {% endfor %}
               </div>
            {% endfor %}
            {% if not documents %}
            <h5 class="no-data">There is no data in your Database :(</h5>
            {% endif %}
         </div>
   </div>

   <script>
      function refreshDocuments() {
         $('#doc-c').load(document.URL + ' #doc-c')
         $('#info-c').load(document.URL + ' #info-c')
      }

      function ani() {
         var ele = document.getElementById('refresh')
         if(ele.classList.contains('rotate-ani')) {
            ele.classList.remove('rotate-ani')
         } else {
            ele.classList.add('rotate-ani')
            setTimeout(() => {
               ele.classList.remove('rotate-ani')
            }, 1500)
         }
      }

      document.addEventListener('keyup', (e) => {
         if(e.key == 'r') {
            ani()
            refreshDocuments()
         }
      })
   </script>
</body>
</html>


'''

def create_app():

   app = Flask(__name__)

   minify(app, html=True, js=True, cssless=True, fail_safe=True)

   @app.route('/')
   def index():
      db = app.db
      file = app.file

      data = refresh_data(file)
      db_info = {}

      db_info['Secured with password'] = True if data.get('__password') else False
      db_info['documents'] = db.documents

      return render_template_string(viewer_html,
                              documents=db.get({}),
                              db_info=db_info,
                              host=db.host,
                              get_obj_class_name=get_obj_class_name,
                              get_class=get_class,
                              f=file)

   return app