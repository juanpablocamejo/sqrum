from flask_restful import Resource, fields, marshal_with, abort
from web_api import _api
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
        
class RolRes(Resource):
    @marshal_with(rol_json)    
    def get(self, rol_id):
        res = Rol.query.get(rol_id)
        if res is None:
            abort(410,message="Rol inexistente")
        else:
            return Rol.query.get(rol_id)
            
        
_api.add_resource(RolesRes,'/api/rol/')
_api.add_resource(RolRes,'/api/rol/<int:rol_id>')