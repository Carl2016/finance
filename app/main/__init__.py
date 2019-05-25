# coding:utf-8
from flask import Flask
from flask_mail import Mail
from flask_moment import Moment
from config import config
from flask_login import LoginManager
from flask_security import Security
from exts import db
from flask_apscheduler import APScheduler

#from app.main.apsCheduler.config import schedulers


# 登录初始化
login_manager = LoginManager()
login_manager.login_message_category = 'info'
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'  # 定义登录的 视图
login_manager.login_message = '请登录以访问此页面'  # 定义需要登录访问页面的提示消息

schedulers = APScheduler()

# 初始化app
def create_app(config_name):
    app = Flask(__name__, template_folder='../templates', static_folder="../static", static_url_path="/static")
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mail = Mail()
    moment = Moment()

    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    #security = Security()
    #security.init_app(app)
    login_manager.init_app(app)

    # if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
    # 任务调度
    schedulers.init_app(app)
    schedulers.start()

    from app.main.stock.views import stock
    from app.main.apsCheduler.views import scheduler
    app.register_blueprint(stock, url_prefix='/stock')
    app.register_blueprint(scheduler, url_prefix='/scheduler')

    return app
