#stdlib
import os

class DevelopmentConfig(object):
    """
    Development configurations
    """
    DEBUG = True

    #DATABASE SETTINGS
    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_NAME = 'flask_blog_tutorial_db'
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}"

    #SQLALCHEMY_ECHO = True
    #ASSETS_DEBUG = True
    #DATABASE = 'teamprojet_db'
    print('THIS APP IS IN DEBUG MODE. YOU SHOULD NOT SEE THIS IN PRODUCTION.')


class ProductionConfig(object):
    """
    Production configurations
    """
    DEBUG = False
    DATABASE = 'teamprojet_prod_db'