# -*- coding: utf-8 -*-
from unittest import TestCase
from app_factory import AppFactory
from flask import Flask
from flask_restful import Api
from flask.ext.sqlalchemy import SQLAlchemy
import imp, os, tempfile
from common import _app, _api, db
from api.models import *
import data

class AppFactoryTest(TestCase):
    
    def setUp(self):
        #arrange
        self.defaultDir = tempfile.mkdtemp(dir='./tmp')
        self.defaultFile = 'index.html'
        self.dbLocation = self.defaultDir + '/temp.db'
        
    def tearDown(self):
        os.system('sudo rm -f -r ' + self.defaultDir)
    
    def test_create_app_ok(self):
        '''AppFactory.create_app | Crea y vincula las instancias de APP, API y ORM'''
        _app = AppFactory.create_app(_api, db, self.dbLocation)
        #assert
        self.assertIs(_app, db.app)
        self.assertIs(_app, _api.app)
        self.assertEquals(_app.config['SQLALCHEMY_DATABASE_URI'], 'sqlite:///' + self.dbLocation)
        
    def test_add_static_server_and_get_static_files_ok(self):
        '''AppFactory.add_static_server | Sirve contenido estático de la carpeta y archivo por defecto en "/"'''
        #arrange
        _app = AppFactory.create_app(_api, db, self.dbLocation)
        _app.testing = True
        self.imgDir = 'imgDir'
        self.imgRelPath = self.imgDir + '/img.png'
        os.mkdir(self.defaultDir + '/' + self.imgDir)
        os.mknod(self.defaultDir + '/' + self.imgRelPath)
        os.mknod(self.defaultDir + '/' + self.defaultFile)
        with open(self.defaultDir + '/' + self.defaultFile, 'a') as f:
            f.write('Hola Sqrum')
        
        #act
        AppFactory.add_static_server(_app, self.defaultDir, self.defaultFile)
        
        #assert
        with _app.test_client() as c:
            res = c.get('/')
            assert res.status_code == 200
            assert 'Hola Sqrum' in res.data
            assert c.get(self.imgRelPath).status_code == 200
    
    #def test_add_test_data_and_get_data_from_db(self):
        
        