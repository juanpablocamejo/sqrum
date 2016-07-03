from flask_restful import Resource, fields, marshal_with, abort, request
from common import _api
from api.models import *
from dateutil.parser import parse
#JSON
iteracion_json = {
    'id': fields.Integer,
    'nombre': fields.String,
    'inicio': fields.String,
    'fin': fields.String
}

#Recursos
class IteracionesRes(Resource):
    @marshal_with(iteracion_json)
    def get(self):
        return Iteracion.query.all()
    
    def post(self):
        args = request.form
        i = Iteracion(args['nombre'])
        if 'inicio' in args: i.inicio = parse(args['inicio']).date()
        if 'fin' in args: i.fin = parse(args['fin']).date()
        db.session.add(i)
        db.session.commit()
        return {'id': i.id}, 201
        
_api.add_resource(IteracionesRes,'/api/iteracion/')

        
class IteracionRes(Resource):
    @marshal_with(iteracion_json)    
    def get(self, id):
        res = Iteracion.query.get(id)
        if res is None:
            abort(410,message="Iteracion inexistente")
        else:
            return Iteracion.query.get(id)
    
    def delete(self, id):
        i = Iteracion.query.get(id)
        if not i is None:
            db.session.delete(i)
            db.session.commit()
        return None, 204
        
    def put(self, id):
        i = Iteracion.query.get(id)
        args = request.form
        if 'nombre' in args: i.nombre = args['nombre']
        if 'inicio' in args: i.inicio = parse(args['inicio']).date()
        if 'fin' in args: i.fin = parse(args['fin']).date()
        db.session.add(i)
        db.session.commit()
        return None, 204
        
_api.add_resource(IteracionRes, '/api/iteracion/<int:id>')