from . import app
from .model import Cliente
from flask import render_template

@app.route('/')
def index():
    javi = Cliente.query.filter_by(nombre='Javi').first()
    return "<strong>Hello Tommy!</strong>"+\
    "<br>"+\
    "%s se ha pedido %d cervezas." % (javi.nombre, javi.pedidos)


@app.route('/other')
def index2():
    javi = Cliente.query.filter_by(nombre='Javi').first()
    return render_template('index.html', nombre=javi.nombre, \
    numCervezas = javi.pedidos)
