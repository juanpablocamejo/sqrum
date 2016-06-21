from flask import Flask
import os
from modulos.modulo_de_prueba import *

app = Flask(__name__)
app.debug = True
@app.route('/')
def index():
    obj = ClaseDePrueba()
    return obj.saluda()
    
if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)