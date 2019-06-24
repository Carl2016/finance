# coding = utf-8
# @Time    : 2018/1/30 0030 23:23
# @Author  : Carl
# @Site    : 
# @File    : template.py
# @Software: PyCharm

import flask

_base_dic = {
    'code': 0,
}


def error_resp(code, msg):
    return flask.jsonify(error=code, msg=msg)


def register_teml(token):
    return dict({
        'token': token,
    }, **_base_dic)
