# coding:utf-8
from flask import Flask, render_template, globals
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler
from config import config
from flask_login import LoginManager
from flask_pagedown import PageDown
from flask_security import Security, login_required, SQLAlchemySessionUserDatastore
from exts import db


# 登录初始化
loginmanager = LoginManager()
loginmanager.login_message_category = "info"
loginmanager.session_protection = 'strong'
loginmanager.login_view = "auth.login"  # 定义登录的 视图
loginmanager.login_message = '请登录以访问此页面'  # 定义需要登录访问页面的提示消息

#bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
# db = SQLAlchemy()
pagedown = PageDown()


# 初始化app
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    security = Security()
    security.init_app(app)
    loginmanager.init_app(app)
    pagedown.init_app(app)

    # 任务调度
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()

    from app.auth.views import auth
    from app.stock.views import stock
    from app.init.views import init
    from app.common.apsCheduler.views import scheduler
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(stock, url_prefix='/stock')
    app.register_blueprint(init, url_prefix='/init')
    app.register_blueprint(scheduler, url_prefix='/scheduler')

    return app
