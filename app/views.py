from . import app, db
from .model import Cliente
from flask import render_template, request


@app.route('/',  methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = list(request.form.keys())[0]
        cliente = Cliente.query.filter_by(nombre=nombre).first()
        cliente.pedidos+=1
        db.session.add(cliente)
        db.session.commit()
    return render_template('index.html', clientes=Cliente.query.all())
