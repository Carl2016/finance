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


def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@stock.route('/initHistoryPen', methods=['GET'])
def initHistoryPen():
    stocks = ts.get_tick_data('300345', date='2018-02-07')
    for index, row in stocks.iterrows():
        dtstr = '2018-02-07 '+ row['time']
        print(dtstr)
        historyPen = HistoryPen()
        historyPen.code = u'300345'
        historyPen.name = u'红宇新材'
        historyPen.dateTime = datetime.datetime.strptime(dtstr, "%Y-%m-%d %H:%M:%S")
        historyPen.time = row['time']
        historyPen.price = row['price']
        historyPen.change = row['change']
        historyPen.volume = row['volume']
        historyPen.amount = row['amount']
        historyPen.type = row['type']
        globals.db.add(historyPen)
        globals.db.commit()
    return '成功'


@stock.route('/initStock', methods=['GET'])
def initStock():
    df = ts.get_stock_basics()
    for index, row in df.iterrows():
        stock = Stock()
        time = str(row['timeToMarket'])
        dateTime = time[0:4] + "-" + time[4:6] + "-" + time[6:8]
        stock.code = index
        stock.name = row['name']
        stock.industry = row['industry']
        stock.area = row['area']
        stock.pe = row['pe']
        stock.outStanding = row['outstanding']
        stock.totals = row['totals']
        stock.totalAssets = row['totalAssets']
        stock.liquidAssets = row['liquidAssets']
        stock.reserved = row['reserved']
        stock.reservedPerShare = row['reservedPerShare']
        stock.esp = row['esp']
        stock.bvps = row['bvps']
        stock.pb = row['pb']
        if len(dateTime) == 10:
            stock.timeToMarketDateTime = datetime.datetime.strptime(dateTime, "%Y-%m-%d")
            stock.timeToMarket = time
        stock.undp = row['undp']
        stock.perundp = row['perundp']
        stock.rev = row['rev']
        stock.profit = row['profit']
        stock.gpr = row['gpr']
        stock.npr = row['npr']
        stock.holders = row['holders']
        globals.db.add(stock)
        globals.db.commit()
    return '成功'


@stock.route('/initStockResults', methods=['GET'])
def initStockResults():
    df = ts.get_report_data(2014,3)
    for index, row in df.iterrows():
        results = Results()
        results.code = row['code']
        results.name = row['name']
        # bvps = row['bvps']
        # eps = row['eps']
        # eps_yoy = row['eps_yoy']
        # epcf = row['epcf']
        # net_profits = row['net_profits']
        # profits_yoy = row['profits_yoy']
        # report_date = row['report_date']
        # eps = row['eps']
        # if pd.isnull(eps):
        #     print(eps)
        if pd.notnull(row['bvps']):
            results.bvps = row['bvps']
        if pd.notnull(row['eps']):
            results.eps = row['eps']
        if pd.notnull(row['eps_yoy']):
            results.epsYoy = row['eps_yoy']
        if pd.notnull(row['roe']):
            results.roe = row['roe']
        if pd.notnull(row['epcf']):
            results.epcf = row['epcf']
        if pd.notnull(row['net_profits']):
            results.netProfits = row['net_profits']
        if pd.notnull(row['distrib']):
            results.distrib = row['distrib']
        if pd.notnull(row['profits_yoy']):
            results.profits_yoy = row['profits_yoy']
        results.reportDate = row['report_date']
        globals.db.add(results)
        globals.db.commit()
    return '成功'


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


@stock.route('/stock', methods=['GET'])
def add():
    # df = ts.broker_tops()
    # stock = Stock(u"0000002", u"小白")
    s_z_kk = Stock()
    s_z_kk.code = u"dfdww11djmdkd2f"
    s_z_kk.name = u'ss22s'
    globals.db.add(s_z_kk)
    globals.db.commit()
    return 'html'


@stock.route('/list')
def list():
    return render_template('stock/stock.html')

