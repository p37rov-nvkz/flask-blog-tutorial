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
from flask_admin.contrib.sqla import ModelView
#project
from config import DevelopmentConfig


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)

from models import Post
from models import Tag


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

admin = Admin(app)
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Tag, db.session))




