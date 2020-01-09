from sqlalchemy import *
from main.models import db, init_db

Base = db.Model


class Test(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)

    def __repr__(self):
        return '<ID %r>' % self.id

    def __str__(self):
        return '<id %r>' % self.id


