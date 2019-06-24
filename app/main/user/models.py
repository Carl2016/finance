# coding:utf-8
from app.main import db
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


# 用户
# class User(db.Model, UserMixin):
#     __tablename__ = 'sys_user'
#     id = db.Column(db.Integer, primary_key=True,autoincrement=True)
#     username = db.Column(db.String(80), unique=True, nullable=False, comment=u'用户名')
#     email = db.Column(db.String(120), unique=True, comment=u'email')
#     #password = db.Column(db.String(100), nullable=False, comment=u'密码')
#     password_hash = db.Column(db.String(128), comment="加密密码")
#     createTime = db.Column(db.DATETIME, server_default=func.now(), comment=u'创建时间')
#     updateTime = db.Column(db.DATETIME, server_default=func.now(), comment=u'修改时间')
#
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#
#     @property
#     def password(self):
#         return self.password_hash
#         #raise AttributeError('不能直接获取明文密码！')
#
#     @password.setter
#     def password(self, password):
#         self.password_hash = generate_password_hash(password)
#
#     def verify_password(self, password):
#         return check_password_hash(self.password_hash, password)
#
#     def get_id(self):
#         return self.username
#
#     # def save(user):
#     #     db.session.add(user)
#     #     db.session.commit()
#
#
# if __name__ == '__main__':
#     db.drop_all()
#     db.create_all()



#loginmanager.anonymous_user = AnonymousUserMixin


# class Role(db.Model):
#     __tablename__ = 'sys_role'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
#     users = db.relationship('User',backref='role',lazy='dynamic')
#
#     def __repr__(self):
#         return '<Role %r>' % self.name