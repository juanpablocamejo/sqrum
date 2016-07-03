from common import db

class Iteracion(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    inicio = db.Column(db.Date)
    fin = db.Column(db.Date)
    
    def __init__(self, inicio=None, fin=None):
        self.inicio = inicio
        self.fin = fin