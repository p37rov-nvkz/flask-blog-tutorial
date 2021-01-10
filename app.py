#flask
from flask import Flask
#flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
#flask_migrate
from flask_migrate import Migrate, MigrateCommand
#flask_script
from flask_script import Manager
#flask_admin
from flask_admin import Admin
#project
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

admin = Admin(app)




