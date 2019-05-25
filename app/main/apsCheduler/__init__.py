# coding = utf-8
# @Time    : 2018/2/8 0008 22:50
# @Author  : Carl
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Blueprint
scheduler = Blueprint('scheduler', __name__,)
from app.main.apsCheduler import views