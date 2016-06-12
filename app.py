# -*- coding: utf-8 -*-
import os
from flask import Flask, send_from_directory
from flask_restful import Api
from orm import db
import test_data
from api.controllers import *
from api.models import *

#INICIALIZANDO FLASK
_app = Flask(__name__)
_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqrum.db'

#INICIALIZANDO FLASK_RESTFUL
_api.init_app(_app)

# INICIALIZANDO SQLALCHEMY
db.init_app(_app)

with _app.app_context():
     db.drop_all()
     db.create_all()
     test_data.insertar_datos()

######## SIRVIENDO CONTENIDO ESTÁTICO DEL FRONT ########
@_app.route('/')
def root():
     return send_from_directory('front', 'index.html')

@_app.route('/<path:path>')
def files(path):
     return send_from_directory('front', path)
#######################################################

if __name__ == '__main__':
     port = int(os.getenv('PORT', 8080))
     host = os.getenv('IP', '0.0.0.0')
     _app.run(port=port, host=host, debug=True)
