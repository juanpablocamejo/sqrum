from common import db

class UserStory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rol_id = db.Column(db.Integer, db.ForeignKey('rol.id'))
    rol = db.relationship('Rol')
    quiero = db.Column(db.Unicode(500), nullable=False)
    para = db.Column(db.Unicode(500))
    observaciones = db.Column(db.Unicode(1000))
    estado_id = db.Column(db.Integer, nullable=False)
    prioridad = db.Column(db.Integer)
    estimacion = db.Column(db.Integer)

    def __init__(self, rol, quiero, para=None, obs=None, prioridad=None, estimacion=None, estado_id=1):
        self.rol = rol
        self.quiero = quiero
        self.para = para
        self.observaciones = obs
        self.prioridad = prioridad
        self.estimacion = estimacion
        self.estado_id = estado_id
        self.observaciones = obs