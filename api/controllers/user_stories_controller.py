from flask_restful import Resource, fields, marshal_with, abort, request
from common import _api
from api.models import *

#JSON
us_json = {
    'us_id': fields.Integer,
    'rol.nombre': fields.String,
    'rol_id': fields.Integer,
    'quiero': fields.String,
    'para': fields.String,
    'estado_id': fields.Integer,
    'estimacion': fields.Integer,
    'prioridad': fields.Integer
}

#Recursos
class StoriesRes(Resource):
    @marshal_with(us_json)
    def get(self):
        return UserStory.query.all()
        
    def post(self):
        args = request.form
        print(args)
        r= Rol.query.get(args['rol_id'])
        us = UserStory(r, args['quiero'], args['para'], args['obs'], args['prioridad'], args['estimacion'], args['estado_id'])
        db.session.add(us)
        db.session.commit()
        return us.us_id, 201
        
_api.add_resource(StoriesRes,'/api/user_story/')

        
class StoryRes(Resource):
    @marshal_with(us_json)    
    def get(self, id):
        res = UserStory.query.get(id)
        if res is None:
            abort(410,message="User story inexistente")
        else:
            return UserStory.query.get(id)
            
_api.add_resource(StoryRes, '/api/user_story/<int:id>')