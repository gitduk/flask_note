import functools
import time
from flask import redirect, flash
from flask import url_for
from note.models.index_model import Assists
from note.views.user import user_bp
from flask import session
from flask import g
from note.models.login_model import User


@user_bp.before_app_request
def load_logged_in_user():

    username = session.get("username")
    authority = session.get("authority")

    if username and authority:
        g.user = User.query.filter_by(name=username).first()
    else:
        g.user = Assists.query.filter_by(name=username).first()


def login_required():
    def user_log(view):
        @functools.wraps(view)
        def wrapper(*args, **kwargs):
            if g.user is None:
                return redirect(url_for("user.login"))
            else:
                message = 'user:{0:12} active:{1:20} time:{2:12}\n'.format(g.user.name, view.__name__, time.ctime(time.time()))
                with open('log', 'a') as f:
                    f.write(message)
                return view(*args, **kwargs)
        return wrapper
    return user_log


def authority(view):
    @functools.wraps(view)
    def wrapper(*args, **kwargs):
        if g.user.authority:
            return view(*args, **kwargs)
        else:
            flash('You have no authority', 'authority')
            return redirect(url_for('index.index'))
    return wrapper
