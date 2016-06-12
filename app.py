import os
from flask import Flask
from flask_restful import Api
from orm import db
import test_data
from api.controllers import *
from api.models import *

#init Flask WebApp
_app = Flask(__name__)
_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqrum.db'

#init Flask_restful API
_api.init_app(_app)

#init SQLAlchemy ORM
db.init_app(_app)

with _app.app_context():
     db.drop_all()
     db.create_all()
     test_data.insertar_datos()

if __name__ == '__main__':
     port = int(os.getenv('PORT', 8080))
     host = os.getenv('IP', '0.0.0.0')
     _app.run(port=port, host=host, debug=True)