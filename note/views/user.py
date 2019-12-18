import sqlalchemy
from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from note.models.login_model import User
from note.models import db, init_db

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/login', methods=("GET", "POST"))
def login():
    # session
    # user =  session.get('username')
    # if user:
    #     print(user)
    #     return redirect(url_for('index.view'))

    user_list = User.query.all()

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        q_user = User.query.filter_by(name=username).first()
        q_password = User.query.filter_by(password=password).first()

        if q_user and q_password:
            flash('You were successfully logged in', 'yes')
            session['username'] = username
            session['password'] = password
            return redirect(url_for('index.index'))
        else:
            flash('You have an error', 'error')
            return render_template('user/login.html', user_list = user_list)
    else:
        return render_template('user/login.html', user_list = user_list)



@user_bp.route('/register', methods=("GET", "POST"))
def register():
    user_list = User.query.all()
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        user = User(name=username, password=password, email=email)
        db.session.add(user)
        try:
            db.session.commit()
            return redirect('login')
        except sqlalchemy.exc.IntegrityError:
            flash('Error')
            return redirect('login')
    else:
        return render_template('user/register.html', **locals())


@user_bp.route('/logout', methods=("GET", "POST"))
def logout():
    session.clear()
    return redirect(url_for('user.login'))

