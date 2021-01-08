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
'''

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())


    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()


    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)


    def __repr__(self):
        return f'<Post id: {self.id}, title: {self.title}>'

