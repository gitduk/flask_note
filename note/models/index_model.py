from datetime import datetime
from sqlalchemy import *
from note.models import db

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
    updated_on = Column(DateTime, onupdate=datetime.now)


class Assists(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(120))

