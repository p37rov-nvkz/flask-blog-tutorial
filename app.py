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

class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))

class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super(BaseModelView, self).on_model_change(form, model, is_created)

class AdminView(AdminMixin, ModelView):
    pass

class HomeAdminView(AdminMixin, AdminIndexView):
    pass

class PostAdminView(AdminMixin, BaseModelView):
    form_columns = ['title','tags', 'body']

class TagAdminView(AdminMixin, BaseModelView):
    form_columns = ['name', 'posts']



migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

admin = Admin(app, 'FlaskApp', url='/', index_view=HomeAdminView(name='Home'))
admin.add_view(PostAdminView(Post, db.session))
admin.add_view(TagAdminView(Tag, db.session))

user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
security = Security(app, user_datastore)


