# -*- coding: utf-8 -*-
from unittest import TestCase
from common import _app, _api, db
from app_factory import AppFactory
import os, tempfile, data, json
from api.models import *
from api.controllers import *

class DesarrolladoresControllerTests(TestCase):
    def setUp(self):
        if not os.path.exists('./tmp'): 
            os.mkdir('./tmp')
        self.defaultDir = tempfile.mkdtemp(dir='./tmp')
        self.defaultFile = 'index.html'
        self.dbLocation = self.defaultDir + '/temp.db'


    def tearDown(self):
        os.system('sudo rm -f -r ./tmp')
        
    def test_get_desarrollador_by_id(self):
        '''API | GET Desarrollador por Id'''
        #arrange
        _app = AppFactory.create_app(_api, db, self.dbLocation)
        _app.testing = True
        self.des1 = Desarrollador(u"Juan")
        self.des2 = Desarrollador(u"Pedro")
        AppFactory.add_test_data(db, [self.des1, self.des2])
        #act
        with _app.test_client() as c:
            self.ruta = '/api/desarrollador/' + str(self.des1.id)
            self.resp = c.get(self.ruta)
        #asserts
            assert self.resp.status_code == 200
            assert json.loads(self.resp.data)['id']==self.des1.id
            assert json.loads(self.resp.data)['nombre']==self.des1.nombre
    
    def test_get_desarrolladores(self):
        '''API | GET Desarrolladores'''
        #arrange
        _app = AppFactory.create_app(_api, db, self.dbLocation)
        _app.testing = True
        self.des1 = Desarrollador(u"Juan")
        self.des2 = Desarrollador(u"Pedro")
        AppFactory.add_test_data(db, [self.des1, self.des2])
        #act
        with _app.test_client() as c:
            self.ruta = '/api/desarrollador/'
            self.resp = c.get(self.ruta)
        #asserts
            assert self.resp.status_code == 200
            assert len(json.loads(self.resp.data))==2
            assert json.loads(self.resp.data)[0]['id'] == self.des1.id
            assert json.loads(self.resp.data)[1]['id'] == self.des2.id
            
    def test_put_desarrollador(self):
        '''API | PUT Desarrollador'''
        #arrange
        _app = AppFactory.create_app(_api, db, self.dbLocation)
        _app.testing = True
        self.des1 = Desarrollador(u"Juan")
        self.nuevo_nombre = u"Miembro del equipo"
        self.put_data = dict(nombre=self.nuevo_nombre)
        AppFactory.add_test_data(db, [self.des1])
        #act
        with _app.test_client() as c:
            self.ruta = '/api/desarrollador/' + str(self.des1.id)
            print(self.ruta, self.put_data)
            self.resp = c.put(self.ruta, data=self.put_data)
            self.modDesarrollador = Desarrollador.query.get(1)
            assert self.resp.status_code in [200,204]
            assert self.modDesarrollador.nombre == self.nuevo_nombre

    def test_post_desarrollador(self):
         '''API | POST Desarrollador'''
         #arrange
         _app = AppFactory.create_app(_api, db, self.dbLocation)
         _app.testing = True
         self.nombre_des = u"Pablo"
         
         #act
         with _app.test_client() as c:
             self.ruta = '/api/desarrollador/'
             self.resp = c.post(self.ruta, data=dict(nombre=self.nombre_des) )
             assert self.resp.status_code == 201            
             assert Desarrollador.query.filter_by(nombre=self.nombre_des) is not None
             
    def test_delete_desarrollador(self):
        '''API | DELETE Desarrollador'''
        #arrange
        _app = AppFactory.create_app(_api, db, self.dbLocation)
        _app.testing = True
        self.des1 = Desarrollador(u"Juan")
        AppFactory.add_test_data(db, [self.des1])
        #act
        with _app.test_client() as c:
            self.ruta = '/api/desarrollador/' + str(self.des1.id)
            self.desarrolladoresAntes = len(json.loads(c.get('/api/desarrollador/').data))
            self.resp = c.delete(self.ruta)
            self.desarrolladoresDespues = len(json.loads(c.get('/api/desarrollador/').data))
        #asserts
            assert self.resp.status_code in [200, 204]
            assert self.desarrolladoresAntes == 1
            assert self.desarrolladoresDespues == 0
            
    def test_delete_desarrollador_asignado(self):
        '''API | DELETE Desarrollador Asignado'''
        #arrange
        _app = AppFactory.create_app(_api, db, self.dbLocation)
        _app.testing = True
        self.des1 = Desarrollador(u"Juan")
        self.rol = Rol(u"Desarrollador")
        self.us1 = UserStory(self.rol, u'Agregar una User Story', para=u'Agregar funcionalidad al sistema', obs=u'Observaciones', prioridad=1, estimacion=2)
        self.us1.desarrollador = self.des1
        AppFactory.add_test_data(db, [self.des1, self.rol ,self.us1])
        #act
        with _app.test_client() as c:
            self.ruta = '/api/desarrollador/' + str(self.des1.id)
            self.desarrolladoresAntes = len(json.loads(c.get('/api/desarrollador/').data))
            self.resp = c.delete(self.ruta)
            self.desarrolladoresDespues = len(json.loads(c.get('/api/desarrollador/').data))
            self.us1 = UserStory.query.get(1)
        #asserts
            assert self.resp.status_code in [200, 204]
            assert self.desarrolladoresAntes == 1
            assert self.desarrolladoresDespues == 0
            assert self.us1.desarrollador is None