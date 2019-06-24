# coding:utf-8
'''
不同蓝本分别位于不同的Python包中，而蓝图的创建则位于Python包下的init.py文件。
不同Python包下的views.py文件则对应不同蓝本下的路由。
'''
from flask import Blueprint
admin = Blueprint('admin', __name__,)
from app.main.admin import views