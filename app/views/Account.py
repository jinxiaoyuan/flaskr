#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template, Blueprint, url_for, flash
from flask.ext.login import login_user, logout_user
from itsdangerous import SignatureExpired

from app import db, timed_serializer
from app.forms.User import SigninForm, SignupForm, AccountForm, PasswordForm
from app.models.User import User

account = Blueprint('account', __name__)

@account.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()

    if form.validate_on_submit():
        acc = form.account.data
        user = User.query.filter((User.username == acc) | (User.email == acc)).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Signin success')
            return render_template('flash_and_redirect.html', to_url=[u'首页',url_for('home.index')])
        else:
            flash('Wrong account or password....', 'emer')
            return render_template('flash_and_redirect.html', to_url=[u'登录页',url_for('account.signin')])
    return render_template('signin.html', form=form, title='Signin page')

@account.route('/signout')
def signout():
    logout_user()
    flash('Logout success')
    return render_template('flash_and_redirect.html')

@account.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Signup success')
        return render_template('flash_and_redirect.html')

    return render_template('signup.html', form=form, title='Signup page')

@account.route('/pwd_reset', methods=['GET', 'POST'])
def pwd_reset():
    form = AccountForm()
    if form.validate_on_submit():
        acc = form.account.data
        user = User.query.filter((User.username == acc) | (User.email == acc)).first()
        if user is None:
            flash('No such a account')
            return u'<script>alert("no such a account: %s");</script>' % acc
        else:
            # subject = 'Password reset requested'
            token = timed_serializer.dumps(user.email, salt='recover-key')
            recover_url = url_for('account.reset_with_token',
                                  token = token,
                                  _external=True)
            return render_template('email/recover.html', recover_url=recover_url)

    return render_template('pwd_reset.html', form=form)

@account.route('/reset/<token>', methods=['GET', 'POST'])
def reset_with_token(token):
    try:
        email = timed_serializer.loads(token, salt='recover-key', max_age=86400)
    except SignatureExpired:
        flash('This reset URL is no longer available.', 'error')
        return render_template('flash_and_redirect.html')

    form = PasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=email).first_or_404()
        user.password = form.password.data

        db.session.add(user)
        db.session.commit()
        flash('password reset successfully')
        return render_template('flash_and_redirect.html', to_url=[u'登录页', url_for('account.signin')])

    return render_template('reset_with_token.html', form=form, token=token)