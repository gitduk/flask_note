from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from note.models import db

Base = db.Model


class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(120))
    authority = Column(Integer, default=1)

