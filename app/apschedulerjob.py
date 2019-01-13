# coding:utf-8
from datetime import datetime
import tushare as ts
import pandas as pd
from app.stock.models import *
from app.common import schedulers
import threading


# 股票列表
def initStock():
    df = ts.get_stock_basics()
    items = []
    with schedulers.app.app_context():
        for index, row in df.iterrows():
            # 判断是否存在
            flag = Stock.query.filter(Stock.code == index).first()
            if flag is not None:
                continue
            stock = Stock()
            time = str(row['timeToMarket'])
            date_time = time[0:4] + "-" + time[4:6] + "-" + time[6:8]
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
            if len(date_time) == 10:
                stock.timeToMarketDateTime = datetime.strptime(date_time, "%Y-%m-%d")
                stock.timeToMarket = time
            stock.undp = row['undp']
            stock.perundp = row['perundp']
            stock.rev = row['rev']
            stock.profit = row['profit']
            stock.gpr = row['gpr']
            stock.npr = row['npr']
            stock.holders = row['holders']
            items.append(stock)
        # 添加不存在的
        if items:
            print(threading.currentThread().ident)
            db.session.add_all(items)
            db.session.commit()
            db.session.remove()


# 股票盈利能力
def initStockProfit(year, month):
    df = ts.get_profit_data(year, month)
    items = []
    with schedulers.app.app_context():
        for index, row in df.iterrows():
            # 判断是否存在
            flag = Profit.query.filter(Profit.year == year, Profit.month == month, Profit.code == row['code']).first()
            if flag is not None:
                break
            profit = Profit()
            profit.code = row['code']
            profit.name = row['name']
            profit.year = year
            profit.month = month
            profit.date = datetime.strptime(str(year) + "-" + str(month) + "-1", "%Y-%m-%d")
            if pd.notnull(row['roe']):
                profit.roe = row['roe']
            if pd.notnull(row['net_profit_ratio']):
                profit.netProfitRatio = row['net_profit_ratio']
            if pd.notnull(row['gross_profit_rate']):
                profit.grossProfitRate = row['gross_profit_rate']
            if pd.notnull(row['net_profits']):
                profit.netProfits = row['net_profits']
            if pd.notnull(row['eps']):
                profit.esp = row['eps']
            if pd.notnull(row['business_income']):
                profit.businessIncome = row['business_income']
            if pd.notnull(row['bips']):
                profit.bips = row['bips']
            items.append(profit)
        # 添加不存在的
        if items:
            print(threading.currentThread().ident)
            db.session.add_all(items)
            db.session.commit()
            db.session.remove()


# 股票运营能力
def initStockOperating(year, month):
    df = ts.get_operation_data(year, month)
    items = []
    with schedulers.app.app_context():
        for index, row in df.iterrows():
            # 判断是否存在
            flag = Operating.query.filter(Operating.year == year, Operating.month == month, Operating.code == row['code']).first()
            if flag is not None:
                break
            operating = Operating()
            operating.code = row['code']
            operating.name = row['name']
            operating.year = year
            operating.month = month
            operating.date = datetime.strptime(str(year) + "-" + str(month) + "-1", "%Y-%m-%d")
            if pd.notnull(row['arturnover']):
                operating.arturnOver = row['arturnover']
            if pd.notnull(row['arturndays']):
                operating.arturnDays = row['arturndays']
            if pd.notnull(row['inventory_turnover']):
                operating.inventoryTurnover = row['inventory_turnover']
            if pd.notnull(row['inventory_days']):
                operating.inventoryDays = row['inventory_days']
            if pd.notnull(row['currentasset_turnover']):
                operating.currentAssetTurnover = row['currentasset_turnover']
            if pd.notnull(row['currentasset_days']):
                operating.currentAssetDays = row['currentasset_days']
            items.append(operating)
        # 添加不存在的
        if items:
            print(threading.currentThread().ident)
            db.session.add_all(items)
            db.session.commit()
            db.session.remove()


# 股票成长能力
def initStockGrowth(year, month):
    df = ts.get_growth_data(year, month)
    items = []
    with schedulers.app.app_context():
        for index, row in df.iterrows():
            # 判断是否存在
            flag = Growth.query.filter(Growth.year == year, Growth.month == month, Growth.code == row['code']).first()
            if flag is not None:
                break
            growth = Growth()
            growth.code = row['code']
            growth.name = row['name']
            growth.year = year
            growth.month = month
            growth.date = datetime.strptime(str(year) + "-" + str(month) + "-1", "%Y-%m-%d")
            if pd.notnull(row['mbrg']):
                growth.mbrg = row['mbrg']
            if pd.notnull(row['nprg']):
                growth.nprg = row['nprg']
            if pd.notnull(row['nav']):
                growth.nav = row['nav']
            if pd.notnull(row['targ']):
                growth.targ = row['targ']
            if pd.notnull(row['epsg']):
                growth.epsg = row['epsg']
            if pd.notnull(row['seg']):
                growth.currentAssetDays = row['seg']
            items.append(growth)
        # 添加不存在的
        if items:
            print(threading.currentThread().ident)
            db.session.add_all(items)
            db.session.commit()
            db.session.remove()


