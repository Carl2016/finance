#!/usr/bin/env python
# coding = utf-8
# @Time    : 2018/1/31 0031 0:18
# @Author  : Carl
# @Site    : 
# @File    : manager.py
# @Software: PyCharm
import os
from app.main.admin.models import User
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app.main import login_manager, socketio, db, create_app
from flask import request, flash, render_template, redirect, url_for, globals, session
from flask_login import login_required, login_user, logout_user
# 导入线程模块
from threading import Thread, Lock
import psutil, time, json
from app.main.utils.utils import get_network


thread = None
thread_lock = Lock()


# 后台线程 产生数据，即刻推送至前端
def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    interval = 1
    k = 1024  # 一 K 所包含的字节数
    while True:
        count += 1
        # 获取系统时间（只取分:秒）
        t = time.strftime('%H:%M:%S', time.localtime())
        # 获取系统cpu使用率 non-blocking
        cpu = 0
        cpus = psutil.cpu_percent(interval=None, percpu=True)
        for i in range(len(cpus)):
            cpu = cpu + cpus[i]
        cpu = round(cpu/len(cpus), 2)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        network = get_network(interval, 'K')
        # 注意：这里不需要客户端连接的上下文，默认 broadcast = True ！！！！！！！
        socketio.emit('server_response', {'data': [t, cpu, memory, disk, network[0], network[1]], 'count': count}, namespace='/sysInfo')


# 与前端建立 socket 连接后，启动后台线程
@socketio.on('connect', namespace='/sysInfo')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


@login_manager.user_loader
def load_user(username):
    return User.query.filter_by(username=username).first()


def make_shell_context():
    return dict(app=app, db=db, User=User)


@app.before_request
def before_request():
    globals.db = db.session


# 请求之后，不管有么有异常,都关闭session
@app.teardown_request
def teardown_request(exception):
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


# 管理员登录
@app.route('/login', methods=['GET', 'POST'])
def login():
    username = session.get('username') if session.get('username') is not None else ''
    if request.method == 'POST':
        # 由于request中的form参数以字典的形式存在，故以下语句等价
        username = request.form.get('username')
        password = request.form.get('password')
        remember_me = request.form.get('remember_me')
        user = User.query.filter_by(username=username, status=1).first()
        if user is None:
            flash('用户不存在')
        else:
            if user.verify_password(password):
                login_user(user, remember_me)
                session['username'] = username
                return redirect(request.args.get('next') or url_for('index'))
            else:
                flash('用户名/密码错误')
    return render_template("common/login.html", username=username)


# 找不到错误
@app.errorhandler(404)
def error_404(error):
    return render_template('common/404.html'), 404


# 权限错误
@app.errorhandler(403)
def error_403(error):
    return render_template('common/403.html'), 403


# 服务器错误
@app.errorhandler(500)
def error_500(error):
    return render_template('common/500.html'), 500


# 注册
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username is not None and password is not None:
            user = User(username, password)
            db.session.add(user)
            db.session.commit()
            session['username'] = username
            return redirect(url_for('login'))
    return render_template('common/register.html', form=request.form)


# 首页
@app.route('/', methods=["GET", "POST"])
@login_required
def index():
    return render_template("index.html")


# 主页
@app.route('/home')
@login_required
def home():
    return render_template("layout/home.html", async_mode=socketio.async_mode)


# 退出
@app.route('/logout')
@login_required
def logout():
    session.pop('username', None)
    logout_user()  # 登出用户
    return redirect(url_for('login'))


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
# 新加入的代码，重写manager的run命令
manager.add_command('runserver', socketio.run(app=app, host='0.0.0.0', port=5000, use_reloader=False, debug=True))


if __name__ == '__main__':
    manager.run()
