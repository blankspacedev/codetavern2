from . import app
from .model import Cliente

@app.route('/')
def index():
    javi = Cliente.query.filter_by(nombre='Javi').first()
    return "<strong>Hello Tommy!</strong>"+\
    "<br>"+\
    "%s se ha pedido %d cervezas." % (javi.nombre, javi.pedidos)
