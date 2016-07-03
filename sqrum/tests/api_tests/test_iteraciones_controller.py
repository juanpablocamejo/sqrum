# -*- coding: utf-8 -*-
from unittest import TestCase
from common import _app, _api, db
from app_factory import AppFactory
import os, tempfile, data, json
from api.models import *
from api.controllers import *
from datetime import date
from dateutil.parser import parse

class IteracionesControllerTests(TestCase):
    def setUp(self):
        if not os.path.exists('./tmp'): 
            os.mkdir('./tmp')
        self.defaultDir = tempfile.mkdtemp(dir='./tmp')
        self.defaultFile = 'index.html'
        self.dbLocation = self.defaultDir + '/temp.db'

    def tearDown(self):
        os.system('sudo rm -f -r ./tmp')
        
    def test_get_iteracion_by_id(self):
        '''API | GET Iteracion por Id'''
        #arrange
        _app = AppFactory.create_app(_api, db, self.dbLocation)
        _app.testing = True
        self.nombre = u"Iteración 1"
        self.inicio = date(2016,1,1)
        self.fin = date(2016,1,14)
        self.ite1 = Iteracion(self.nombre, self.inicio, self.fin)
        AppFactory.add_test_data(db, [self.ite1])
        #act
        with _app.test_client() as c:
            self.ruta = '/api/iteracion/1'
            self.resp = c.get(self.ruta)
            self.respData = json.loads(self.resp.data)
        #asserts
            assert self.resp.status_code == 200
            assert self.respData["id"]==1
            assert self.respData["nombre"]==self.ite1.nombre
            assert parse(self.respData["inicio"]).date()==self.ite1.inicio
            assert parse(self.respData["fin"]).date()==self.ite1.fin
            
    
    def test_get_iteraciones(self):
        '''API | GET Iteraciones'''
        #arrange
        _app = AppFactory.create_app(_api, db, self.dbLocation)
        _app.testing = True
        self.nombre1 = u"Iteración 1"
        self.nombre2 = u"Iteración 2"
        self.inicio1 = date(2016,1,1)
        self.fin1 = date(2016,1,14)
        self.inicio2 = date(2016,1,15)
        self.fin2 = date(2016,1,29)
        self.ite1 = Iteracion(self.nombre1, self.inicio1, self.fin1)
        self.ite2 = Iteracion(self.nombre2, self.inicio2, self.fin2)
        AppFactory.add_test_data(db, [self.ite1, self.ite2])
        #act
        with _app.test_client() as c:
            self.ruta = '/api/iteracion/'
            self.resp = c.get(self.ruta)
        #asserts
            assert self.resp.status_code == 200
            assert len(json.loads(self.resp.data))==2
            assert json.loads(self.resp.data)[0]['id'] == self.ite1.id
            assert json.loads(self.resp.data)[1]['id'] == self.ite2.id
            
    def test_put_iteracion(self):
        '''API | PUT Iteracion'''
        #arrange
        _app = AppFactory.create_app(_api, db, self.dbLocation)
        _app.testing = True
        self.nombre = u"Iteración 2"
        self.inicio = date(2016,1,1)
        self.fin = date(2016,1,14)
        self.modNombre = u"Iteración 3"
        self.modInicio = "2016-01-02"
        self.modFin = "2016-01-15"
        self.ite1 = Iteracion(self.nombre, self.inicio, self.fin)
        self.put_data = dict(nombre=self.modNombre, inicio=self.modInicio,fin=self.modFin)
        AppFactory.add_test_data(db, [self.ite1])
        #act
        with _app.test_client() as c:
            self.ruta = '/api/iteracion/' + str(self.ite1.id)
            print(self.ruta, self.put_data)
            self.resp = c.put(self.ruta, data=self.put_data)
            self.modifiedIte = Iteracion.query.get(1)
            assert self.resp.status_code in [200,204]
            assert self.modifiedIte.nombre == self.modNombre
            assert self.modifiedIte.inicio == parse(self.modInicio).date()
            assert self.modifiedIte.fin == parse(self.modFin).date()

    def test_post_iteracion(self):
         '''API | POST Iteracion'''
         #arrange
         _app = AppFactory.create_app(_api, db, self.dbLocation)
         _app.testing = True
         self.nombre = u"Iteración 1"
         self.inicio = '2016-07-01'
         self.fin = '2016-07-10'
         self.data = dict(nombre=self.nombre,inicio=self.inicio,fin=self.fin)
         
         #act
         with _app.test_client() as c:
             self.ruta = '/api/iteracion/'
             self.resp = c.post(self.ruta, data=self.data)
             self.ite = Iteracion.query.get(1)
             assert self.resp.status_code == 201  
             assert self.ite.nombre == self.nombre
             assert self.ite.inicio == parse(self.inicio).date()
             assert self.ite.fin == parse(self.fin).date()
             
             
    def test_delete_iteracion(self):
        '''API | DELETE Iteracion'''
        #arrange
        _app = AppFactory.create_app(_api, db, self.dbLocation)
        _app.testing = True
        self.ite1 = Iteracion(u"Iteracion",date(2016,1,1),date(2016,1,2))
        AppFactory.add_test_data(db, [self.ite1])
        #act
        with _app.test_client() as c:
            self.ruta = '/api/iteracion/' + str(self.ite1.id)
            self.iteracionesAntes = len(json.loads(c.get('/api/iteracion/').data))
            self.resp = c.delete(self.ruta)
            self.iteracionesDespues = len(json.loads(c.get('/api/iteracion/').data))
        #asserts
            assert self.resp.status_code in [200, 204]
            assert self.iteracionesAntes == 1
            assert self.iteracionesDespues == 0
            
    def test_delete_iteracion_asignado(self):
        '''API | DELETE Iteracion Con Stories'''
        #arrange
        _app = AppFactory.create_app(_api, db, self.dbLocation)
        _app.testing = True
        self.ite1 = Iteracion(u"Iteracion",date(2016,1,1),date(2016,1,2))
        self.rol = Rol(u"UnRol")
        self.us1 = UserStory(self.rol, u'Agregar una User Story', para=u'Agregar funcionalidad al sistema', obs=u'Observaciones', prioridad=1, estimacion=2)
        self.us1.iteracion = self.ite1
        AppFactory.add_test_data(db, [self.ite1, self.rol, self.us1])
        #act
        with _app.test_client() as c:
            self.ruta = '/api/iteracion/' + str(self.ite1.id)
            self.iteracionesAntes = len(json.loads(c.get('/api/iteracion/').data))
            self.resp = c.delete(self.ruta)
            self.iteracionesDespues = len(json.loads(c.get('/api/iteracion/').data))
            self.us1 = UserStory.query.get(1)
        #asserts
            assert self.resp.status_code in [200, 204]
            assert self.iteracionesAntes == 1
            assert self.iteracionesDespues == 0
            assert self.us1.iteracion is None