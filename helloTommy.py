from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
'mysql://blankspace:BSdev2016!@localhost/codetavern2'

db = SQLAlchemy(app)

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(32), nullable = False, unique = True)
    pedidos = db.Column(db.Integer, default = 0)

def populate():
    #Crea la base de datos. Si ya está creada, no hace nada
    #(¡aunque la hayamos modificado!)
    db.create_all()

    if Cliente.query.filter_by(nombre='Javi').first() is None:
        javi = Cliente(nombre="Javi", pedidos = 3)
        #Crea un contexto para guardar para usar la variable de entorno session.
        app_ctx = app.app_context()
        app_ctx.push()
        db.session.add(javi)
        db.session.commit()
        app_ctx.pop()

@app.route('/')
def index():
    javi = Cliente.query.filter_by(nombre='Javi').first()
    return "<strong>Hello Tommy!</strong>"+\
    "<br>"+\
    "%s se ha pedido %d cervezas." % (javi.nombre, javi.pedidos)

if __name__ == '__main__':
    populate()
    app.run()
