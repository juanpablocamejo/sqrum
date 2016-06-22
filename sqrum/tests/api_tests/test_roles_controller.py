# -*- coding: utf-8 -*-
from unittest import TestCase
from common import _app, _api, db
from app_factory import AppFactory
import os, tempfile, data, json
from api.models import *
from api.controllers import *

class RolesControllerTests(TestCase):
    def setUp(self):
        if not os.path.exists('./tmp'): 
            os.mkdir('./tmp')
        self.defaultDir = tempfile.mkdtemp(dir='./tmp')
        self.defaultFile = 'index.html'
        self.dbLocation = self.defaultDir + '/temp.db'

    def tearDown(self):
        os.system('sudo rm -f -r ./tmp')
        
    def test_get_rol_by_id(self):
        '''API | GET Rol por Id'''
        #arrange
        _app = AppFactory.create_app(_api, db, self.dbLocation)
        _app.testing = True
        self.rol1 = Rol(u"Desarrollador")
        self.rol2 = Rol(u"Administrador")
        AppFactory.add_test_data(db, [self.rol1, self.rol2])
        #act
        with _app.test_client() as c:
            self.ruta = '/api/rol/' + str(self.rol1.id)
            self.resp = c.get(self.ruta)
        #assert
        assert self.resp.status_code == 200
        assert json.loads(self.resp.data)['id']==self.rol1.id
        assert json.loads(self.resp.data)['nombre']==self.rol1.nombre
    
    def test_get_roles(self):
        '''API | GET Roles'''
        #arrange
        _app = AppFactory.create_app(_api, db, self.dbLocation)
        _app.testing = True
        self.rol1 = Rol(u"Desarrollador")
        self.rol2 = Rol(u"Administrador")
        AppFactory.add_test_data(db, [self.rol1, self.rol2])
        #act
        with _app.test_client() as c:
            self.ruta = '/api/rol/'
            self.resp = c.get(self.ruta)
        #assert
        assert self.resp.status_code == 200
        assert len(json.loads(self.resp.data))==2
        assert json.loads(self.resp.data)[0]['id'] == self.rol1.id
        assert json.loads(self.resp.data)[1]['id'] == self.rol2.id