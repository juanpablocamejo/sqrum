from common import db

class Desarrollador(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.Unicode, nullable=False)
    
    def __init__(self, nombre):
        self.nombre = nombre