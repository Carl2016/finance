# coding:utf-8
from flask import request, flash, render_template, redirect, url_for, jsonify, Response, globals
from app.stock import stock
import json
import tushare as ts
import pandas as pd
import numpy as np
from exts import db
from app.stock.models import *
import datetime
from app.common.alchemyEncoder import AlchemyEncoder


def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


#股票列表
@stock.route('/list', methods=["GET", "POST"])
def list():
    if request.method == 'POST':
        page = request.form['page']
        limit = request.form['limit']
        pagination = StockBasic.query.paginate(int(page), int(limit), error_out=False)
        count = StockBasic.query.paginate(int(page), int(limit), error_out=False).pages
        items = pagination.items
        result = {
            "code": 0,
            "msg": "获取成功",
            "count": count,
            "data": items
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    return render_template('stock/stock.html')


# #股票业绩预告
# @stock.route('/perNotice', methods=["GET", "POST"])
# def perNotice():
#     if request.method == 'POST':
#         page = request.form['page']
#         limit = request.form['limit']
#         pagination = PerformanceNotice.query.paginate(int(page), int(limit), error_out=False)
#         count = PerformanceNotice.query.paginate(int(page), int(limit), error_out=False).pages
#         items = pagination.items
#         result = {
#             "code": 0,
#             "msg": "获取成功",
#             "count": count,
#             "data": items
#         }
#         return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
#     return render_template('stock/stockPerNotice.html')
#
#
# #股票盈利能力
# @stock.route('/profit', methods=["GET", "POST"])
# def profit():
#     if request.method == 'POST':
#         page = request.form['page']
#         limit = request.form['limit']
#         pagination = Profit.query.paginate(int(page), int(limit), error_out=False)
#         count = Profit.query.paginate(int(page), int(limit), error_out=False).pages
#         items = pagination.items
#         result = {
#             "code": 0,
#             "msg": "获取成功",
#             "count": count,
#             "data": items
#         }
#         return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
#     return render_template('stock/stockProfit.html')
#
#
# #股票运营能力
# @stock.route('/operating', methods=["GET", "POST"])
# def operating():
#     if request.method == 'POST':
#         page = request.form['page']
#         limit = request.form['limit']
#         pagination = Operating.query.paginate(int(page), int(limit), error_out=False)
#         count = Operating.query.paginate(int(page), int(limit), error_out=False).pages
#         items = pagination.items
#         result = {
#             "code": 0,
#             "msg": "获取成功",
#             "count": count,
#             "data": items
#         }
#         return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
#     return render_template('stock/stockOperating.html')
#
#
# #股票成长能力
# @stock.route('/growth', methods=["GET", "POST"])
# def growth():
#     if request.method == 'POST':
#         page = request.form['page']
#         limit = request.form['limit']
#         pagination = Growth.query.paginate(int(page), int(limit), error_out=False)
#         count = Growth.query.paginate(int(page), int(limit), error_out=False).pages
#         items = pagination.items
#         result = {
#             "code": 0,
#             "msg": "获取成功",
#             "count": count,
#             "data": items
#         }
#         return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
#     return render_template('stock/stockGrowth.html')
#
#
# #股票偿债能力
# @stock.route('/solvency', methods=["GET", "POST"])
# def solvency():
#     if request.method == 'POST':
#         page = request.form['page']
#         limit = request.form['limit']
#         pagination = Solvency.query.paginate(int(page), int(limit), error_out=False)
#         count = Solvency.query.paginate(int(page), int(limit), error_out=False).pages
#         items = pagination.items
#         result = {
#             "code": 0,
#             "msg": "获取成功",
#             "count": count,
#             "data": items
#         }
#         return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
#     return render_template('stock/stockSolency.html')
#
#
# #股票现金流量
# @stock.route('/cashFlow', methods=["GET", "POST"])
# def cashFlow():
#     if request.method == 'POST':
#         page = request.form['page']
#         limit = request.form['limit']
#         pagination = CashFlow.query.paginate(int(page), int(limit), error_out=False)
#         count = CashFlow.query.paginate(int(page), int(limit), error_out=False).pages
#         items = pagination.items
#         result = {
#             "code": 0,
#             "msg": "获取成功",
#             "count": count,
#             "data": items
#         }
#         return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
#     return render_template('stock/stockCashFlow.html')
#
#
# #交易数据-股票实时分笔
# @stock.route('/realTimePen', methods=["GET", "POST"])
# def realTimePen():
#     if request.method == 'POST':
#         page = request.form['page']
#         limit = request.form['limit']
#         pagination = RealTimePen.query.paginate(int(page), int(limit), error_out=False)
#         count = RealTimePen.query.paginate(int(page), int(limit), error_out=False).pages
#         items = pagination.items
#         result = {
#             "code": 0,
#             "msg": "获取成功",
#             "count": count,
#             "data": items
#         }
#         return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
#     return render_template('stock/stockRealTimePen.html')
#
#
# #交易数据-股票历史行情
# @stock.route('/historicalQuotes', methods=["GET", "POST"])
# def historicalQuotes():
#     if request.method == 'POST':
#         page = request.form['page']
#         limit = request.form['limit']
#         pagination = HistoricalQuotes.query.paginate(int(page), int(limit), error_out=False)
#         count = HistoricalQuotes.query.paginate(int(page), int(limit), error_out=False).pages
#         items = pagination.items
#         result = {
#             "code": 0,
#             "msg": "获取成功",
#             "count": count,
#             "data": items
#         }
#         return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
#     return render_template('stock/stockHistoricaQuotes.html')
#
#
# #交易数据-股票复权数据
# @stock.route('/recoverData', methods=["GET", "POST"])
# def recoverData():
#     if request.method == 'POST':
#         page = request.form['page']
#         limit = request.form['limit']
#         pagination = RecoverData.query.paginate(int(page), int(limit), error_out=False)
#         count = RecoverData.query.paginate(int(page), int(limit), error_out=False).pages
#         items = pagination.items
#         result = {
#             "code": 0,
#             "msg": "获取成功",
#             "count": count,
#             "data": items
#         }
#         return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
#     return render_template('stock/stockRecoverData.html')
#
#
# #交易数据-股票实时行情
# @stock.route('/realTimeMarket', methods=["GET", "POST"])
# def realTimeMarket():
#     if request.method == 'POST':
#         page = request.form['page']
#         limit = request.form['limit']
#         pagination = RealTimeMarket.query.paginate(int(page), int(limit), error_out=False)
#         count = RealTimeMarket.query.paginate(int(page), int(limit), error_out=False).pages
#         items = pagination.items
#         result = {
#             "code": 0,
#             "msg": "获取成功",
#             "count": count,
#             "data": items
#         }
#         return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
#     return render_template('stock/stockRealTimeMarket.html')
#
#
# #交易数据-股票历史分笔
# @stock.route('/historyPen', methods=["GET", "POST"])
# def historyPen():
#     if request.method == 'POST':
#         page = request.form['page']
#         limit = request.form['limit']
#         pagination = HistoryPen.query.paginate(int(page), int(limit), error_out=False)
#         count = HistoryPen.query.paginate(int(page), int(limit), error_out=False).pages
#         items = pagination.items
#         result = {
#             "code": 0,
#             "msg": "获取成功",
#             "count": count,
#             "data": items
#         }
#         return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
#     return render_template('stock/stockHistoryPen.html')
#
#
# #交易数据-股票当日历史分笔
# @stock.route('/todayHistoryPen', methods=["GET", "POST"])
# def todayHistoryPen():
#     if request.method == 'POST':
#         page = request.form['page']
#         limit = request.form['limit']
#         pagination = TodayHistoryPen.query.paginate(int(page), int(limit), error_out=False)
#         count = TodayHistoryPen.query.paginate(int(page), int(limit), error_out=False).pages
#         items = pagination.items
#         result = {
#             "code": 0,
#             "msg": "获取成功",
#             "count": count,
#             "data": items
#         }
#         return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
#     return render_template('stock/stockTodayHistoryPen.html')
#
#
# #交易数据-股票大盘指数行情列表
# @stock.route('/marketIndex', methods=["GET", "POST"])
# def marketIndex():
#     if request.method == 'POST':
#         page = request.form['page']
#         limit = request.form['limit']
#         pagination = MarketIndex.query.paginate(int(page), int(limit), error_out=False)
#         count = MarketIndex.query.paginate(int(page), int(limit), error_out=False).pages
#         items = pagination.items
#         result = {
#             "code": 0,
#             "msg": "获取成功",
#             "count": count,
#             "data": items
#         }
#         return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
#     return render_template('stock/stockMarketIndex.html')
#
#
# #交易数据-股票大单交易数据
# @stock.route('/bigSingleTransactionData', methods=["GET", "POST"])
# def bigSingleTransactionData():
#     if request.method == 'POST':
#         page = request.form['page']
#         limit = request.form['limit']
#         pagination = BigSingleTransactionData.query.paginate(int(page), int(limit), error_out=False)
#         count = BigSingleTransactionData.query.paginate(int(page), int(limit), error_out=False).pages
#         items = pagination.items
#         result = {
#             "code": 0,
#             "msg": "获取成功",
#             "count": count,
#             "data": items
#         }
#         return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
#     return render_template('stock/stockBigSingleTransactionData.html')










# @stock.route('/historyPen', methods=['GET', 'POST'])
# def historyPen():
#     if request.method == 'POST':
#         datas = {
#             "data": [
#                 {"name": "allpe", "num": 100},
#                 {"name": "peach", "num": 123},
#                 {"name": "Pear", "num": 234},
#                 {"name": "avocado", "num": 20},
#                 {"name": "cantaloupe", "num": 1},
#                 {"name": "Banana", "num": 77},
#                 {"name": "Grape", "num": 43},
#                 {"name": "apricot", "num": 0}
#             ]
#         }
#         content = json.dumps(datas)
#         resp = Response_headers(content)
#         return resp
#     return render_template("stock/historyPen.html")




