from . import db

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(32), nullable = False, unique = True)
    pedidos = db.Column(db.Integer, default = 0)


def populate():
    #Crea la base de datos. Si ya está creada, no hace nada
    #(¡aunque la hayamos modificado!)
    #Ahora primero borramos el esquema y después lo recreamos!
    db.drop_all()
    db.create_all()

    if Cliente.query.filter_by(nombre='Javi').first() is None:
        javi = Cliente(nombre="Javi", pedidos = 3)
        jacinto = Cliente(nombre="Jacinto", pedidos = 5)
        db.session.add_all([javi, jacinto])
        db.session.commit()
