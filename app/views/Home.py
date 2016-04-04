#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

from flask import render_template, Blueprint, url_for, request

from app import cache, app

home = Blueprint('home', __name__)

@home.route('/')
@home.route('/index')
# @cache.cached()
def index():
    # output = datetime.now()
    output = u'您用的是%s浏览器' % request.user_agent
    return render_template('test_out.html', output = output)

@home.route('/about')
def about():
    return render_template('test_out.html', output = 'About Brother yuan')

@home.route('/contact')
def contact():
    return render_template('test_out.html', output = 'Contact Brother yuan')

@app.route('/test')
def test():
    return url_for('test', _external=True)