from flask_restful import Resource, fields, marshal_with, abort, request
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
    
    def post(self):
        args = request.form
        r = Rol(args['nombre'])
        db.session.add(r)
        db.session.commit()
        return {'id': r.id}, 201
        
_api.add_resource(RolesRes,'/api/rol/')

        
class RolRes(Resource):
    @marshal_with(rol_json)    
    def get(self, id):
        res = Rol.query.get(id)
        if res is None:
            abort(410,message="Rol inexistente")
        else:
            return Rol.query.get(id)
    
    def delete(self, id):
        r = Rol.query.get(id)
        if not r is None:
            db.session.delete(r)
            db.session.commit()
        return None, 204
        
    def put(self, id):
        r = Rol.query.get(id)
        args = request.form
        if 'nombre' in args: r.nombre = args['nombre']
        db.session.add(r)
        db.session.commit()
        return None, 204
        
_api.add_resource(RolRes, '/api/rol/<int:id>')