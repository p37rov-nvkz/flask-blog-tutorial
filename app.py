#flask
from flask import Flask
#flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
#flask_migrate
from flask_migrate import Migrate, MigrateCommand
#flask_script
from flask_script import Manager
#project
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)




