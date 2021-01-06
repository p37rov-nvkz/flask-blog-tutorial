#project
from config import DevelopmentConfig
#flask
from flask import Flask

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)




