# coding:utf-8
import os
# from app.stock.views import initHistoryPen
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
CSRF_ENABLED = False
SECURITY_TRACKABLE = True
SECRET_KEY = os.urandom(24)
WTF_CSRF_ENABLED = False


class Config:

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
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/finance?charset=utf8'
    # 设置是否在每次连接结束后自动提交数据库中的变动。
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 数据库连接池的大小。默认是数据库引擎的默认值：5
    SQLALCHEMY_POOL_SIZE = 10
    # 控制在连接池达到最大值后可以创建的连接数。当这些额外的连接使用后回收到连接池后将会被断开和抛弃。保证连接池只有设置的大小
    SQLALCHEMY_MAX_OVERFLOW = 5
    # 指定数据库连接池的超时时间。默认是：10
    SQLALCHEMY_POOL_TIMEOUT = 10
    # 自动回收连接的秒数
    SQLALCHEMY_POOL_RECYCLE = 1200


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
