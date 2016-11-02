from flask import Flask
from flask_script import Manager, Shell
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
'mysql://blankspace:BSdev2016!@localhost/codetavern2'

manager = Manager(app)
db = SQLAlchemy(app)

from .model import Cliente

from .views import index

def make_shell_context():
    from .model import populate
    return dict(app = app, db = db, Cliente = Cliente, populate = populate)
manager.add_command("database", Shell(make_context=make_shell_context))
