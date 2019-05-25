# coding = utf-8

from flask import render_template
from app.main.common import common


@common.app_errorhandler(404)
def page_not_found(e):
    return render_template('/common/404.html'), 404


@common.app_errorhandler(500)
def inter_server_error(e):
    return render_template('/common/500.html'), 500