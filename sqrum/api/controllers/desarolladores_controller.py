from flask_restful import Resource, fields, marshal_with, abort, request
from common import _api
from api.models import *

#JSON
desarrollador_json = {
    'id': fields.Integer,
    'nombre':   fields.String
}

#Recursos
class DesarrolladoresRes(Resource):
    @marshal_with(desarrollador_json)
    def get(self):
        return Desarrollador.query.all()
    
    def post(self):
        args = request.form
        r = Desarrollador(args['nombre'])
        db.session.add(r)
        db.session.commit()
        return {'id': r.id}, 201
        
_api.add_resource(DesarrolladoresRes,'/api/desarrollador/')

        
class DesarrolladorRes(Resource):
    @marshal_with(desarrollador_json)    
    def get(self, id):
        res = Desarrollador.query.get(id)
        if res is None:
            abort(410,message="Desarrollador inexistente")
        else:
            return Desarrollador.query.get(id)
    
    def delete(self, id):
        d = Desarrollador.query.get(id)
        if not d is None:
            db.session.delete(d)
            db.session.commit()
        return None, 204
    
    # def deleteFromStories(self,des):
    #     us = UserStory.query.filter_by(desarrollador = d)
    #     for u in us:
    #          u.desarrollador = None
    #          db.session.add(u)
    #     db.session.commit()
    
    def put(self, id):
        r = Desarrollador.query.get(id)
        args = request.form
        if 'nombre' in args: r.nombre = args['nombre']
        db.session.add(r)
        db.session.commit()
        return None, 204
        
_api.add_resource(DesarrolladorRes, '/api/desarrollador/<int:id>')