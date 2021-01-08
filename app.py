#project
from config import DevelopmentConfig
#flask
from flask import Flask
#flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)

app.register_blueprint(posts, url_prefix='/blog')




