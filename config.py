class DevelopmentConfig(object):
    """
    Development configurations
    """
    DEBUG = True
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