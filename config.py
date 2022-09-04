import  os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "chaihongjing"
    SSL_REDIRECT = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    FLASKY_PER_PAGE = 10
    SQLALCHEMY_POOL_SIZE = 5

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:11111111@127.0.0.1:5306/flaskvue"

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:11111111@127.0.0.1:3306/flaskvueadmin"

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:11111111@172.19.0.3:3306/flaskvueadmin"

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
