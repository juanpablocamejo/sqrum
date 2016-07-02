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
        #asserts
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
        #asserts
            assert self.resp.status_code == 200
            assert len(json.loads(self.resp.data))==2
            assert json.loads(self.resp.data)[0]['id'] == self.rol1.id
            assert json.loads(self.resp.data)[1]['id'] == self.rol2.id
            
    def test_put_rol(self):
        '''API | PUT Rol'''
        #arrange
        _app = AppFactory.create_app(_api, db, self.dbLocation)
        _app.testing = True
        self.rol1 = Rol(u"Desarrollador")
        self.nuevo_nombre = u"Miembro del equipo"
        self.put_data = dict(nombre=self.nuevo_nombre)
        AppFactory.add_test_data(db, [self.rol1])
        #act
        with _app.test_client() as c:
            self.ruta = '/api/rol/' + str(self.rol1.id)
            print(self.ruta, self.put_data)
            self.resp = c.put(self.ruta, data=self.put_data)
            self.modRol = Rol.query.get(1)
            assert self.resp.status_code in [200,204]
            assert self.modRol.nombre == self.nuevo_nombre

    def test_post_rol(self):
         '''API | POST Rol'''
         #arrange
         _app = AppFactory.create_app(_api, db, self.dbLocation)
         _app.testing = True
         self.nombre_rol = u"Gerente"
         
         #act
         with _app.test_client() as c:
             self.ruta = '/api/rol/'
             self.resp = c.post(self.ruta, data=dict(nombre=self.nombre_rol) )
             assert self.resp.status_code == 201            
             assert Rol.query.filter_by(nombre=self.nombre_rol) is not None
             
    def test_delete_rol(self):
        '''API | DELETE Rol'''
        #arrange
        _app = AppFactory.create_app(_api, db, self.dbLocation)
        _app.testing = True
        self.rol1 = Rol(u"Desarrollador")
        AppFactory.add_test_data(db, [self.rol1])
        #act
        with _app.test_client() as c:
            self.ruta = '/api/rol/' + str(self.rol1.id)
            self.rolesBefore = len(json.loads(c.get('/api/rol/').data))
            self.resp = c.delete(self.ruta)
            self.rolesAfter = len(json.loads(c.get('/api/rol/').data))
        #asserts
            assert self.resp.status_code in [200, 204]
            assert self.rolesBefore == 1
            assert self.rolesAfter == 0