#flask
from flask import Blueprint, redirect, url_for
from flask import render_template

#project
from models import Post, Tag

tags = Blueprint('tags', __name__, template_folder='templates', static_folder='../static')

@tags.route('/')
def index():
    tags = Tag.query.all()
    return render_template('tags/index.html', tags=tags)

# http://localhost/ tag/<slug>
@tags.route('/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first()
    posts = tag.posts.all()
    return render_template('tags/tag_detail.html', posts=posts, tag=tag)

