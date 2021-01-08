#flask
from flask import Flask
#flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
#project
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)





