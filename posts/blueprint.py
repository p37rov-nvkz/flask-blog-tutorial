#flask
from flask import Blueprint
from flask import render_template
from flask import request

#project
from models import Post, Tag

posts = Blueprint('posts', __name__, template_folder='templates', static_folder='../static')

@posts.route('/')
def index():
    q = request.args.get('q')
    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q)).all()
    else:
        posts = Post.query.all()
    return render_template('posts/index.html', posts=posts)




# http://localhost/blog /<slug>
@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first()
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)



