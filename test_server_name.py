#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, Blueprint

app = Flask(__name__)
app.config.DEBUG = True
app.config['SERVER_NAME'] = 'ts.com:8888'
#app.url_map.default_subdomain = 'www'

www = Blueprint('www', 'www', subdomain='www')
sub = Blueprint('sub', 'sub', subdomain='gs')


@www.route('/')
def www_hello():
    return 'www.www_hello'


@sub.route('/')
def sub_hello():
    return 'sub.sub_hello'


app.register_blueprint(www)
app.register_blueprint(sub)

if __name__ == '__main__':
    app.run(host='192.168.22.231', port=8888, debug=True)