# coding:utf-8
from flask import Flask
from flask_mail import Mail
from flask_moment import Moment
from config import config
from flask_login import LoginManager
from flask_pagedown import PageDown
from flask_security import Security
from exts import db
from app.common import schedulers
import os

# 登录初始化
loginmanager = LoginManager()
loginmanager.login_message_category = 'info'
loginmanager.session_protection = 'strong'
loginmanager.login_view = 'auth.login'  # 定义登录的 视图
loginmanager.login_message = '请登录以访问此页面'  # 定义需要登录访问页面的提示消息

mail = Mail()
moment = Moment()
pagedown = PageDown()


# 初始化app
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    security = Security()
    security.init_app(app)
    loginmanager.init_app(app)
    pagedown.init_app(app)

    # if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
    # 任务调度
    schedulers.init_app(app)
    schedulers.start()

    from app.auth.views import auth
    from app.stock.views import stock
    from app.apsCheduler import scheduler
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(stock, url_prefix='/stock')
    app.register_blueprint(scheduler, url_prefix='/scheduler')

    return app
