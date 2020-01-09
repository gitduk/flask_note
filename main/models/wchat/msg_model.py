from datetime import datetime
from sqlalchemy import *
from main.models import db

Base = db.Model


class Text(Base):
    MsgId = Column(String(50), primary_key=True, nullable=False)
    MsgType = Column(String(50), nullable=False)
    CreateTime = Column(String(50), nullable=False)

    Content = Column(String(50), nullable=False)

    ToUserName = Column(String(50), nullable=False)
    FromUserName = Column(String(50), nullable=False)


class Image(Base):
    MsgId = Column(String(50), primary_key=True, nullable=False)
    MsgType = Column(String(50), nullable=False)
    CreateTime = Column(String(50), nullable=False)

    PicUrl = Column(String(50), nullable=False)
    MediaID = Column(String(50), nullable=False)

    ToUserName = Column(String(50), nullable=False)
    FromUserName = Column(String(50), nullable=False)


class Voice(Base):
    MsgId = Column(String(50), primary_key=True, nullable=False)
    MsgType = Column(String(50), nullable=False)
    CreateTime = Column(String(50), nullable=False)

    MediaID = Column(String(50), nullable=False)
    Format = Column(String(50), nullable=False)

    ToUserName = Column(String(50), nullable=False)
    FromUserName = Column(String(50), nullable=False)


class Video(Base):
    MsgId = Column(String(50), primary_key=True, nullable=False)
    MsgType = Column(String(50), nullable=False)
    CreateTime = Column(String(50), nullable=False)

    MediaID = Column(String(50), nullable=False)
    ThumbMediaID = Column(String(50), nullable=False)

    ToUserName = Column(String(50), nullable=False)
    FromUserName = Column(String(50), nullable=False)


class ShortVideo(Base):
    MsgId = Column(String(50), primary_key=True, nullable=False)
    MsgType = Column(String(50), nullable=False)
    CreateTime = Column(String(50), nullable=False)

    MediaID = Column(String(50), nullable=False)
    ThumbMediaID = Column(String(50), nullable=False)

    ToUserName = Column(String(50), nullable=False)
    FromUserName = Column(String(50), nullable=False)


class Location(Base):
    MsgId = Column(String(50), primary_key=True, nullable=False)
    MsgType = Column(String(50), nullable=False)
    CreateTime = Column(String(50), nullable=False)

    Location_X = Column(String(50), nullable=False)
    Location_Y = Column(String(50), nullable=False)
    Label = Column(String(50), nullable=False)
    Scale = Column(String(50), nullable=False)

    ToUserName = Column(String(50), nullable=False)
    FromUserName = Column(String(50), nullable=False)


class Link(Base):
    MsgId = Column(String(50), primary_key=True, nullable=False)
    MsgType = Column(String(50), nullable=False)
    CreateTime = Column(String(50), nullable=False)

    Title = Column(String(50), nullable=False)
    Description = Column(String(50), nullable=False)
    Url = Column(String(50), nullable=False)

    ToUserName = Column(String(50), nullable=False)
    FromUserName = Column(String(50), nullable=False)
