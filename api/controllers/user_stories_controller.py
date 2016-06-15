from flask_restful import Resource, fields, marshal_with, abort
from flask import make_response
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