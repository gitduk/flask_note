import sqlalchemy
from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

from main.models.note.index_model import Assists
from main.models.note.login_model import User
from main.models import db

user_bp = Blueprint('user', __name__, url_prefix='/note/user')

@user_bp.route('/login', methods=("GET", "POST"))
def login():
    index = 'Login'
    # session
    # user =  session.get('username')
    # if user:
    #     print(user)
    #     return redirect(url_for('index.view'))

    user_list = User.query.all()
    assist_list = Assists.query.all()

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(name=username).first()
        u_password = User.query.filter_by(password=password).first()

        assist = Assists.query.filter_by(name=username).first()
        a_password = Assists.query.filter_by(password=password).first()

        if user and u_password:
            session['username'] = username
            session['authority'] = user.authority
            return redirect(url_for('index.index'))
        elif assist and a_password:
            session['username'] = username
            session['authority'] = assist.authority
            return redirect(url_for('index.index'))
        else:
            flash('You have an error', 'error')
            return render_template('note/user/login.html', **locals())
    else:
        return render_template('note/user/login.html', **locals())



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
        return render_template('note/user/register.html', **locals())


@user_bp.route('/logout', methods=("GET", "POST"))
def logout():
    session.clear()
    return redirect(url_for('user.login'))

