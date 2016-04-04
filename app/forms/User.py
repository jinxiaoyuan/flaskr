#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo

from app.utils.Validators import Unique
from app.models.User import User

class SignupForm(Form):
    username = StringField('Username',
                           validators=[DataRequired(),
                                       Unique(User, User.username,
                                              message='There is already an account with that username.')]
                           )
    email = StringField('Email',
                        validators=[DataRequired(),
                                    Email(),
                                    Unique(User, User.email, message='There is already an account with that email.')
                                    ]
                        )
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirm = PasswordField('Password_confirm',
                                     validators=[DataRequired(), EqualTo(password, 'password not match')])

class SigninForm(Form):
    account = StringField('Nickname_or_email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class AccountForm(Form):
    account = StringField('Nickname_or_email', validators=[DataRequired()])

class PasswordForm(Form):
    password = PasswordField('New_password', validators=[DataRequired()])