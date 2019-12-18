class Config(object):
    SECRET_KEY = 'dev'
    FLASK_ENV = 'development'
    # 设置连接数据库的URL
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/flask_note'
    # 设置每次请求结束后会自动提交数据库的改动
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 查询时显示原始SQL语句
    SQLALCHEMY_ECHO = False
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True