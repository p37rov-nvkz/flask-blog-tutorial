#project
from app import app
from app import db
from posts.blueprint import posts
from tags.blueprint import tags
import view

app.register_blueprint(posts, url_prefix='/blog')
app.register_blueprint(tags, url_prefix='/tags')


if __name__ == '__main__':
    app.run()
