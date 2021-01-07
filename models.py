#stdlib
from datetime import datetime
import zlib

#project
from app import db

def slugify(s):
    return zlib.crc32(s.encode('cp1251'))

# TODO:
'''
Написать тесты для этого кода:

>>> import models
THIS APP IS IN DEBUG MODE. YOU SHOULD NOT SEE THIS IN PRODUCTION.
>>> from app import db
>>> db.create_all()
>>> from models import Post
>>> p = Post(title='First post', body='First post body')
>>> db.session.add(p)
>>> db.session.commit()
>>> p
<Post id: 1, title: First post>
>>> p.slug
slug
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

