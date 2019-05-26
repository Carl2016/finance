# coding = utf-8
# @Time    : 2018/1/30 0030 23:56
# @Author  : Carl
# @Site    : 
# @File    : email.py
# @Software: PyCharm
# from flask_mail import Message
# from app import mail
# from flask import render_template
#
# def send_email(to,subject,template,**kwargs):
#     msg=Message("[TecnologyDreamer]"+subject,sender='879651072@qq.com',recipients=[to])
#     msg.body=render_template(template+'.txt',**kwargs)
#     msg.html=render_template(template+'.html',**kwargs)
#     mail.send(msg)