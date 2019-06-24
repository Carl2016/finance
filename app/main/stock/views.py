# coding:utf-8
from flask import request, render_template, Response, globals
from app.main.stock import stock
from flask_login import login_required
import json
from app.main.stock.models import *
from app.main.common.alchemyEncoder import AlchemyEncoder
import datetime
from app.main.utils import utils


def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


# 股票列表
@stock.route('/list', methods=["GET", "POST"])
@login_required
def stockList():
    if request.method == 'POST':
        page = request.form['page']
        limit = request.form['limit']
        pagination = globals.db.query(StockBasic).paginate(int(page), int(limit), error_out=False)
        count = globals.db.query(StockBasic).paginate(int(page), int(limit), error_out=False).pages
        items = pagination.items
        result = {
            "code": 0,
            "msg": "获取成功",
            "count": count,
            "data": items
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    return render_template('stock/stock.html')


# 股票上市公司基本信息
@stock.route('/company', methods=["GET", "POST"])
@login_required
def stockCompany():
    if request.method == 'POST':
        page = request.form['page']
        limit = request.form['limit']
        pagination = globals.db.query(StockCompany).paginate(int(page), int(limit), error_out=False)
        count = globals.db.query(StockCompany).paginate(int(page), int(limit), error_out=False).pages
        items = pagination.items
        result = {
            "code": 0,
            "msg": "获取成功",
            "count": count,
            "data": items
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    return render_template('stock/stockCompany.html')


# 股票IPO新股列表
@stock.route('/newShare', methods=["GET", "POST"])
@login_required
def stockNewShare():
    if request.method == 'POST':
        page = request.form['page']
        limit = request.form['limit']
        pagination = globals.db.query(StockNewShare).paginate(int(page), int(limit), error_out=False)
        count = globals.db.query(StockNewShare).paginate(int(page), int(limit), error_out=False).pages
        items = pagination.items
        result = {
            "code": 0,
            "msg": "获取成功",
            "count": count,
            "data": items
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    return render_template('stock/stockNewShare.html')


# 股票A股复权行情
@stock.route('/proBar', methods=["GET", "POST"])
@login_required
def stockProBar():
    if request.method == 'POST':
        page = request.form['page']
        limit = request.form['limit']
        pagination = globals.db.query(StockProBar).paginate(int(page), int(limit), error_out=False)
        count = globals.db.query(StockProBar).paginate(int(page), int(limit), error_out=False).pages
        items = pagination.items
        result = {
            "code": 0,
            "msg": "获取成功",
            "count": count,
            "data": items
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    return render_template('stock/stockProBar.html')


# 股票复权因子
@stock.route('/adjFactor', methods=["GET", "POST"])
@login_required
def stockAdjFactor():
    if request.method == 'POST':
        page = request.form['page']
        limit = request.form['limit']
        pagination = globals.db.query(StockAdjFactor).paginate(int(page), int(limit), error_out=False)
        count = globals.db.query(StockAdjFactor).paginate(int(page), int(limit), error_out=False).pages
        items = pagination.items
        result = {
            "code": 0,
            "msg": "获取成功",
            "count": count,
            "data": items
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    return render_template('stock/stockAdjFactor.html')


# 股票每日指标
@stock.route('/dailyBasic', methods=["GET", "POST"])
@login_required
def stockDailyBasic():
    if request.method == 'POST':
        page = request.form['page']
        limit = request.form['limit']
        pagination = globals.db.query(StockDailyBasic).paginate(int(page), int(limit), error_out=False)
        count = globals.db.query(StockDailyBasic).paginate(int(page), int(limit), error_out=False).pages
        items = pagination.items
        result = {
            "code": 0,
            "msg": "获取成功",
            "count": count,
            "data": items
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    return render_template('stock/stockDailyBasic.html')


# 股票停复牌
@stock.route('/suspend', methods=["GET", "POST"])
@login_required
def stockSuspend():
    if request.method == 'POST':
        page = request.form['page']
        limit = request.form['limit']
        pagination = globals.db.query(StockSuspend).paginate(int(page), int(limit), error_out=False)
        count = globals.db.query(StockSuspend).paginate(int(page), int(limit), error_out=False).pages
        items = pagination.items
        result = {
            "code": 0,
            "msg": "获取成功",
            "count": count,
            "data": items
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    return render_template('stock/stockSuspend.html')


# 股票利润表
@stock.route('/income', methods=["GET", "POST"])
@login_required
def stockIncome():
    if request.method == 'POST':
        page = request.form['page']
        limit = request.form['limit']
        pagination = globals.db.query(StockIncome).paginate(int(page), int(limit), error_out=False)
        count = globals.db.query(StockIncome).paginate(int(page), int(limit), error_out=False).pages
        items = pagination.items
        result = {
            "code": 0,
            "msg": "获取成功",
            "count": count,
            "data": items
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    return render_template('stock/stockIncome.html')


# 股票资产负债表
@stock.route('/balanceSheet', methods=["GET", "POST"])
@login_required
def stockBalanceSheet():
    if request.method == 'POST':
        page = request.form['page']
        limit = request.form['limit']
        pagination = globals.db.query(StockBalanceSheet).paginate(int(page), int(limit), error_out=False)
        count = globals.db.query(StockBalanceSheet).paginate(int(page), int(limit), error_out=False).pages
        items = pagination.items
        result = {
            "code": 0,
            "msg": "获取成功",
            "count": count,
            "data": items
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    return render_template('stock/stockBalanceSheet.html')


# 股票现金流量表
@stock.route('/cashFlow', methods=["GET", "POST"])
@login_required
def stockCashFlow():
    if request.method == 'POST':
        page = request.form['page']
        limit = request.form['limit']
        pagination = globals.db.query(StockCashFlow).paginate(int(page), int(limit), error_out=False)
        count = globals.db.query(StockCashFlow).paginate(int(page), int(limit), error_out=False).pages
        items = pagination.items
        result = {
            "code": 0,
            "msg": "获取成功",
            "count": count,
            "data": items
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    return render_template('stock/stockCashFlow.html')


# 股票业绩预告
@stock.route('/foreCast', methods=["GET", "POST"])
@login_required
def stockForeCast():
    if request.method == 'POST':
        page = request.form['page']
        limit = request.form['limit']
        pagination = StockForeCast.query.paginate(int(page), int(limit), error_out=False)
        count = StockForeCast.query.paginate(int(page), int(limit), error_out=False).pages
        items = pagination.items
        result = {
            "code": 0,
            "msg": "获取成功",
            "count": count,
            "data": items
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    return render_template('stock/stockForeCast.html')


# 股票业绩快报
@stock.route('/express', methods=["GET", "POST"])
@login_required
def stockExpress():
    if request.method == 'POST':
        page = request.form['page']
        limit = request.form['limit']
        pagination = StockExpress.query.paginate(int(page), int(limit), error_out=False)
        count = StockExpress.query.paginate(int(page), int(limit), error_out=False).pages
        items = pagination.items
        result = {
            "code": 0,
            "msg": "获取成功",
            "count": count,
            "data": items
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    return render_template('stock/stockExpress.html')


# 股票分红送股
@stock.route('/dividnd', methods=["GET", "POST"])
@login_required
def stockDividend():
    if request.method == 'POST':
        page = request.form['page']
        limit = request.form['limit']
        pagination = StockDividend.query.paginate(int(page), int(limit), error_out=False)
        count = StockDividend.query.paginate(int(page), int(limit), error_out=False).pages
        items = pagination.items
        result = {
            "code": 0,
            "msg": "获取成功",
            "count": count,
            "data": items
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    return render_template('stock/stockDividend.html')


# 财务审计意见
@stock.route('/finaAudit', methods=["GET", "POST"])
@login_required
def stockFinaAudit():
    if request.method == 'POST':
        page = request.form['page']
        limit = request.form['limit']
        pagination = StockFinaAudit.query.paginate(int(page), int(limit), error_out=False)
        count = StockFinaAudit.query.paginate(int(page), int(limit), error_out=False).pages
        items = pagination.items
        result = {
            "code": 0,
            "msg": "获取成功",
            "count": count,
            "data": items
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    return render_template('stock/stockFinaAudit.html')


# 财务审计意见
@stock.route('/finaMainbz', methods=["GET", "POST"])
@login_required
def stockFinaMainbz():
    if request.method == 'POST':
        page = request.form['page']
        limit = request.form['limit']
        pagination = StockFinaMainbz.query.paginate(int(page), int(limit), error_out=False)
        count = StockFinaMainbz.query.paginate(int(page), int(limit), error_out=False).pages
        items = pagination.items
        result = {
            "code": 0,
            "msg": "获取成功",
            "count": count,
            "data": items
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    return render_template('stock/stockFinaMainbz.html')


#股票日线行情
@stock.route('/daily', methods=["GET", "POST"])
@login_required
def stockDaily():
    if request.method == 'POST':
        params = request.get_json()

        if params is None:
            start_date = request.form['startDate']
            end_date = request.form['endDate']
            code = request.form['code']
        else:
            start_date = params['startDate']
            end_date = params['endDate']
            code = params['code']

        if start_date == '' or end_date == '':
            current_date = utils.getTheMonth(datetime.datetime.today(), 6)
            stock_daily = StockDaily.query.filter(StockDaily.code == code, StockDaily.trade_date >= current_date).order_by(StockDaily.trade_date.asc()).all()
        else:
            stock_daily = StockDaily.query.filter(StockDaily.code == code, StockDaily.trade_date >= start_date, StockDaily.trade_date < end_date).order_by(StockDaily.trade_date.asc()).all()

        count = len(stock_daily)
        name = None
        if count > 0:
            name = stock_daily[1].name
        data2 = []
        for i in range(count):
            data1 = []
            data1.append(stock_daily[i].trade_date.strftime("%Y/%m/%d"))
            data1.append(float(stock_daily[i].open))
            data1.append(float(stock_daily[i].close))
            data1.append(float(stock_daily[i].low))
            data1.append(float(stock_daily[i].high))
            data2.append(data1)

        result = {
            "code": 0,
            "msg": "获取成功",
            "count": count,
            "name": name,
            "data": data2
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    return render_template('stock/stockDaily.html')


#股票周线行情
@stock.route('/weekly', methods=["GET", "POST"])
@login_required
def stockWeekly():
    if request.method == 'POST':
        params = request.get_json()

        if params is None:
            start_date = request.form['startDate']
            end_date = request.form['endDate']
            code = request.form['code']
        else:
            start_date = params['startDate']
            end_date = params['endDate']
            code = params['code']

        if start_date == '' or end_date == '':
            current_date = utils.getTheMonth(datetime.datetime.today(), 12)
            stocks = StockWeekly.query.filter(StockWeekly.code == code, StockWeekly.trade_date >= current_date).order_by(StockWeekly.trade_date.asc()).all()
        else:
            stocks = StockWeekly.query.filter(StockWeekly.code == code, StockWeekly.trade_date >= start_date, StockWeekly.trade_date < end_date).order_by(StockWeekly.trade_date.asc()).all()

        count = len(stocks)
        name = None
        if count > 0:
            name = stocks[1].name
        data2 = []
        for i in range(count):
            data1 = []
            data1.append(stocks[i].trade_date.strftime("%Y/%m/%d"))
            data1.append(float(stocks[i].open))
            data1.append(float(stocks[i].close))
            data1.append(float(stocks[i].low))
            data1.append(float(stocks[i].high))
            data2.append(data1)

        result = {
            "code": 0,
            "msg": "获取成功",
            "count": count,
            "name": name,
            "data": data2
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    return render_template('stock/stockWeekly.html')


#股票月线行情
@stock.route('/monthly', methods=["GET", "POST"])
@login_required
def stockMonthly():
    if request.method == 'POST':
        params = request.get_json()

        if params is None:
            start_date = request.form['startDate']
            end_date = request.form['endDate']
            code = request.form['code']
        else:
            start_date = params['startDate']
            end_date = params['endDate']
            code = params['code']

        if start_date == '' or end_date == '':
            current_date = utils.getTheMonth(datetime.datetime.today(), 24)
            stocks = StockMonthly.query.filter(StockMonthly.code == code, StockMonthly.trade_date >= current_date).order_by(StockMonthly.trade_date.asc()).all()
        else:
            stocks = StockMonthly.query.filter(StockMonthly.code == code, StockMonthly.trade_date >= start_date, StockMonthly.trade_date < end_date).order_by(StockMonthly.trade_date.asc()).all()

        count = len(stocks)
        name = None
        if count > 0:
            name = stocks[1].name
        data2 = []
        for i in range(count):
            data1 = []
            data1.append(stocks[i].trade_date.strftime("%Y/%m/%d"))
            data1.append(float(stocks[i].open))
            data1.append(float(stocks[i].close))
            data1.append(float(stocks[i].low))
            data1.append(float(stocks[i].high))
            data2.append(data1)

        result = {
            "code": 0,
            "msg": "获取成功",
            "count": count,
            "name": name,
            "data": data2
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    return render_template('stock/stockWeekly.html')





