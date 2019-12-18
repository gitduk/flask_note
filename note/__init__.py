import os
from flask import Flask
from note.models import db, init_db
from note.config import *

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object(Config)
    else:
        # load the test config if passed in
        app.config.from_pyfile(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # init app
    db.init_app(app)

    # init db
    init_db(app)

    # register blueprint
    from note.views.user import user_bp
    from note.views.index import index_bp
    app.register_blueprint(user_bp)
    app.register_blueprint(index_bp)

    return app

