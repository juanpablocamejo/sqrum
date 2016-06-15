from flask import Flask
from flask_restful import Api
from flask.ext.sqlalchemy import SQLAlchemy
#se dejan las variables "globales" en este modulo para evitar imports circulares
_app = Flask(__name__)
_api = Api()
db = SQLAlchemy()