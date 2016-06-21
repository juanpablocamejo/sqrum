# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api
from flask.ext.sqlalchemy import SQLAlchemy

#se dejan las variables "globales" en este modulo para evitar imports circulares
_app = None
_api = Api()
db = SQLAlchemy()