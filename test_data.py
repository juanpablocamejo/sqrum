from api.models import *
from orm import db

def insertar_datos():
    roles = [Rol("Usuario"), Rol("Administrador")]

    for r in roles:
        db.session.add(r)
    
    db.session.commit()