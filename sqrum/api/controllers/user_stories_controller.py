from flask_restful import Resource, fields, marshal_with, abort, request
from common import _api
from api.models import *

#JSON
us_json = {
    'id': fields.Integer,
    'rol_id': fields.Integer,
    'quiero': fields.String,
    'para': fields.String,
    'estado_id': fields.Integer,
    'estimacion': fields.Integer,
    'prioridad': fields.Integer,
    'observaciones': fields.String,
    'desarrollador_id': fields.Integer,
    'iteracion_id': fields.Integer
}

#Recursos
class StoriesRes(Resource):
    @marshal_with(us_json)
    def get(self):
        return UserStory.query.all()
        
    def post(self):
        args = request.form
        r= Rol.query.get(args['rol_id'])
        us = UserStory(r, args['quiero'], args['para'], args['obs'], args['prioridad'], args['estimacion'], 1)
        db.session.add(us)
        db.session.commit()
        return {'id': us.id}, 201
        
        
_api.add_resource(StoriesRes,'/api/user_story/')

        
class StoryRes(Resource):
    @marshal_with(us_json)    
    def get(self, id):
        res = UserStory.query.get(id)
        if res is None:
            abort(410,message="User story inexistente")
        else:
            return UserStory.query.get(id)
            
    def delete(self, id):
        us = UserStory.query.get(id)
        if not us is None:
            db.session.delete(us)
            db.session.commit()
        return None, 204
        
    def put(self, id):
        us = UserStory.query.get(id)
        if not us is None:
            args = request.form
            if 'quiero' in args: us.quiero = args['quiero']
            if 'para' in args: us.para = args['para']
            if 'estado' in args: us.estado_id = args['estado']
            if 'rol' in args: us.rol = Rol.query.get(args['rol'])
            if 'observaciones' in args: us.observaciones = args['observaciones']
            if 'estimacion' in args: us.estimacion = args['estimacion']
            if 'prioridad' in args: us.prioridad = args['prioridad']
            if 'desarrollador' in args: 
                if args['desarrollador']=='': 
                    us.desarrollador=None
                else: 
                    us.desarrollador = Desarrollador.query.get(args['desarrollador'])
            if 'iteracion' in args: 
                if args['iteracion']=='': 
                    us.iteracion=None
                else:
                    us.iteracion = Iteracion.query.get(args['iteracion'])
            db.session.add(us)
            db.session.commit()
        return None, 204
            
_api.add_resource(StoryRes, '/api/user_story/<int:id>')

