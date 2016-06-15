# -*- coding: utf-8 -*-
from flask import Flask, send_from_directory
from api.models import *
from api.controllers import *

class AppFactory:
     @staticmethod
     def create_app(api, orm, dbLocation):
          #INICIALIZANDO FLASK
          newApp = Flask(__name__)
          newApp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbLocation 
          #INICIALIZANDO FLASK_RESTFUL
          api.init_app(newApp)
          #INICIALIZANDO SQLALCHEMY
          orm.init_app(newApp)
          orm.app = newApp
          with newApp.app_context():
               orm.drop_all()
               orm.create_all()
               
          return newApp
          
     @staticmethod
     def add_static_server(app, staticFolder, defaultFile):
          ######## SIRVIENDO CONTENIDO ESTÁTICO DEL FRONT ########
          @app.route('/')
          def root():
               return send_from_directory(staticFolder, defaultFile)
          
          @app.route('/<path:path>')
          def files(path):
               return send_from_directory(staticFolder, path)
          #######################################################
          
     @staticmethod
     def add_test_data(orm, objs):
          for obj in objs:
               db.session.add(obj)
          db.session.commit()
     


