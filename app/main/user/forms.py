# coding = utf-8
# @Time    : 2018/1/30 0030 20:22
# @Author  : Carl
# @Site    : 
# @File    : forms.py
# @Software: PyCharm
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError


# class LoginForm(FlaskForm):
#     username = StringField('Email', validators=[DataRequired(), Length(1, 64)])
#     password = PasswordField('Password', validators=[DataRequired()])
#     remember_me = BooleanField('Keep me logged in')
#     submit = SubmitField('Log In')