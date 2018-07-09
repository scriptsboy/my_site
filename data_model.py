# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class Article(db.Model):
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    title = db.Column(db.String(255))
    text = db.Column(db.String)
    md_file = db.Column(db.Text)
    type = db.Column(db.Integer)
    author = db.Column(db.ForeignKey('user.id'), index=True)

    user = db.relationship('User', primaryjoin='Article.author == User.id', backref='articles')


class Tag(db.Model):
    __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class Tagmap(db.Model):
    __tablename__ = 'tagmap'

    id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.ForeignKey('tag.id'), nullable=False, index=True)
    article_id = db.Column(db.ForeignKey('article.id'), index=True)

    article = db.relationship('Article', primaryjoin='Tagmap.article_id == Article.id', backref='tagmaps')
    tag = db.relationship('Tag', primaryjoin='Tagmap.tag_id == Tag.id', backref='tagmaps')


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text)
    name = db.Column(db.String(255), unique=True)
    create_at = db.Column(db.DateTime)
    password_hash = db.Column(db.Text)
    access = db.Column(db.Integer, server_default=db.FetchedValue())