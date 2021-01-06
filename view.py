#project
from app import app
#flask
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')
