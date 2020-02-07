import functools
import time

import redis
from flask import redirect, flash
from flask import url_for
from main.models.note.index_model import Assists
from main.views.note.user import user_bp
from flask import session
from flask import g
from main.models.note.login_model import User
from main import Config


@user_bp.before_app_request
def load_logged_in_user():
    username = session.get("username")
    authority = session.get("authority")

    if username and authority:
        g.user = User.query.filter_by(name=username).first()
    else:
        g.user = Assists.query.filter_by(name=username).first()


def login_required(view):
    @functools.wraps(view)
    def wrapper(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("user.login"))
        else:
            # data handling
            fmt = 'user:{0:12} active:{1:20} time:{2:12}\n'
            message = fmt.format(g.user.name, view.__name__, time.ctime(time.time()))
            file_path = ('{}/{}/{}/{}'.format('main', 'files', 'note', 'message.txt'))

            with open(file_path, 'a') as f:
                f.write(message)
            return view(*args, **kwargs)

    return wrapper


def authority(view):
    @functools.wraps(view)
    def wrapper(*args, **kwargs):
        if g.user.authority:
            return view(*args, **kwargs)
        else:
            flash('You have no authority', 'authority')
            return redirect(url_for('index.index'))

    return wrapper


def connect_redis():
    return redis.StrictRedis(host="127.0.0.1", port=6379, db=0)
