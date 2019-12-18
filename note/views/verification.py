import functools
from flask import redirect
from flask import url_for
from note.views.user import user_bp
from flask import session
from flask import g
from note.models.login_model import User


@user_bp.before_app_request
def load_logged_in_user():

    username = session.get("username")

    if username:
        g.user = User.query.filter_by(name=username).first()
    else:
        g.user = None


def login_required(view):
    """View decorator that redirects anonymous users to the login page."""
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("user.login"))
        return view(**kwargs)
    return wrapped_view