# 股票偿债能力
def initStockSolvency(year, month):
    df = ts.get_debtpaying_data(year, month)
    items = []
    with schedulers.app.app_context():
        for index, row in df.iterrows():
            # 判断是否存在
            flag = Solvency.query.filter(Solvency.year == year, Solvency.month == month, Solvency.code == row['code']).first()
            if flag is not None:
                break
            solvency = Solvency()
            solvency.code = row['code']
            solvency.name = row['name']
            solvency.year = year
            solvency.month = month
            solvency.date = datetime.strptime(str(year) + "-" + str(month) + "-1", "%Y-%m-%d")
            if pd.notnull(row['currentratio']):
                if isinstance(row['currentratio'], float):
                    solvency.currentRatio = row['currentratio']
                elif row['currentratio'].find("--") == -1:
                    solvency.currentRatio = row['currentratio']
            if pd.notnull(row['quickratio']):
                if isinstance(row['quickratio'], float):
                    solvency.quickRatio = row['quickratio']
                elif row['quickratio'].find("--") == -1:
                    solvency.quickRatio = row['quickratio']
            if pd.notnull(row['cashratio']):
                if isinstance(row['cashratio'], float):
                    solvency.cashRatio = row['cashratio']
                elif row['cashratio'].find("--") == -1:
                    solvency.cashRatio = row['cashratio']
            if pd.notnull(row['icratio']):
                if isinstance(row['icratio'], float):
                    solvency.icRatio = row['icratio']
                elif row['icratio'].find("--") == -1:
                    solvency.icRatio = row['icratio']
            if pd.notnull(row['sheqratio']):
                if isinstance(row['sheqratio'], float):
                    solvency.sheqRatio = row['sheqratio']
                elif row['sheqratio'].find("--") == -1:
                    solvency.sheqRatio = row['sheqratio']
            if pd.notnull(row['adratio']):
                if isinstance(row['adratio'], float):
                    solvency.adRatio = row['adratio']
                elif row['adratio'].find("--") == -1:
                    solvency.adRatio = row['adratio']
            items.append(solvency)
        # 添加不存在的
        if items:
            print(threading.currentThread().ident)
            db.session.add_all(items)
            db.session.commit()
            db.session.remove()


# 股票现金流量
def initStockCashFlow(year, month):
    df = ts.get_cashflow_data(year, month)
    items = []
    with schedulers.app.app_context():
        for index, row in df.iterrows():
            # 判断是否存在
            flag = CashFlow.query.filter(CashFlow.year == year, CashFlow.month == month, CashFlow.code == row['code']).first()
            if flag is not None:
                break
            cashFlow = CashFlow()
            cashFlow.code = row['code']
            cashFlow.name = row['name']
            cashFlow.year = year
            cashFlow.month = month
            cashFlow.date = datetime.strptime(str(year) + "-" + str(month) + "-1", "%Y-%m-%d")
            if pd.notnull(row['cf_sales']):
                cashFlow.cfSales = row['cf_sales']
            if pd.notnull(row['rateofreturn']):
                cashFlow.rateOfReturn = row['rateofreturn']
            if pd.notnull(row['cf_nm']):
                cashFlow.cfNm = row['cf_nm']
            if pd.notnull(row['cf_liabilities']):
                cashFlow.cfLiabilities = row['cf_liabilities']
            if pd.notnull(row['cashflowratio']):
                cashFlow.cashFlowRatio = row['cashflowratio']
            items.append(cashFlow)
        # 添加不存在的
        if items:
            print(threading.currentThread().ident)
            db.session.add_all(items)
            db.session.commit()
            db.session.remove()


# 股票历史行情
def initStockHistoricalQuotess():
    with schedulers.app.app_context():
        stocks = db.session.execute('select * from stock_details')
        result = stocks.fetchall()
        stocks.close()
    for i in range(len(result)):
        df = ts.get_hist_data(result[i].code)
        items = []
        for index, row in df.iterrows():
            historicalQuotes = HistoricalQuotes()
            historicalQuotes.code = result[i].code
            historicalQuotes.name = result[i].name
            historicalQuotes.date = index
            if pd.notnull(row['open']):
                historicalQuotes.open = row['open']
            if pd.notnull(row['high']):
                historicalQuotes.high = row['high']
            if pd.notnull(row['close']):
                historicalQuotes.close = row['close']
            if pd.notnull(row['low']):
                historicalQuotes.low = row['low']
            if pd.notnull(row['volume']):
                historicalQuotes.volume = row['volume']
            if pd.notnull(row['price_change']):
                historicalQuotes.priceChange = row['price_change']
            if pd.notnull(row['p_change']):
                historicalQuotes.pChange = row['p_change']
            if pd.notnull(row['ma5']):
                historicalQuotes.ma5 = row['ma5']
            if pd.notnull(row['ma10']):
                historicalQuotes.ma10 = row['ma10']
            if pd.notnull(row['ma20']):
                historicalQuotes.ma20 = row['ma20']
            if pd.notnull(row['v_ma5']):
                historicalQuotes.vMa5 = row['v_ma5']
            if pd.notnull(row['v_ma10']):
                historicalQuotes.vMa10 = row['v_ma10']
            if pd.notnull(row['v_ma20']):
                historicalQuotes.vMa20 = row['v_ma20']
            # if pd.notnull(row['turnover']):
            #     historicalQuotes.turnover = row['turnover']
            items.append(historicalQuotes)
            # 添加不存在的
            with schedulers.app.app_context():
                db.session.add_all(items)
                db.session.commit()
    db.session.remove()


