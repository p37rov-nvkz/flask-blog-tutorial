#flask
from flask import Blueprint, redirect, url_for
from flask import render_template
from flask import request

#project
from models import Post, Tag

tags = Blueprint('tags', __name__, template_folder='templates', static_folder='../static')

@tags.route('/')
def index():
    # Search
    q = request.args.get('q')
    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q)).all()
        return render_template('posts/index.html', posts=posts)
    
    tags = Tag.query.all()
    return render_template('tags/index.html', tags=tags)

# http://localhost/ tag/<slug>
@tags.route('/<slug>')
def tag_detail(slug):
    # Search
    q = request.args.get('q')
    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q)).all()
        return render_template('posts/index.html', posts=posts)

    tag = Tag.query.filter(Tag.slug==slug).first()
    if tag:
        posts = tag.posts.all()
        return render_template('tags/detail.html', posts=posts, tag=tag)
    else:
        return redirect(url_for('tags.index'))

