import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqrum.db'
db = SQLAlchemy(app)

from api.models import *
from api.controllers import *

db.create_all()

if __name__ == '__main__':
     port = int(os.getenv('PORT', 8080))
     host = os.getenv('IP', '0.0.0.0')
     app.run(port=port, host=host)