from flask import Blueprint
from main.models import db
from flask import render_template
from flask import request
from .ffunc import *
from main.models.note.index_model import Notes, Assists, NotesAssists
from flask import g
from flask import redirect
from flask import url_for

index_bp = Blueprint('index', __name__, url_prefix='/note/index')


@index_bp.route('/', methods=("GET", "POST"))
@login_required
def index():
    index = "Index"
    note_list = Notes.query.all()
    assist_list = Assists.query.all()
    return render_template('note/index/index.html', **locals())


@index_bp.route('/show_user_detail', methods=("GET", "POST"))
@login_required
def show_user_detail():
    index = "User Detail"
    return render_template('note/index/show_user_detail.html', **locals())


@index_bp.route('/show_assist_detail/<int:assist_id>', methods=("GET", "POST"))
@authority
@login_required
def show_assist_detail(assist_id):
    index = "Assist Detail"
    assist = Assists.query.filter_by(id=assist_id).first()
    return render_template('note/index/show_assist_detail.html', **locals())


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
        return render_template('note/index/view.html', **locals())
    else:
        index = "Index"
        return render_template('note/index/index.html', **locals())


@index_bp.route('/create', methods=("GET", "POST"))
@authority
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
        index = "Create Note"
        return redirect(url_for('index.view', note_id=note.id))
    else:
        index = "Create Note"
        return render_template('note/index/create.html', **locals())


@index_bp.route('/delete/<int:note_id>', methods=("GET", "POST"))
@authority
@login_required
def delete(note_id):
    delete_note = Notes.query.filter_by(id=note_id).delete()
    delete_association = NotesAssists.query.filter_by(note_id=note_id).delete()

    db.session.commit()

    delete_note_id = note_id

    next_note = Notes.query.filter_by(id=note_id + 1).first()

    if next_note:
        index = "View"
        return redirect(url_for('index.view', note_id=note_id+1))
    else:
        index = "View"
        return redirect(url_for('index.view', note_id=delete_note_id-1))


@index_bp.route('/create_assist/<int:note_id>', methods=("GET", "POST"))
@authority
@login_required
def create_assist(note_id):
    index = "Create Assist"
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

        # deal with the association of main and assist
        notes_assists = NotesAssists(note_id=note.id, assist_id=assist.id)
        db.session.add(notes_assists)
        db.session.commit()

        index = "View"
        return redirect(url_for('index.view', note_id=note_id))
    else:
        index = "Create Assist"
        return render_template('note/index/create_assist.html', **locals())




