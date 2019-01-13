# coding:utf-8
from flask import request, flash, render_template, redirect, url_for, jsonify
from flask_login import login_required
from flask_security import login_user, logout_user, current_user
from app.user.models import *
from app.auth import auth
from .. import db


# 管理员登录
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if not current_user.is_anonymous:
        return redirect(url_for('auth.login'))
    if request.method == 'POST':
        # 由于request中的form参数以字典的形式存在，故以下语句等价
        username = request.form.get('username')
        password = request.form.get('password')
        remember_me = request.form.get('remember_me')
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash('用户不存在')
        else:
            if user.verify_password(password):
                login_user(user, remember_me)
                return redirect(request.args.get('next') or url_for('auth.index'))
            else:
                flash('用户名/密码错误')
    return render_template("system/login.html")


# 注册
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username is not None and password is not None:
            user = User(username,password)
            # user.username = username
            # user.password_hash = user.password(password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
    return render_template('system/register.html', form=request.form)


# 首页
@auth.route('/index')
@login_required
def index():
    return render_template("index.html")


# 退出
@auth.route('/logout')
@login_required
def logout():
    logout_user()  # 登出用户
    return redirect(url_for('auth/login'))


