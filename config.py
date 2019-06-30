# coding:utf-8
import os
import redis


class Config:
    DEBUG = True
    SCHEDULER_API_ENABLED = True
    CSRF_ENABLED = False
    SECURITY_TRACKABLE = True
    SECRET_KEY = os.urandom(24)
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flask]'
    FLASKY_ADMIN = '417449614@qq.com'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    MAIL_SERVER = 'smtp.qq.com'  # smtp.163.com
    MAIL_PORT = 465  # 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = '468647870@qq.com'
    MAIL_PASSWORD = 'kfbfznsqgzjqcbag'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/finance?charset=utf8'
    # 设置是否在每次连接结束后自动提交数据库中的变动。
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    # 数据库连接池的大小。默认是数据库引擎的默认值：5
    SQLALCHEMY_POOL_SIZE = 5
    # 控制在连接池达到最大值后可以创建的连接数。当这些额外的连接使用后回收到连接池后将会被断开和抛弃。保证连接池只有设置的大小
    SQLALCHEMY_MAX_OVERFLOW = 5
    # 指定数据库连接池的超时时间。默认是：10
    SQLALCHEMY_POOL_TIMEOUT = 10
    # 自动回收连接的秒数
    SQLALCHEMY_POOL_RECYCLE = 1200

    # session
    SESSION_TYPE = 'redis'
    # 如果设置为True，则关闭浏览器session就失效
    SESSION_PERMANENT = True
    # 是否对发送到浏览器上session的cookie值进行加密
    SESSION_USE_SIGNER = False
    # 保存到session中的值的前缀
    SESSION_KEY_PREFIX = 'session'
    SESSION_REDIS = redis.Redis(host='127.0.0.1', port='6379', password='', db=0)


class TestingConfig(Config):
    TESTING = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.qq.com'  # smtp.163.com
    MAIL_PORT = 465  # 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = '468647870@qq.com'
    MAIL_PASSWORD = 'kfbfznsqgzjqcbag'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/finance?charset=utf8'
    # 设置是否在每次连接结束后自动提交数据库中的变动。
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    # 数据库连接池的大小。默认是数据库引擎的默认值：5
    SQLALCHEMY_POOL_SIZE = 5
    # 控制在连接池达到最大值后可以创建的连接数。当这些额外的连接使用后回收到连接池后将会被断开和抛弃。保证连接池只有设置的大小
    SQLALCHEMY_MAX_OVERFLOW = 5
    # 指定数据库连接池的超时时间。默认是：10
    SQLALCHEMY_POOL_TIMEOUT = 10
    # 自动回收连接的秒数
    SQLALCHEMY_POOL_RECYCLE = 1200

    # session
    SESSION_TYPE = 'redis'
    # 如果设置为True，则关闭浏览器session就失效
    SESSION_PERMANENT = True
    # 是否对发送到浏览器上session的cookie值进行加密
    SESSION_USE_SIGNER = False
    # 保存到session中的值的前缀
    SESSION_KEY_PREFIX = 'session'
    SESSION_REDIS = redis.Redis(host='127.0.0.1', port='6379', password='', db=0)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
