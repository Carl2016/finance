#!/usr/bin/env python
# coding = utf-8
# @Time    : 2018/1/31 0031 0:18
# @Author  : Carl
# @Site    : 
# @File    : manager.py
# @Software: PyCharm
import os
from app import create_app
from exts import db
from app.user.models import *
from app.stock.models import *
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask import request, flash, render_template, redirect, url_for, jsonify, globals
from flask_login import login_required, LoginManager
from flask_security import login_user, logout_user, current_user


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.debug = False
manager = Manager(app)
migrate = Migrate(app, db)


@loginmanager.user_loader
def load_user(username):
    # print("调用了----------------------------------------------------------------")
    return User.query.filter_by(username=username).first()


def make_shell_context():
    return dict(app=app, db=db, User=User)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@app.before_request
def before_request():
    globals.db = db.session


# 请求之后，不管有么有异常,都关闭session
@app.teardown_request
def teardown_request(self):
    db.session.remove()


# 创建数据库脚本
@manager.command
def create_db():
    db.drop_all()
    db.create_all()


@manager.command
def deploy():
    from flask_migrate import init, migrate, upgrade
    init()


@manager.command
def initrole():
    print("Roles added!")


if __name__ == '__main__':
    manager.run()
