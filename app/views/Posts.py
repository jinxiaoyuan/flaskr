#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template, Blueprint, flash

from app import cache
from app.models import User

posts = Blueprint('posts', __name__)

@posts.route('/<string:author>/posts')
@cache.cached()
def get_author_post(author):
    user = User.User.query.filter_by(username=author).first()
    if user is None:
        flash(u'抱歉系统无此作者 %s' % author)
        return render_template('flash_and_redirect.html')
        # return u'<script>alert("抱歉系统无此作者: %s"); window.location.href = "%s";</script>' % (author, url_for('home.index'))

    all_posts = user.user_posts.all()
    if all_posts:
        posts_dict = {}
        for pst in all_posts:
            posts_dict[pst.title] = pst.body
        return render_template('posts.html', author = author, posts_dict = posts_dict)
    else:
        flash('No posts from %s' % author, 'error')
        return render_template('flash_and_redirect.html')