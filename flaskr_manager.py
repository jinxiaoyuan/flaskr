#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app, db

migrate = Migrate()
DATABASE_URI = getattr(app.config, 'SQLALCHEMY_DATABASE_URI', '')
is_sqlite = DATABASE_URI.startswith('sqlite:')
migrate.init_app(app, db, render_as_batch=is_sqlite)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()