#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.login import LoginManager
from flask_cache import Cache
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from itsdangerous import URLSafeTimedSerializer

app = Flask(__name__, static_url_path='', static_folder='/data/apps/flaskr/app/static')

app.config.from_object('config.default')
app.config.from_object('config.development')
# app.config.from_envvar('APP_CONFIG_FILE',silent=True)

timed_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
cache = Cache(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from .views.Home import home
from .views.Posts import posts
from .views.Account import account
from . import models
from .models.User import User

app.register_blueprint(home, subdomain='www')
app.register_blueprint(posts, subdomain='www')
app.register_blueprint(account, subdomain='www')
# app.url_map.default_subdomain = 'www'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view =  "signin"

@login_manager.user_loader
def load_user(userid):
    return User.query.filter(User.id==userid).first()