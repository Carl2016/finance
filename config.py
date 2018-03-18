# coding:utf-8
import os
# from app.stock.views import initHistoryPen
basedir = os.path.abspath(os.path.dirname(__file__))


DEBUG = True
CSRF_ENABLED = False
SECURITY_TRACKABLE = True
SECRET_KEY = os.urandom(24)
WTF_CSRF_ENABLED = False


def job_1(a, b):  # 一个函数，用来做定时任务的任务。
    print(str(a) + ' ' + str(b))


class Config:
    # 任务调度
    JOBS = [
        # { # 任务字典（细节）
        #     'id': 'job1',
        #     'func': initHistoryPen,
        #     'args': '',
        #     'trigger': 'cron',
        #     'hour': 19,
        #     'minute': 27
        # },
        # {  # 第二个任务字典
        #     'id': 'job2',
        #     'func': job_1,
        #     'args': (3, 4),
        #     'trigger': 'interval',
        #     'seconds': 5,
        # }
    ]
    SCHEDULER_API_ENABLED = True

    #
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = '417449614@qq.com'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost:3306/finance?charset=utf8'


class TestingConfig(Config):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
