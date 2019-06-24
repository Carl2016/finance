# coding = utf-8
from threading import Thread
from functools import wraps
from flask import session
from app.main.admin.models import *

def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper


def auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        username = session.get('username')
        user = globals.db.query(User).filter_by(username=username).first()
        return func(*args, **kwargs)
    return wrapper