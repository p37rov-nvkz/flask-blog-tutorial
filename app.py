#project
from config import DevelopmentConfig
from posts.blueprint import posts
#flask
from flask import Flask

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

app.register_blueprint(posts, url_prefix='/blog')




