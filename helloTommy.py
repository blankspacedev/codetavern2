from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
'mysql://blankspace:BSdev2016!@localhost/codetavern2'

db = SQLAlchemy(app)

@app.route('/')
def index():
    javi = Cliente.query.filter_by(nombre='Javi').first()
    return "<strong>Hello Tommy!</strong>"+\
    "<br>"+\
    "%s se ha pedido %d cervezas." % (javi.nombre, javi.pedidos)

if __name__ == '__main__':
    from model import Cliente
    app.run()
