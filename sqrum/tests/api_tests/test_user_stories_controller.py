# -*- coding: utf-8 -*-
import unittest
from common import _app, _api, db
from app_factory import AppFactory
import os, tempfile, data, json
from api.models import *
from api.controllers import *

class UserStoriesControllerTests(unittest.TestCase):
    def setUp(self):
        if not os.path.exists('./tmp'): 
            os.mkdir('./tmp')
        self.defaultDir = tempfile.mkdtemp(dir='./tmp')
        self.defaultFile = 'index.html'
        self.dbLocation = self.defaultDir + '/temp.db'
        self.rol = Rol(u"Desarrollador")
        self.us1 = UserStory(self.rol, u'Agregar una User Story', para=u'Agregar funcionalidad al sistema', obs=u'Observaciones', prioridad=1, estimacion=2)
        self.us2 = UserStory(self.rol, u'Cambiar el estado a una user story', para=u'Registrar lo que hago como desarrollador y que sea visible al resto del equipo', obs=u'Observaciones', prioridad=1, estimacion=2)

    def tearDown(self):
        os.system('sudo rm -f -r ./tmp')
        
    def test_get_user_story_by_id(self):
        '''API | GET User Story por Id'''
        #arrange
        _app = AppFactory.create_app(_api, db, self.dbLocation)
        _app.testing = True
        AppFactory.add_test_data(db, [self.rol,self.us1])
        #act
        with _app.test_client() as c:
            self.ruta = '/api/user_story/' + str(self.us1.id)
            self.resp = c.get(self.ruta)
        #assert
        assert self.resp.status_code == 200
        assert json.loads(self.resp.data)['id']==self.us1.id
        assert json.loads(self.resp.data)['quiero']==self.us1.quiero
        assert json.loads(self.resp.data)['para']==self.us1.para
        #assert json.loads(self.resp.data)['rol_id']==self.rol.id
        
    def test_get_user_stories(self):
        '''API | GET User Stories'''
        #arrange
        _app = AppFactory.create_app(_api, db, self.dbLocation)
        _app.testing = True
        AppFactory.add_test_data(db, [self.rol, self.us1, self.us2])
        #act
        with _app.test_client() as c:
            self.ruta = '/api/user_story/'
            self.resp = c.get(self.ruta)
        #assert
        assert self.resp.status_code == 200
        assert len(json.loads(self.resp.data))==2
        assert json.loads(self.resp.data)[0]['id'] == self.us1.id
        assert json.loads(self.resp.data)[1]['id'] == self.us2.id
        assert json.loads(self.resp.data)[0]['quiero'] == self.us1.quiero
        assert json.loads(self.resp.data)[1]['quiero'] == self.us2.quiero
        # assert json.loads(self.resp.data)[0]['rol_id'] == self.rol.id
        # assert json.loads(self.resp.data)[1]['rol_id'] == self.rol.id
        
    def test_post_user_story(self):
        '''API | POST User Story'''
        #arrange
        _app = AppFactory.create_app(_api, db, self.dbLocation)
        _app.testing = True
        AppFactory.add_test_data(db, [self.rol])
        self.data = dict(quiero=self.us1.quiero, para=self.us1.para, obs=self.us1.observaciones, 
        rol_id=self.rol.id, estimacion=self.us1.estimacion, prioridad=self.us1.prioridad)
        #act
        with _app.test_client() as c:
            self.ruta = '/api/user_story/'
            self.resp = c.post(self.ruta, data=self.data)
            self.jsonResp = json.loads(self.resp.data)
            self.createdUS=UserStory.query.get(1)
        #assert
        assert self.resp.status_code == 201
        assert self.jsonResp['id'] == 1
        assert self.createdUS.quiero == self.us1.quiero
        assert self.createdUS.para == self.us1.para
        assert self.createdUS.estimacion == self.us1.estimacion
        assert self.createdUS.prioridad == self.us1.prioridad
        
    def test_delete_user_story(self):
        '''API | DELETE User Story'''
        #arrange
        _app = AppFactory.create_app(_api, db, self.dbLocation)
        _app.testing = True
        AppFactory.add_test_data(db, [self.rol, self.us1])
        #act
        with _app.test_client() as c:
            self.ruta = '/api/user_story/' + str(self.us1.id)
            self.storiesBefore = len(json.loads(c.get('/api/user_story/').data))
            self.resp = c.delete(self.ruta)
            self.storiesAfter = len(json.loads(c.get('/api/user_story/').data))
            
        #assert
        assert self.resp.status_code in [200, 204]
        assert self.storiesBefore == 1
        assert self.storiesAfter == 0
        
    def test_put_user_story(self):
        '''API | PUT User Story'''
        #arrange
        _app = AppFactory.create_app(_api, db, self.dbLocation)
        _app.testing = True
        AppFactory.add_test_data(db, [self.rol, self.us1])
        self.modQuiero = "quiero modificado"
        self.modPara = "para modificado"
        self.modEstado = 2
        self.data = dict(quiero=self.modQuiero, para=self.modPara, estado=self.modEstado)
        #act
        with _app.test_client() as c:
            self.ruta = '/api/user_story/1'
            self.resp = c.put(self.ruta, data=self.data)
            self.modifiedUS=UserStory.query.get(1)
        #assert
        
        assert self.resp.status_code in [200, 204]
        assert self.modifiedUS.quiero == self.modQuiero
        assert self.modifiedUS.para == self.modPara
        assert self.modifiedUS.estado_id == self.modEstado