# 股票复权数据
def initStockRecoverData():
    # 两个日期之间的前复权数据
    df = ts.get_h_data('002337', start='2015-01-01', end='2015-03-16')
    for index, row in df.iterrows():
        recoverData = RecoverData()
        recoverData.code = u'600848'
        recoverData.name = u'上海临港'
        recoverData.date = index
        if pd.notnull(row['open']):
            recoverData.open = row['open']
        if pd.notnull(row['high']):
            recoverData.high = row['high']
        if pd.notnull(row['close']):
            recoverData.close = row['close']
        if pd.notnull(row['low']):
            recoverData.low = row['low']
        if pd.notnull(row['volume']):
            recoverData.volume = row['volume']
        if pd.notnull(row['amount']):
            recoverData.amount = row['amount']
        globals.db.add(recoverData)
        globals.db.commit()
    return '成功'


# 股票实时行情
def initStockRealTimeMarket():
    df = ts.get_today_all()
    with schedulers.app.app_context():
        items = []
        for index, row in df.iterrows():
            realTimeMarket = RealTimeMarket()
            realTimeMarket.code = row['code']
            realTimeMarket.name = row['name']
            if pd.notnull(row['open']):
                realTimeMarket.open = row['open']
            if pd.notnull(row['high']):
                realTimeMarket.high = row['high']
            if pd.notnull(row['low']):
                realTimeMarket.low = row['low']
            if pd.notnull(row['volume']):
                realTimeMarket.volume = row['volume']
            if pd.notnull(row['amount']):
                realTimeMarket.amount = row['amount']
            if pd.notnull(row['changepercent']):
                realTimeMarket.changepercent = row['changepercent']
            if pd.notnull(row['trade']):
                realTimeMarket.trade = row['trade']
            if pd.notnull(row['settlement']):
                realTimeMarket.settlement = row['settlement']
            if pd.notnull(row['turnoverratio']):
                realTimeMarket.turnoverratio = row['turnoverratio']
            if pd.notnull(row['per']):
                realTimeMarket.per = row['per']
            if pd.notnull(row['pb']):
                realTimeMarket.per = row['pb']
            if pd.notnull(row['mktcap']):
                realTimeMarket.per = row['mktcap']
            if pd.notnull(row['nmc']):
                realTimeMarket.nmc = row['nmc']
            items.append(realTimeMarket)
        # 添加不存在的
        if items:
            print(threading.currentThread().ident)
            db.session.add_all(items)
            db.session.commit()
            db.session.remove()


# 股票历史分笔
def initHistoryPen():
    stocks = ts.get_tick_data('300345', date='2018-02-07')
    with schedulers.app.app_context():
        items = []
        for index, row in stocks.iterrows():
            dtstr = '2018-02-07 ' + row['time']
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
            items.append(historyPen)
        # 添加不存在的
        if items:
            print(threading.currentThread().ident)
            db.session.add_all(items)
            db.session.commit()
            db.session.remove()


# 股票实时分笔
def initStockRealTimePen():
    df = ts.get_realtime_quotes('000581')
    for index, row in df.iterrows():
        realTimePen = RealTimePen()
        dtstr = '2018-02-07 ' + row['time']
        realTimePen.code = u'600848'
        realTimePen.name = u'上海临港'
        if pd.notnull(row['open']):
            realTimePen.open = row['open']
        if pd.notnull(row['high']):
            realTimePen.high = row['high']
        if pd.notnull(row['price']):
            realTimePen.price = row['price']
        if pd.notnull(row['pre_close']):
            realTimePen.preClose = row['pre_close']
        if pd.notnull(row['low']):
            realTimePen.low = row['low']
        if pd.notnull(row['volume']):
            realTimePen.volume = row['volume']
        if pd.notnull(row['amount']):
            realTimePen.amount = row['amount']
        if pd.notnull(row['ask']):
            realTimePen.ask = row['ask']
        if pd.notnull(row['bid']):
            realTimePen.bid = row['bid']
        if pd.notnull(row['b1_v']):
            realTimePen.b1Volume = row['b1_v']
        if pd.notnull(row['b2_v']):
            realTimePen.b2Volume = row['b2_v']
        if pd.notnull(row['b3_v']):
            realTimePen.b3Volume = row['b3_v']
        if pd.notnull(row['b4_v']):
            realTimePen.b4Volume = row['b4_v']
        if pd.notnull(row['b5_v']):
            realTimePen.b5Volume = row['b5_v']
        if pd.notnull(row['b1_p']):
            realTimePen.b1Price = row['b1_p']
        if pd.notnull(row['b2_p']):
            realTimePen.b2Price = row['b2_p']
        if pd.notnull(row['b3_p']):
            realTimePen.b3Price = row['b3_p']
        if pd.notnull(row['b4_p']):
            realTimePen.b4Price = row['b4_p']
        if pd.notnull(row['b5_p']):
            realTimePen.b5Price = row['b5_p']
        if pd.notnull(row['a1_v']):
            realTimePen.a1Volume = row['a1_v']
        if pd.notnull(row['a2_v']):
            realTimePen.a2Volume = row['a2_v']
        if pd.notnull(row['a3_v']):
            realTimePen.a3Volume = row['a3_v']
        if pd.notnull(row['a4_v']):
            realTimePen.a4Volume = row['a4_v']
        if pd.notnull(row['a5_v']):
            realTimePen.a5Volume = row['a5_v']
        if pd.notnull(row['a1_p']):
            realTimePen.a1Price = row['a1_p']
        if pd.notnull(row['a2_p']):
            realTimePen.a2Price = row['a2_p']
        if pd.notnull(row['a3_p']):
            realTimePen.a3Price = row['a3_p']
        if pd.notnull(row['a4_p']):
            realTimePen.a4Price = row['a4_p']
        if pd.notnull(row['a5_p']):
            realTimePen.a5Price = row['a5_p']
        realTimePen.dateTime = datetime.datetime.strptime(dtstr, "%Y-%m-%d %H:%M:%S")
        realTimePen.date = row['date']
        realTimePen.time = row['time']
        globals.db.add(realTimePen)
        globals.db.commit()
    return '成功'


