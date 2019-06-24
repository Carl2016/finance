# coding:utf-8
'''
不同蓝本分别位于不同的Python包中，而蓝图的创建则位于Python包下的init.py文件。
不同Python包下的views.py文件则对应不同蓝本下的路由。
'''
from flask import Blueprint

stock = Blueprint('stock', __name__,)

from app.main.stock import views
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session

engine = create_engine(
        "mysql+pymysql://carl:chuan@localhost:3306/finance?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=100,  # 连接池大小
        pool_timeout=60,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1,  # 多久之后对线程池中的线程进行一次连接的回收（重置）
        pool_pre_ping=True
    )
# Session = sessionmaker(bind=engine)
Session = scoped_session(engine)


