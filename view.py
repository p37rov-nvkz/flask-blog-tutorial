#project
from app import app
from models import Post
#flask
from flask import render_template
from flask import request


@app.route('/')
def index():
    q = request.args.get('q')
    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q)).all()
        return render_template('posts/index.html', posts=posts)
    else:
        return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404