# 股票当日历史分笔
def initTodayHistoryPen():
    df = ts.get_today_ticks('300345')
    for index, row in df.iterrows():
        dtstr = '2018-02-07 '+ row['time']
        todayHistoryPen = TodayHistoryPen()
        todayHistoryPen.code = u'300345'
        todayHistoryPen.name = u'红宇新材'
        todayHistoryPen.dateTime = datetime.datetime.strptime(dtstr, "%Y-%m-%d %H:%M:%S")
        todayHistoryPen.time = row['time']
        todayHistoryPen.price = row['price']
        todayHistoryPen.change = row['change']
        todayHistoryPen.volume = row['volume']
        todayHistoryPen.amount = row['amount']
        todayHistoryPen.type = row['type']
        globals.db.add(todayHistoryPen)
        globals.db.commit()
    return '成功'


# 股票大盘指数行情列表
def initStockMarketIndex():
    df = ts.get_index()
    for index, row in df.iterrows():
        marketIndex = MarketIndex()
        dtstr = '2018-02-07 '
        marketIndex.code = row['code']
        marketIndex.name = row['name']
        if pd.notnull(row['open']):
            marketIndex.open = round(row['open'], 4)
        if pd.notnull(row['high']):
            marketIndex.high = round(row['high'], 4)
        if pd.notnull(row['close']):
            marketIndex.close = row['close']
        if pd.notnull(row['low']):
            marketIndex.low = row['low']
        if pd.notnull(row['volume']):
            marketIndex.volume = row['volume']
        if pd.notnull(row['amount']):
            marketIndex.amount = row['amount']
        if pd.notnull(row['preclose']):
            marketIndex.preClose = row['preclose']
        if pd.notnull(row['change']):
            marketIndex.change = row['change']
        #marketIndex.dateTime = datetime.datetime.strptime(dtstr, "%Y-%m-%d %H:%M:%S")
        globals.db.add(marketIndex)
        globals.db.commit()
    return '成功'


# 股票大单交易数据
def initBigSingleTransactionData():
    # 默认400手
    df = ts.get_sina_dd('300345', date='2017-12-24', vol=500) #默认400手
    for index, row in df.iterrows():
        bigSingleTransactionData = BigSingleTransactionData()
        dtstr = '2018-02-07 ' + row['time']
        bigSingleTransactionData.code = row['code']
        bigSingleTransactionData.name = row['name']
        if pd.notnull(row['time']):
            bigSingleTransactionData.time = row['time']
        if pd.notnull(row['price']):
            bigSingleTransactionData.price = row['price']
        if pd.notnull(row['volume']):
            bigSingleTransactionData.volume = row['volume']
        if pd.notnull(row['amount']):
            bigSingleTransactionData.amount = row['amount']
        if pd.notnull(row['preprice']):
            bigSingleTransactionData.preprice = row['preprice']
        if pd.notnull(row['type']):
            bigSingleTransactionData.type = row['type']
        bigSingleTransactionData.dateTime = datetime.datetime.strptime(dtstr, "%Y-%m-%d %H:%M:%S")
        globals.db.add(bigSingleTransactionData)
        globals.db.commit()
    return '成功'


# 股票分配预案
def initDistributionPlan():
    df = ts.profit_data(top=60)
    for index, row in df.iterrows():
        distributionPlan = DistributionPlan()
        dtstr = row['report_date'] + ' 00:00:00'
        distributionPlan.code = row['code']
        distributionPlan.name = row['name']
        if pd.notnull(row['year']):
            distributionPlan.year = row['year']
        if pd.notnull(row['report_date']):
            distributionPlan.reportDate = row['report_date']
        if pd.notnull(row['divi']):
            distributionPlan.divi = row['divi']
        if pd.notnull(row['shares']):
            distributionPlan.shares = row['shares']
        distributionPlan.dateTime = datetime.datetime.strptime(dtstr, "%Y-%m-%d %H:%M:%S")
        globals.db.add(distributionPlan)
        globals.db.commit()
    return '成功'


