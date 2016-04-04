#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

BASE_DIR = os.path.abspath('.')

# Flask
SECRET_KEY = '3V0_OXJZZgCH7QEOKDejEPw0hAjy4Egh'
DEBUG = False # Turns on debugging features in Flask
BCRYPT_LEVEL = 12 # Configuration for the Flask-Bcrypt extension
MAIL_FROM_EMAIL = "shonnchin@gmail.com" # For use in application emails
SERVER_NAME = 'ts.com:5001'

# Flask-Cache
CACHE_TYPE = 'memcached'
CACHE_DEFAULT_TIMEOUT = 120
CACHE_KEY_PREFIX = 'flaskr_'
CACHE_MEMCACHED_SERVERS = ['127.0.0.1:11210']
# CACHE_ARGS
# CACHE_OPTIONS

# SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/flaskr.db' % BASE_DIR
SQLALCHEMY_TRACK_MODIFICATIONS = False
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')