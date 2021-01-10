#stdlib
from datetime import datetime
import zlib

#project
from app import db

def slugify(s):
    return zlib.crc32(s.encode('cp1251'))

'''
Create:

>>> from models import Post
>>> p = Post(title="First post", body="First post body")
>>> db.session.add(p)
>>> db.session.commit()

Find query all:

>>> posts = Post.query.all()
>>> posts
[<Post id: 1, title: First post>, <Post id: 2, title: Second post>, <Post id: 3, title: Third post>]

Post query filter all:

>>> p2 = Post.query.filter(Post.title.contains('second')).all()
>>> p2
[<Post id: 2, title: Second post>]

Возвращаемые значения:

>>> type(p2)
<class 'list'>
>>> len(p2)
1
>>> p2[0]
<Post id: 2, title: Second post>
>>> type(p2[0])
<class 'models.Post'>
>>> p2[0].title
'Second post'
>>> p2[0].body
'Second post body'

Поиск точного соответствия:

>>> p3 = Post.query.filter(Post.title=="!").all()

Работа с обьектами BaseQuery:

>>> post1 = Post.query.filter(Post.id==1)
>>> post1
<flask_sqlalchemy.BaseQuery object at 0x7feb8bf03fa0>
>>> post1.count()
1
>>> post1 = post1.first()
>>> post1
<Post id: 1, title: First post>

Ассоциирование поста с тегом:

>>> from models import Post, Tag
>>> t = Tag.query.first()
>>> post1.tags
[]
>>> post1.tags.append(t)
>>> post1.tags
[<Tag id: 1, name: flask>]

>>> t.posts
<sqlalchemy.orm.dynamic.AppenderBaseQuery object at 0x7feb8ed3d040>
>>> t.posts.all()
[<Post id: 1, title: First post>]
>>> t.posts.first()
<Post id: 1, title: First post>

'''

# ManyToMany implementation
post_tags = db.Table('post_tags',
                     db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')))
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())


    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic')) #lazy='dynamic' return BaseQuery

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title + self.body)


    def __repr__(self):
        return f'title: {self.title}>'


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return f'{self.name}>'