# 股票业绩预告
def initPerformanceNotice():
    df = ts.forecast_data(2014, 2)
    for index, row in df.iterrows():
        performanceNotice = PerformanceNotice()
        dtstr = row['report_date'] + ' 00:00:00'
        performanceNotice.code = row['code']
        performanceNotice.name = row['name']
        if pd.notnull(row['type']):
            performanceNotice.type = row['type']
        if pd.notnull(row['pre_eps']):
            performanceNotice.preEps = row['pre_eps']
        if pd.notnull(row['range']) :
            performanceNotice.range = row['range']
            # if row['range'].find("%") == -1:
            #     performanceNotice.range = row['range']
            # else:
            #     range = row['range'].strip().lstrip().rstrip('%')
            #     performanceNotice.range = range
        if pd.notnull(dtstr):
            performanceNotice.dateTime = datetime.datetime.strptime(dtstr, "%Y-%m-%d %H:%M:%S")
            performanceNotice.reportDate = datetime.datetime.strptime(dtstr, "%Y-%m-%d %H:%M:%S")
        globals.db.add(performanceNotice)
        globals.db.commit()
    return '成功'


# 股票限售股解禁
def initRestrictedSharesLifted():
    df = ts.xsg_data()
    for index, row in df.iterrows():
        restrictedSharesLifted = RestrictedSharesLifted()
        dtstr = row['date'] + ' 00:00:00'
        restrictedSharesLifted.code = row['code']
        restrictedSharesLifted.name = row['name']
        if pd.notnull(row['date']):
            restrictedSharesLifted.date = row['date']
        if pd.notnull(row['count']):
            restrictedSharesLifted.count = row['count']
        if pd.notnull(row['ratio']):
            restrictedSharesLifted.ratio = row['ratio']
        restrictedSharesLifted.dateTime = datetime.datetime.strptime(dtstr, "%Y-%m-%d %H:%M:%S")
        globals.db.add(restrictedSharesLifted)
        globals.db.commit()
    return '成功'


# 股票基金持股
def initFundHoldings():
    df = ts.fund_holdings(2014, 4)
    for index, row in df.iterrows():
        fundHoldings = FundHoldings()
        dtstr = row['date'] + ' 00:00:00'
        fundHoldings.code = row['code']
        fundHoldings.name = row['name']
        if pd.notnull(row['date']):
            fundHoldings.date = row['date']
        if pd.notnull(row['nums']):
            fundHoldings.nums = row['nums']
        if pd.notnull(row['nlast']):
            fundHoldings.nlast = row['nlast']
        if pd.notnull(row['count']):
            fundHoldings.count = row['count']
        if pd.notnull(row['clast']):
            fundHoldings.clast = row['clast']
        if pd.notnull(row['amount']):
            fundHoldings.amount = row['amount']
        if pd.notnull(row['ratio']):
            fundHoldings.ratio = row['ratio']
        fundHoldings.dateTime = datetime.datetime.strptime(dtstr, "%Y-%m-%d %H:%M:%S")
        globals.db.add(fundHoldings)
        globals.db.commit()
    return '成功'


# 股票新股数据
def initIpoData():
    df = ts.new_stocks()
    for index, row in df.iterrows():
        ipoData = IpoData()
        ipoStr = row['ipo_date'] + ' 00:00:00'
        issStr = row['issue_date'] + ' 00:00:00'
        ipoData.code = row['code']
        ipoData.name = row['name']
        if pd.notnull(row['ipo_date']):
            ipoData.ipoDate = row['ipo_date']
        if pd.notnull(row['issue_date']):
            ipoData.issueDate = row['issue_date']
        if pd.notnull(row['amount']):
            ipoData.amount = row['amount']
        if pd.notnull(row['markets']):
            ipoData.markets = row['markets']
        if pd.notnull(row['price']):
            ipoData.price = row['price']
        if pd.notnull(row['pe']):
            ipoData.pe = row['pe']
        if pd.notnull(row['limit']):
            ipoData.limit = row['limit']
        if pd.notnull(row['funds']):
            ipoData.funds = row['funds']
        if pd.notnull(row['ballot']):
            ipoData.ballot = row['ballot']
        ipoData.ipoDateTime = datetime.datetime.strptime(ipoStr, "%Y-%m-%d %H:%M:%S")
        ipoData.issueDateTime = datetime.datetime.strptime(issStr, "%Y-%m-%d %H:%M:%S")
        globals.db.add(ipoData)
        globals.db.commit()
    return '成功'


# 股票融资融券（沪市）
def initShMarginTrading():
    df = ts.sh_margins(start='2015-01-01', end='2015-04-19')
    for index, row in df.iterrows():
        shMarginTrading = ShMarginTrading()
        str = row['opDate'] + ' 00:00:00'
        shMarginTrading.code = row['code']
        shMarginTrading.name = row['name']
        if pd.notnull(row['opDate']):
            shMarginTrading.opDate = row['opDate']
        if pd.notnull(row['rzye']):
            shMarginTrading.rzye = row['rzye']
        if pd.notnull(row['rzmre']):
            shMarginTrading.rzmre = row['rzmre']
        if pd.notnull(row['rqyl']):
            shMarginTrading.rqyl = row['rqyl']
        if pd.notnull(row['rqylje']):
            shMarginTrading.rqylje = row['rqylje']
        if pd.notnull(row['rqmcl']):
            shMarginTrading.rqmcl = row['rqmcl']
        if pd.notnull(row['rzrqjyzl']):
            shMarginTrading.rzrqjyzl = row['rzrqjyzl']
        shMarginTrading.ipoDateTime = datetime.datetime.strptime(str, "%Y-%m-%d %H:%M:%S")
        globals.db.add(shMarginTrading)
        globals.db.commit()
    return '成功'


