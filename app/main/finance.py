# # coding:utf-8
# from flask import Flask, request, flash, render_template, redirect, url_for, jsonify, globals
# from flask import render_template
# from app.admin.views import admin
# from app.stock.views import stock
# from flask_login import LoginManager,login_required
# from flask_security import login_user, logout_user, current_user
# import config
# from exts import db
# from app.user.models import *
# from app.stock.models import *
#
# app = Flask(__name__)
#
# # 使用config文件
# app.config.from_object(config)
#
# # 定义数据库
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/finance?charset=utf8'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#
#
# # 请求之前创建session
# @app.before_request
# def before_request():
#     globals.db = db.session
#
#
# # 请求之后，不管有么有异常,都关闭session
# @app.teardown_request
# def teardown_request(self):
#     db.session.remove()
#
#
# # 初始化数据库
# with app.app_context():
#     db.init_app(app)
#     #db.drop_all()
#     db.create_all()
#
# # 注册路由
# app.register_blueprint(admin, url_prefix='/admin')
# app.register_blueprint(stock, url_prefix='/stock')
#
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_message_category = "info"
# login_manager.session_protection = 'strong'
# login_manager.login_view = "login"  # 定义登录的 视图
# login_manager.login_message = '请登录以访问此页面'  # 定义需要登录访问页面的提示消息
#
#
# # # 注册
# # @app.route('/register', methods=['GET', 'POST'])
# # def register():
# #     form = forms.RegisterForm()
# #     if form.validate_on_submit():
# #         if form.password.data != form.password_again.data:
# #             errors = '两次输入的密码不同'
# #             return render_template('register.html', form=form, errors=errors)
# #         new_user = user_datastore.create_user(email=form.email.data, password=form.password.data)
# #         normal_role = user_datastore.find_role('User')
# #         db.session.add(new_user)
# #         user_datastore.add_role_to_user(new_user, normal_role)
# #         login_user(new_user)
# #         return redirect(url_for('index'))
# #     return render_template('register.html', form=form)
#
#
# # 管理员登录
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if not current_user.is_anonymous:
#         return redirect(url_for('index'))
#     if request.method == 'POST':
#         # 由于request中的form参数以字典的形式存在，故以下语句等价
#         username = request.form.get('username')
#         password = request.form.get('password')
#         user = User.query.filter_by(username = username).first()
#         if not user:
#             flash('该用户不存在')
#         elif password != user.password:
#             flash('密码错误')
#         else:
#             print (user.username)
#             login_user(user, remember=True)
#             next_url = request.args.get('next')
#             return redirect(next_url or url_for('index'))
#     return render_template("system/templates/common/login.html")
#
#
# # 首页
# @app.route('/')
# @login_required
# def index():
#     return render_template("index.html")
#
#
# # 退出
# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()  # 登出用户
#     return redirect('login')
#
#
# if __name__ == '__main__':
#     app.run()
