#project
from app import app
from app import db
from posts.blueprint import posts
import view


if __name__ == '__main__':
    app.run()