# 股票融资融券详细（沪市）
def initShMarginTradingDetails():
    df = ts.sh_margin_details(start='2015-01-01', end='2015-04-19', symbol='601989')
    for index, row in df.iterrows():
        shMarginTradingDetails = ShMarginTradingDetails()
        str = row['opDate'] + ' 00:00:00'
        shMarginTradingDetails.code = row['code']
        shMarginTradingDetails.name = row['name']
        if pd.notnull(row['opDate']):
            shMarginTradingDetails.opDate = row['opDate']
        if pd.notnull(row['stockCode']):
            shMarginTradingDetails.stockCode = row['stockCode']
        if pd.notnull(row['securityAbbr']):
            shMarginTradingDetails.securityAbbr = row['securityAbbr']
        if pd.notnull(row['rzye']):
            shMarginTradingDetails.rzye = row['rzye']
        if pd.notnull(row['rzmre']):
            shMarginTradingDetails.rzmre = row['rzmre']
        if pd.notnull(row['rzche']):
            shMarginTradingDetails.rzche = row['rzche']
        if pd.notnull(row['rqyl']):
            shMarginTradingDetails.rqyl = row['rqyl']
        if pd.notnull(row['rqmcl']):
            shMarginTradingDetails.rqmcl = row['rqmcl']
        if pd.notnull(row['rqchl']):
            shMarginTradingDetails.rqchl = row['rqchl']
        shMarginTradingDetails.dateTime = datetime.datetime.strptime(str, "%Y-%m-%d %H:%M:%S")
        globals.db.add(shMarginTradingDetails)
        globals.db.commit()
    return '成功'


# 股票 融资融券（深市）
def initSzMarginTrading():
    df = ts.sz_margins(start='2015-01-01', end='2015-04-19')
    for index, row in df.iterrows():
        szMarginTrading = SzMarginTrading()
        str = row['opDate'] + ' 00:00:00'
        szMarginTrading.code = row['code']
        szMarginTrading.name = row['name']
        if pd.notnull(row['opDate']):
            szMarginTrading.opDate = row['opDate']
        if pd.notnull(row['rzmre']):
            szMarginTrading.rzmre = row['rzmre']
        if pd.notnull(row['rzye']):
            szMarginTrading.rzye = row['rzye']
        if pd.notnull(row['rqmcl']):
            szMarginTrading.rqmcl = row['rqmcl']
        if pd.notnull(row['rqyl']):
            szMarginTrading.rqyl = row['rqyl']
        if pd.notnull(row['rzche']):
            szMarginTrading.rzche = row['rzche']
        if pd.notnull(row['rqyl']):
            szMarginTrading.rqyl = row['rqyl']
        if pd.notnull(row['rqye']):
            szMarginTrading.rqye = row['rqye']
        if pd.notnull(row['rzrqye']):
            szMarginTrading.rzrqye = row['rzrqye']
        szMarginTrading.dateTime = datetime.datetime.strptime(str, "%Y-%m-%d %H:%M:%S")
        globals.db.add(szMarginTrading)
        globals.db.commit()
    return '成功'


# 股票 融资融券详细（深市）
def initSzMarginTradingDetails():
    df = ts.sz_margin_details('2015-04-20')
    for index, row in df.iterrows():
        szMarginTradingDetails = SzMarginTradingDetails()
        str = row['opDate'] + ' 00:00:00'
        szMarginTradingDetails.code = row['code']
        szMarginTradingDetails.name = row['name']
        if pd.notnull(row['opDate']):
            szMarginTradingDetails.opDate = row['opDate']
        if pd.notnull(row['rzmre']):
            szMarginTradingDetails.rzmre = row['rzmre']
        if pd.notnull(row['rzye']):
            szMarginTradingDetails.rzye = row['rzye']
        if pd.notnull(row['rqmcl']):
            szMarginTradingDetails.rqmcl = row['rqmcl']
        if pd.notnull(row['rqyl']):
            szMarginTradingDetails.rqyl = row['rqyl']
        if pd.notnull(row['rqye']):
            szMarginTradingDetails.rqye = row['rqye']
        if pd.notnull(row['rzrqye']):
            szMarginTradingDetails.rzrqye = row['rzrqye']
        szMarginTradingDetails.dateTime = datetime.datetime.strptime(str, "%Y-%m-%d %H:%M:%S")
        globals.db.add(szMarginTradingDetails)
        globals.db.commit()
    return '成功'


