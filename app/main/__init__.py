# coding:utf-8
import os
from config import config
#from flask_cors import CORS
from flask_login import LoginManager
from flask_apscheduler import APScheduler
from flask_socketio import SocketIO
from flask import Flask
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session as Session


# 登录初始化
login_manager = LoginManager()
login_manager.login_message_category = 'info'
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'  # 定义登录的 视图
login_manager.login_message = '请登录以访问此页面'  # 定义需要登录访问页面的提示消息

schedulers = APScheduler()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
async_mode = 'gevent'
socketio = SocketIO()
# 创建一个Session的实例
session = Session()


# 初始化app
def create_app(config_name):
    app = Flask(__name__, template_folder='../templates', static_folder="../static", static_url_path="/static")
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    session.init_app(app)

    #security = Security()
    #security.init_app(app)
    login_manager.init_app(app)

    # 解决FLASK DEBUG模式定时任务执行两次
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        schedulers.init_app(app)
        schedulers.start()

    # 解决跨域请求
    #CORS(app)

    from app.main.stock.views import stock
    from app.main.admin.views import admin
    from app.main.apsCheduler.views import scheduler
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(stock, url_prefix='/stock')
    app.register_blueprint(scheduler, url_prefix='/scheduler')

    socketio.init_app(app=app, async_mode=async_mode)  # 新添加的代码

    return app
