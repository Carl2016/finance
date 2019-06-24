# coding = utf-8
# @Time    : 2018/1/30 0030 23:56
# @Author  : Carl
# @Site    :
# @File    : email.py
# @Software: PyCharm
from flask_mail import Message
from app.main import mail
from flask import render_template, current_app
import config
from threading import Thread


# 发送邮件线程函数
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


# 发送邮件整体函数
def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message('Carl:' + subject, sender=config.DevelopmentConfig.MAIL_USERNAME, recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr


