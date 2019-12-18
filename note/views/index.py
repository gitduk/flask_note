import sqlalchemy
from flask import Blueprint
from note.models import db, init_db
from flask import render_template
from flask import request
from .verification import *
from note.models.index_model import Notes, Assists, NotesAssists
from werkzeug.security import generate_password_hash
from flask import flash
from flask import g
from flask import redirect
from flask import session
from flask import url_for
from werkzeug.security import check_password_hash

index_bp = Blueprint('index', __name__, url_prefix='/index')


@index_bp.route('/index', methods=("GET", "POST"))
@login_required
def index():
    note_list = Notes.query.all()
    assist_list = Assists.query.all()
    index = "Index"
    return render_template('index/index.html', **locals())


@index_bp.route('/show_user_detail/<int:user_id>', methods=("GET", "POST"))
@login_required
def show_user_detail(user_id):
    index = "User Detail"
    return render_template('index/show_user_detail.html', **locals())


@index_bp.route('/show_assist_detail/<int:assist_id>', methods=("GET", "POST"))
@login_required
def show_assist_detail(assist_id):
    index = "Assist Detail"
    assist = Assists.query.filter_by(id=assist_id).first()
    return render_template('index/show_assist_detail.html', **locals())


@index_bp.route('/view/<int:note_id>', methods=("GET", "POST"))
@login_required
def view(note_id):
    note_list = Notes.query.all()
    view_note = Notes.query.filter_by(id=note_id).first()
    list = NotesAssists.query.filter_by(note_id=note_id).all()
    assist_list = []
    for assist in list:
        assist_list.append(Assists.query.filter_by(id=assist.assist_id).first())

    if view_note:
        index = "View"
        return render_template('index/view.html', **locals())
    else:
        index = "Index"
        return render_template('index/index.html', **locals())


@index_bp.route('/create', methods=("GET", "POST"))
@login_required
def create():
    note_list = Notes.query.all()
    if request.method == 'POST':
        title = request.form['title']
        txt = request.form['txt']
        note = Notes(title=title, txt=txt)
        note.user_id = g.user.id
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('index.view', note_id=note.id))
    else:
        index = "Create Note"
        return render_template('index/create.html', **locals())


@index_bp.route('/delete/<int:note_id>', methods=("GET", "POST"))
@login_required
def delete(note_id):
    delete_note = Notes.query.filter_by(id=note_id).delete()
    delete_association = NotesAssists.query.filter_by(note_id=note_id).delete()

    db.session.commit()

    delete_note_id = note_id

    next_note = Notes.query.filter_by(id=note_id + 1).first()

    if next_note:
        return redirect(url_for('index.view', note_id=note_id+1))
    else:
        return redirect(url_for('index.view', note_id=delete_note_id-1))


@index_bp.route('/create_assist/<int:note_id>', methods=("GET", "POST"))
@login_required
def create_assist(note_id):
    assist_list = Assists.query.all()
    note = Notes.query.filter_by(id=note_id).first()

    if request.method == 'POST':
        # get data
        username = request.form['assist']
        password = request.form['password']
        email = request.form['email']

        # deal with assist
        assist = Assists(name=username, password=password, email=email)
        db.session.add(assist)
        db.session.commit()

        # deal with the association of note and assist
        notes_assists = NotesAssists(note_id=note.id, assist_id=assist.id)
        db.session.add(notes_assists)
        db.session.commit()

        return redirect(url_for('index.view', note_id=note_id))
    else:
        index = "Create Assist"
        return render_template('index/create_assist.html', **locals())




