#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.ext.hybrid import hybrid_property

from app import db, bcrypt

class User(db.Model):
    # __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True)
    email = db.Column(db.String(120), unique = True)
    _password = db.Column(db.String(128))
    # posts = db.relationship('Post', backref = db.backref('post_user', lazy = 'dynamic'))


    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plain_text):
        self._password = bcrypt.generate_password_hash(plain_text)

    def check_password(self, plaintext):
        return bcrypt.check_password_hash(self._password, plaintext)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % self.username