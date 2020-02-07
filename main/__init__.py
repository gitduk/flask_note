from main.models import db, init_db
from flask import Flask, app


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance init, if it exists, when not testing
        app.config.from_object(Config)
    else:
        # load the test init if passed in
        app.config.from_pyfile(test_config)

    # init app
    db.init_app(app)

    # init db
    init_db(app)

    # register blueprint
    from main.views.note.user import user_bp
    from main.views.note.index import index_bp
    from main.views.wchat.msg_view import wct
    app.register_blueprint(user_bp)
    app.register_blueprint(index_bp)
    app.register_blueprint(wct)

    return app


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
    # REDIS_URL = 'redis://127.0.0.1:6379/0'
    CACHE_TYPE = 'redis'
    CACHE_REDIS_HOST = '127.0.0.1'
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = ''
    CACHE_REDIS_PASSWORD = ''


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class MyConfig(object):
    LOCAL_DELETE = False