# 股票 每日龙虎榜列表
def initDailyBillboard():
    df = ts.top_list('2016-06-12')
    for index, row in df.iterrows():
        dailyBillboard = DailyBillboard()
        str = row['date'] + ' 00:00:00'
        dailyBillboard.code = row['code']
        dailyBillboard.name = row['name']
        if pd.notnull(row['pchange']):
            dailyBillboard.pchange = row['pchange']
        if pd.notnull(row['amount']):
            dailyBillboard.amount = row['amount']
        if pd.notnull(row['buy']):
            dailyBillboard.buy = row['buy']
        if pd.notnull(row['bratio']):
            dailyBillboard.bratio = row['bratio']
        if pd.notnull(row['sell']):
            dailyBillboard.sell = row['sell']
        if pd.notnull(row['sratio']):
            dailyBillboard.sratio = row['sratio']
        if pd.notnull(row['reason']):
            dailyBillboard.reason = row['reason']
        if pd.notnull(row['date']):
            dailyBillboard.date = row['date']
        dailyBillboard.dateTime = datetime.datetime.strptime(str, "%Y-%m-%d %H:%M:%S")
        globals.db.add(dailyBillboard)
        globals.db.commit()
    return '成功'


# 股票 个股上榜统计
def initStockListCount():
    df = ts.cap_tops()
    for index, row in df.iterrows():
        stockListCount = StockListCount()
        #str = row['date'] + ' 00:00:00'
        stockListCount.code = row['code']
        stockListCount.name = row['name']
        if pd.notnull(row['count']):
            stockListCount.count = row['count']
        if pd.notnull(row['bamount']):
            stockListCount.bamount = row['bamount']
        if pd.notnull(row['samount']):
            stockListCount.samount = row['samount']
        if pd.notnull(row['net']):
            stockListCount.net = row['net']
        if pd.notnull(row['bcount']):
            stockListCount.bcount = row['bcount']
        if pd.notnull(row['scount']):
            stockListCount.scount = row['scount']
        #stockListCount.dateTime = datetime.datetime.strptime(str, "%Y-%m-%d %H:%M:%S")
        globals.db.add(stockListCount)
        globals.db.commit()
    return '成功'


# 股票 营业部上榜统计
def initSalesDepartmentListCount():
    df = ts.broker_tops()
    for index, row in df.iterrows():
        salesDepartmentListCount = SalesDepartmentListCount()
        #str = row['date'] + ' 00:00:00'
        salesDepartmentListCount.code = row['code']
        salesDepartmentListCount.name = row['name']
        if pd.notnull(row['broker']):
            salesDepartmentListCount.broker = row['broker']
        if pd.notnull(row['count']):
            salesDepartmentListCount.count = row['count']
        if pd.notnull(row['bamount']):
            salesDepartmentListCount.bamount = row['bamount']
        if pd.notnull(row['bcount']):
            salesDepartmentListCount.bcount = row['bcount']
        if pd.notnull(row['samount']):
            salesDepartmentListCount.samount = row['samount']
        if pd.notnull(row['scount']):
            salesDepartmentListCount.scount = row['scount']
        if pd.notnull(row['top3']):
            salesDepartmentListCount.top3 = row['top3']
        #stockListCount.dateTime = datetime.datetime.strptime(str, "%Y-%m-%d %H:%M:%S")
        globals.db.add(salesDepartmentListCount)
        globals.db.commit()
    return '成功'


# 股票 机构席位追踪
def initOrganizationSeatTracking():
    df = ts.inst_tops()
    for index, row in df.iterrows():
        organizationSeatTracking = OrganizationSeatTracking()
        #str = row['date'] + ' 00:00:00'
        organizationSeatTracking.code = row['code']
        organizationSeatTracking.name = row['name']
        if pd.notnull(row['bamount']):
            organizationSeatTracking.bamount = row['bamount']
        if pd.notnull(row['bcount']):
            organizationSeatTracking.bcount = row['bcount']
        if pd.notnull(row['samount']):
            organizationSeatTracking.samount = row['samount']
        if pd.notnull(row['scount']):
            organizationSeatTracking.scount = row['scount']
        if pd.notnull(row['net']):
            organizationSeatTracking.net = row['net']
        #stockListCount.dateTime = datetime.datetime.strptime(str, "%Y-%m-%d %H:%M:%S")
        globals.db.add(organizationSeatTracking)
        globals.db.commit()
    return '成功'


# 股票 机构成交明细
def initAgencyTurnoverDetails():
    df = ts.inst_detail()
    for index, row in df.iterrows():
        agencyTurnoverDetails = AgencyTurnoverDetails()
        str = row['date'] + ' 00:00:00'
        agencyTurnoverDetails.code = row['code']
        agencyTurnoverDetails.name = row['name']
        if pd.notnull(row['date']):
            agencyTurnoverDetails.date = row['date']
        if pd.notnull(row['bamount']):
            agencyTurnoverDetails.bamount = row['bamount']
        if pd.notnull(row['samount']):
            agencyTurnoverDetails.samount = row['samount']
        if pd.notnull(row['type']):
            agencyTurnoverDetails.type = row['type']
        agencyTurnoverDetails.dateTime = datetime.datetime.strptime(str, "%Y-%m-%d %H:%M:%S")
        globals.db.add(agencyTurnoverDetails)
        globals.db.commit()
    return '成功'


