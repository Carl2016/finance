# coding:utf-8
from flask import request, flash, render_template, redirect, url_for, jsonify, Response, globals
from app.stock import stock
import json
import tushare as ts
import pandas as pd
import numpy as np
from exts import db
import matplotlib.pyplot as plt
from app.stock.models import *
import datetime
from app.common.alchemyEncoder import AlchemyEncoder


def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@stock.route('/list', methods=["GET"])
def list():
    return render_template('stock/stock.html')


@stock.route('/list/ajax', methods=["GET"])
def listAjax():
    #postValues = request.values.get()
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    pagination = Stock.query.paginate(page, limit, error_out=False)
    stocks = pagination.items
    #content = dict(stocks)
    content = json.dumps(stocks, cls=AlchemyEncoder)
    #content = json.dumps(stocks)
    resp = Response_headers(content)
    return resp


@stock.route('/historyPen', methods=['GET','POST'])
def historyPen():
    if request.method == 'POST':
        datas = {
            "data": [
                {"name": "allpe", "num": 100},
                {"name": "peach", "num": 123},
                {"name": "Pear", "num": 234},
                {"name": "avocado", "num": 20},
                {"name": "cantaloupe", "num": 1},
                {"name": "Banana", "num": 77},
                {"name": "Grape", "num": 43},
                {"name": "apricot", "num": 0}
            ]
        }
        content = json.dumps(datas)
        resp = Response_headers(content)
        return resp
    return render_template("stock/historyPen.html")




