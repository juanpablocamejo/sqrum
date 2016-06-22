# -*- coding: utf-8 -*-
from common import db

class Rol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.Unicode(200), nullable=False)

    def __init__(self, nombre):
        self.nombre = nombre