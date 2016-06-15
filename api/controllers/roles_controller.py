from flask_restful import Resource, fields, marshal_with, abort
from common import _api
from api.models import *

#JSON
rol_json = {
    'id': fields.Integer,
    'nombre':   fields.String
}

#Recursos
class RolesRes(Resource):
    @marshal_with(rol_json)
    def get(self):
        return Rol.query.all()
        
_api.add_resource(RolesRes,'/api/rol/')

        
class RolRes(Resource):
    @marshal_with(rol_json)    
    def get(self, id):
        res = Rol.query.get(id)
        if res is None:
            abort(410,message="Rol inexistente")
        else:
            return Rol.query.get(id)
            
_api.add_resource(RolRes, '/api/rol/<int:id>')