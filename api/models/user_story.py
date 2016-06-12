from orm import db

class UserStory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiero = db.Column(db.String(500), nullable=False)
    para = db.Column(db.String(500), nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('rol.id'))
    rol = db.relationship('Rol')
    estado_id = db.Column(db.Integer)

    def __init__(self, quiero, para, rol):
        self.quiero = quiero
        self.para = para
        self.rol = rol