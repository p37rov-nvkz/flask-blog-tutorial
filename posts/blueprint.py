#flask
from flask import Blueprint
from flask import render_template

#project
from models import Post, Tag

posts = Blueprint('posts', __name__, template_folder='templates', static_folder='static')

@posts.route('/')
def index():
    posts = Post.query.all()
    return render_template('posts/index.html', posts=posts)

# http://localhost/blog /<slug>
@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first()
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)

# http://localhost/blog/ tag/<slug>
@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first()
    posts = tag.posts.all()
    return render_template('posts/tag_detail.html', posts=posts, tag=tag)

