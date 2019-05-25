#!/usr/bin/env python
# coding = utf-8
# @Time    : 2018/1/31 0031 0:18
# @Author  : Carl
# @Site    : 
# @File    : manager.py
# @Software: PyCharm
import os
from app.main import create_app
from app.main.user.models import *
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask import globals
from app.main import login_manager
from flask import request, flash, render_template, redirect, url_for
from flask_login import login_required, login_user, current_user, logout_user

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.debug = True
manager = Manager(app)
migrate = Migrate(app, db)


@login_manager.user_loader
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
    from flask_migrate import init
    init()


@manager.command
def initrole():
    print("Roles added!")


# 管理员登录
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if not current_user.is_anonymous:
        return redirect(url_for('login'))
    if request.method == 'POST':
        # 由于request中的form参数以字典的形式存在，故以下语句等价
        username = request.form.get('username')
        password = request.form.get('password')
        #remember_me = request.form.get('remember_me')
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash('用户不存在')
        else:
            if user.verify_password(password):
                login_user(user)
                return redirect(request.args.get('next') or url_for('index'))
            else:
                flash('用户名/密码错误')
    return render_template("common/login.html")


# 注册
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username is not None and password is not None:
            user = User(username, password)
            # user.username = username
            # user.password_hash = user.password(password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('system/register.html', form=request.form)


# 首页
@app.route('/index')
@login_required
def index():
    return render_template("index.html")


# 主页
@app.route('/home')
def home():
    return render_template("layout/home.html")


# 退出
@app.route('/logout')
@login_required
def logout():
    logout_user()  # 登出用户
    return redirect(url_for('login'))


if __name__ == '__main__':
    manager.run()
