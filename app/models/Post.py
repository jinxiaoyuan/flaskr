#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

from app import db

class Post(db.Model):
    # __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('cat_posts', lazy='dynamic'))
    user = db.relationship('User', backref=db.backref('user_posts', lazy='dynamic'))

    def __init__(self, user, title, body, category, pub_date=datetime.utcnow()):
        self.user = user
        self.title = title
        self.body = body
        self.pub_date = pub_date
        self.category = category

    def __repr__(self):
        return '<Post %r>' % self.title

    def __str__(self):
        return self.title


class Category(db.Model):
    # __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name