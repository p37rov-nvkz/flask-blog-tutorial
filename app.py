#flask
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
#flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
#flask_migrate
from flask_migrate import Migrate, MigrateCommand
#flask_script
from flask_script import Manager
#flask_admin
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
#flask_security
from flask_security import SQLAlchemySessionUserDatastore
from flask_security import Security
from flask_security import current_user
#project
from config import DevelopmentConfig



app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)

from models import Post
from models import Tag

from models import User
from models import Role

class AdminView(ModelView):
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))

class HomeAdminView(AdminIndexView):
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))



migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

admin = Admin(app, 'FlaskApp', url='/', index_view=HomeAdminView(name='Home'))
admin.add_view(AdminView(Post, db.session))
admin.add_view(AdminView(Tag, db.session))

user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
security = Security(app, user_datastore)


