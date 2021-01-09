#flask
from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

#project
from models import Post
from .forms import PostForm
from app import db

posts = Blueprint('posts', __name__, template_folder='templates', static_folder='../static')


# http://localhost/blog /create
@posts.route('/create', methods=['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            db.session.commit()
        except:
            print('Не удалось добавить пост')

        return redirect(url_for('posts.index'))

    form = PostForm()
    return render_template('posts/create.html', form=form)


# http://localhost/blog
@posts.route('/')
def index():
    # Search
    q = request.args.get('q')
    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q)).all()
    else:
        posts = Post.query.order_by(Post.created.desc())
    return render_template('posts/index.html', posts=posts)


# http://localhost/blog /<slug>
@posts.route('/<slug>')
def post_detail(slug):
    # Search
    q = request.args.get('q')
    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q)).all()
        return render_template('posts/index.html', posts=posts)

    post = Post.query.filter(Post.slug==slug).first()
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)



