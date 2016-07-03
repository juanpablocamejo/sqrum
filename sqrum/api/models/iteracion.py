from common import db

class Iteracion(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.Unicode)
    inicio = db.Column(db.Date)
    fin = db.Column(db.Date)
    
    def __init__(self, nombre, inicio=None, fin=None):
        self.nombre = nombre
        self.inicio = inicio
        self.fin = fin