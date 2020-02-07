from datetime import datetime
from sqlalchemy import *
from main.models import db

Base = db.Model


class NotesAssists(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    note_id = Column(Integer)
    assist_id = Column(Integer)


class Notes(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    txt = Column(Text)
    create_time = Column(DateTime, default=datetime.now)
    updated_on = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted = Column(String(50), default=False, nullable=False)


class Assists(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(120))
    authority = Column(Integer, default=0)


class Roll(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    operation = Column(String(50), unique=False)
    note_id = Column(Integer)
    note_title = Column(String(50), nullable=False)
    note_txt = Column(Text)
    note_create_time = Column(DateTime, default=datetime.now)
    delete_type = Column(String(50), default='logic', nullable=False)
    delete_time = Column(DateTime, default=datetime.now)