# 股票 行业分类
def initIndustryCategory():
    df = ts.get_industry_classified()
    for index, row in df.iterrows():
        industryCategory = IndustryCategory()
        industryCategory.code = row['code']
        industryCategory.name = row['name']
        if pd.notnull(row['c_name']):
            industryCategory.cName = row['c_name']
        globals.db.add(industryCategory)
        globals.db.commit()
    return '成功'


# 股票 概念分类
def initConceptCategory():
    df = ts.get_concept_classified()
    for index, row in df.iterrows():
        conceptCategory = ConceptCategory()
        conceptCategory.code = row['code']
        conceptCategory.name = row['name']
        if pd.notnull(row['c_name']):
            conceptCategory.cName = row['c_name']
        globals.db.add(conceptCategory)
        globals.db.commit()
    return '成功'


# 股票 地域分类
def initAreaCategory():
    df = ts.get_area_classified()
    for index, row in df.iterrows():
        areaCategory = AreaCategory()
        areaCategory.code = row['code']
        areaCategory.name = row['name']
        if pd.notnull(row['area']):
            areaCategory.area = row['area']
        globals.db.add(areaCategory)
        globals.db.commit()
    return '成功'


# 股票 中小板分类
def initSmallBoardCategory():
    df = ts.get_sme_classified()
    for index, row in df.iterrows():
        smallBoardCategory = SmallBoardCategory()
        smallBoardCategory.code = row['code']
        smallBoardCategory.name = row['name']
        globals.db.add(smallBoardCategory)
        globals.db.commit()
    return '成功'


# 股票 创业板分类
def initGemCategory():
    df = ts.get_gem_classified()
    for index, row in df.iterrows():
        gemCategory = GemCategory()
        gemCategory.code = row['code']
        gemCategory.name = row['name']
        globals.db.add(gemCategory)
        globals.db.commit()
    return '成功'


# 股票 风险警示板分类
def initRiskWarningCategory():
    df = ts.get_st_classified()
    for index, row in df.iterrows():
        riskWarningCategory = RiskWarningCategory()
        riskWarningCategory.code = row['code']
        riskWarningCategory.name = row['name']
        globals.db.add(riskWarningCategory)
        globals.db.commit()
    return '成功'


# 股票 沪深300成份及权重
def initHs300Weights():
    df = ts.get_hs300s()
    for index, row in df.iterrows():
        str = row['date'] + ' 00:00:00'
        hs300Weights = Hs300Weights()
        hs300Weights.code = row['code']
        hs300Weights.name = row['name']
        if pd.notnull(row['weight']):
            hs300Weights.weight = row['weight']

        hs300Weights.dateTime = datetime.datetime.strptime(str, "%Y-%m-%d %H:%M:%S")
        globals.db.add(hs300Weights)
        globals.db.commit()
    return '成功'


# 股票 上证50成份股
def initSz50Weights():
    df = ts.get_sz50s()
    for index, row in df.iterrows():
        hs300Weights = Hs300Weights()
        hs300Weights.code = row['code']
        hs300Weights.name = row['name']
        globals.db.add(hs300Weights)
        globals.db.commit()
    return '成功'


# 股票 中证500成份股
def initZz500Weights():
    df = ts.get_zz500s()
    for index, row in df.iterrows():
        zz500Weights = Zz500Weights()
        zz500Weights.code = row['code']
        zz500Weights.name = row['name']
        globals.db.add(zz500Weights)
        globals.db.commit()
    return '成功'


# 股票 终止上市股票列表
def initTerminateListing():
    df = ts.get_terminated()
    for index, row in df.iterrows():
        terminateListing = TerminateListing()
        terminateListing.code = row['code']
        terminateListing.name = row['name']
        terminateListing.oDate = row['oDate']
        terminateListing.tDate = row['tDate']
        globals.db.add(terminateListing)
        globals.db.commit()
    return '成功'


# 股票 暂停上市股票列表
def initPauseListing():
    df = ts.get_suspended()
    for index, row in df.iterrows():
        terminateListing = TerminateListing()
        terminateListing.code = row['code']
        terminateListing.name = row['name']
        terminateListing.oDate = row['oDate']
        terminateListing.tDate = row['tDate']
        globals.db.add(terminateListing)
        globals.db.commit()
    return '成功'


# 股票 即时新闻
def initLatestNews():
    df = ts.get_latest_news()
    for index, row in df.iterrows():
        latestNews = LatestNews()
        latestNews.classify = row['classify']
        latestNews.title = row['title']
        latestNews.time = row['time']
        latestNews.url = row['url']
        latestNews.content = row['content']
        globals.db.add(latestNews)
        globals.db.commit()
    return '成功'


# 股票 信息地雷
def initNotices():
    df = ts.get_notices()
    for index, row in df.iterrows():
        notices = Notices()
        notices.title = row['title']
        notices.type = row['type']
        notices.date = row['date']
        notices.url = row['url']
        globals.db.add(notices)
        globals.db.commit()
    return '成功'


# 股票 新浪股吧
def initGubaSina():
    df = ts.get_notices()
    for index, row in df.iterrows():
        gubaSina = GubaSina()
        gubaSina.title = row['title']
        gubaSina.rcounts = row['rcounts']
        gubaSina.ptime = row['ptime']
        gubaSina.content = row['content']
        globals.db.add(gubaSina)
        globals.db.commit()
    return '成功'

