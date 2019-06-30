# coding:utf-8
from app.main import db
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from flask import session, abort, globals
import functools


sys_user_role = db.Table('sys_user_role',  # 用户角色关联表
    db.Column('userId', db.Integer, db.ForeignKey('sys_user.id')),
    db.Column('roleId', db.Integer, db.ForeignKey('sys_role.id')),
    db.Column('createTime', db.DateTime, default=datetime.now),
)

sys_role_permission = db.Table('sys_role_permission',  # 角色权限关联表
    db.Column('permissionId', db.Integer, db.ForeignKey('sys_permission.id')),
    db.Column('roleId', db.Integer, db.ForeignKey('sys_role.id')),
    db.Column('createTime', db.DateTime, default=datetime.now),
)

sys_role_menu = db.Table('sys_role_menu',  # 用户菜单关联表
    db.Column('roleId', db.Integer, db.ForeignKey('sys_role.id')),
    db.Column('menuId', db.Integer, db.ForeignKey('sys_menu.id')),
    db.Column('createdTime', db.DateTime, default=datetime.now),
    db.Column('isDelete', db.Boolean, default=False),
)


# 用户
class User(db.Model, UserMixin):
    __tablename__ = 'sys_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False, comment=u'用户名')
    password_hash = db.Column(db.String(128), comment="加密密码")
    email = db.Column(db.String(120), unique=True, comment=u'email')
    phone = db.Column(db.String(20), unique=True, comment=u'手机号码')
    avatar = db.Column(db.String(200), comment=u'头像')
    status = db.Column(db.Integer, default=1, comment=u'状态')
    lastLoginTime = db.Column(db.DATETIME, server_default=func.now(), comment=u'最后登录时间')
    createTime = db.Column(db.DATETIME, server_default=func.now(), comment=u'创建时间')
    createBy = db.Column(db.String(50), comment=u'创建人')
    updateTime = db.Column(db.DATETIME, server_default=func.now(), comment=u'修改时间')
    updateBy = db.Column(db.String(50), comment=u'修改人')

    roles = db.relationship(
        'Role',
        secondary=sys_user_role,
        backref=db.backref('users', lazy='dynamic')
    )

    @property
    def role_names(self):
        strs = ''
        for i in range(len(self.roles)):
            strs = strs + self.roles[i].name + ','
        return strs

    # @property
    # def permissions(self):
    #     permissions = Permission.query.join(sys_role_permission).join(Role).join(sys_user_role).join(User). \
    #         filter(
    #         User.id == self.id
    #     )
    #     return permissions

    @property
    def menus(self):
        menus = Menu.query.join(sys_role_menu).join(Role).join(sys_user_role).join(User). \
            filter(
            User.id == self.id
        ).order_by(Menu.type, Menu.order).all()
        return menus

    def check(self, action):
        permission = self.permissions.filter(Permission.action == action).first()
        return bool(permission)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __init__(self, username, phone):
        self.username = username
        self.password = phone

    @property
    def password(self):
        return self.password_hash
        # raise AttributeError('不能直接获取明文密码！')

    @property
    def create_time(self):
        return self.createTime.strftime('%Y-%m-%d')

    # def auth(method):
    #     @functools.wraps(method)
    #     def wrapper(*args, **kwargs):
    #         user_id = session.get('user_id')
    #         if not user_id:
    #             return abort(403)
    #         return method(*args, **kwargs)
    #
    #     return wrapper

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.username

    def update(self):
        globals.db.commit()

    def delete(self):
        globals.db.delete(self)
        globals.db.commit()

    def save(self):
        globals.db.add(self)
        globals.db.commit()


class Role(db.Model):
    __tablename__ = 'sys_role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True, comment=u'角色名称')
    describe = db.Column(db.String(200), unique=True, comment=u'角色描述')
    status = db.Column(db.Integer, default=1, comment=u'状态')
    createTime = db.Column(db.DATETIME, server_default=func.now(), comment=u'创建时间')
    createBy = db.Column(db.String(50), comment=u'创建人')
    updateTime = db.Column(db.DATETIME, server_default=func.now(), comment=u'修改时间')
    updateBy = db.Column(db.String(50), comment=u'修改人')

    # @property
    # def permissions(self):
    #     permissions = Permission.query.join(sys_role_permission).join(Role).filter(Role.id == self.id)
    #     return permissions

    menus = db.relationship('Menu', secondary=sys_role_menu, backref=db.backref('menus', lazy='dynamic'))

    # @property
    # def menus(self):
    #     menus = Menu.query.join(sys_role_menu).join(Role).filter(Role.id == self.id).order_by(Menu.type, Menu.order).all()
    #     return menus

    @property
    def permission_names(self):
        strs = ''
        for i in range(len(self.menus)):
            strs = strs + self.menus[i].name + ','
        return strs

    @property
    def create_time(self):
        return self.createTime.strftime('%Y-%m-%d')

    @property
    def menu_ids(self):
        ids = []
        for i in range(len(self.menus)):
            if self.menus[i].url is not None:
                ids.append(self.menus[i].id)
        return ids

    def __init__(self):
        pass

    def save(self):
        globals.db.add(self)
        globals.db.commit()

    def update(self):
        globals.db.commit()

    def delete(self):
        globals.db.delete(self)
        globals.db.commit()

    def __repr__(self):
        return '<Role %r>' % self.name


class Permission(db.Model):
    __tablename__ = 'sys_permission'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), comment=u'权限名称')
    action = db.Column(db.String(250), unique=True, comment=u'权限值')
    status = db.Column(db.Integer, default=1, comment=u'状态')
    createTime = db.Column(db.DATETIME, server_default=func.now(), comment=u'创建时间')
    createBy = db.Column(db.String(50), comment=u'创建人')
    updateTime = db.Column(db.DATETIME, server_default=func.now(), comment=u'修改时间')
    updateBy = db.Column(db.String(50), comment=u'修改人')


class Menu(db.Model):
    __tablename__ = 'sys_menu'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    parent_id = db.Column(db.Integer, comment=u'父菜单')
    name = db.Column(db.String(50), comment=u'菜单名称')
    icon = db.Column(db.String(50), comment=u'菜单图标')
    url = db.Column(db.String(250), comment=u'菜单路径')
    order = db.Column(db.SmallInteger, default=0, comment=u'排序')
    type = db.Column(db.Integer, comment=u'类型 0：目录 1：菜单 2：按钮')
    status = db.Column(db.Integer, default=1, comment=u'状态')
    createTime = db.Column(db.DATETIME, server_default=func.now(), comment=u'创建时间')
    createBy = db.Column(db.String(50), comment=u'创建人')
    updateTime = db.Column(db.DATETIME, server_default=func.now(), comment=u'修改时间')
    updateBy = db.Column(db.String(50), comment=u'修改人')

    def save(self):
        globals.db.add(self)
        globals.db.commit()

    def update(self):
        globals.db.commit()

    def delete(self):
        globals.db.delete(self)
        globals.db.commit()

    def __repr__(self):
        return '<Menu %r>' % self.name

