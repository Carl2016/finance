# coding = utf-8
from threading import Thread
from functools import wraps
from flask import session, request
from app.main.admin.models import *

def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper


# 鉴权装饰器
def auth(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        flag = False
        username = session.get('username')
        url = request.path
        user = globals.db.query(User).filter_by(username=username).first()
        menus = user.menus
        for i in range(len(menus)):
            if menus[i].url == url:
                flag = True
                continue
        if flag is True:
            return func(*args, **kwargs)
        else:
            abort(403)
    return wrapper