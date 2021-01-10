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

@posts.route('/<slug>/edit', methods=['POST', 'GET'])
def edit_post(slug):
    post = Post.query.filter(Post.slug==slug).first()

    if request.method == 'POST':
        # Наполнение формы данными
        form = PostForm(formdata=request.form, obj=post)
        # Получение новых данных
        form.populate_obj(post)
        db.session.commit()

        return redirect(url_for('posts.post_detail', slug=post.slug))

    form = PostForm(obj=post)
    return render_template('posts/edit.html', post=post, form=form)


# http://localhost/blog
@posts.route('/')
def index():
    # Pagination
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    # Search
    q = request.args.get('q')
    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q)).all()
    else:
        posts = Post.query.order_by(Post.created.desc())

    # Pagination
    pages = posts.paginate(page=page, per_page=5)

    return render_template('posts/index.html', posts=posts, pages=pages)

# http://localhost/blog /<slug>
@posts.route('/<slug>')
def post_detail(slug):
    # Search
    q = request.args.get('q')
    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q)).all()
        return render_template('posts/index.html', posts=posts)

    post = Post.query.filter(Post.slug==slug).first()
    if post:
        tags = post.tags
        return render_template('posts/post_detail.html', post=post, tags=tags)
    else:
        return redirect(url_for('posts.index'))





