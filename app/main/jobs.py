# coding:utf-8
import json
import datetime
import requests
from app.main.stock.models import *
from app.main import schedulers
import threading
import tushare as ts


# ts.set_token('')
# pro = ts.pro_api()
pro = ts.pro_api('9fa73a58ea99ddfe8fa4a2cf2b9b265a486ea47f50376d7226faab40')


def req_http_api(req_params):
    req = requests.post('http://api.waditu.com', json.dumps(req_params).encode('utf-8'))
    req.encoding
    result = json.loads(req.text)
    if result['code'] != 0:
        raise Exception(result['msg'])
    return result['data']


def query(api_name, fields, **kwargs):
    req_params = {
        'api_name': api_name,
        'token': '9fa73a58ea99ddfe8fa4a2cf2b9b265a486ea47f50376d7226faab40',
        'params': kwargs,
        'fields': fields
    }

    data = req_http_api(req_params)
    columns = data['fields']
    items = data['items']
    return items


# 股票列表
def initStock():
    fields = 'ts_code,symbol,name,area,industry,fullname,enname,exchange,curr_type,list_status,is_hs,market,list_date,delist_date'
    df = pro.query('stock_basic', list_status='L', fields=fields)
    data = json.loads(df.to_json(orient='records'))
    items = []
    with schedulers.app.app_context():
        for i in range(len(data)):
            stock = StockBasic()
            stock.symbol = data[i]['ts_code']
            stock.code = data[i]['symbol']
            stock.name = data[i]['name']
            stock.area = data[i]['area']
            stock.industry = data[i]['industry']
            stock.fullname = data[i]['fullname']
            stock.enname = data[i]['enname']
            stock.market = data[i]['market']
            stock.exchange = data[i]['exchange']
            stock.curr_type = data[i]['curr_type']
            stock.list_status = data[i]['list_status']
            stock.is_hs = data[i]['is_hs']
            list_time = data[i]['list_date']
            delist_time = data[i]['delist_date']
            if delist_time is not None:
                delist_date_time = delist_time[0:4] + "-" + delist_time[4:6] + "-" + delist_time[6:8]
                stock.delist_date = datetime.strptime(delist_date_time, "%Y-%m-%d")
            if list_time is not None:
                list_date_time = list_time[0:4] + "-" + list_time[4:6] + "-" + list_time[6:8]
                stock.list_date = datetime.strptime(list_date_time, "%Y-%m-%d")
            # 判断是否存在
            flag = StockBasic.query.filter(StockBasic.code == data[i]['symbol']).first()
            if flag is not None:
                continue
            items.append(stock)
        # 添加不存在的
        if items:
            print(threading.currentThread().ident)
            db.session.add_all(items)
            db.session.commit()
    db.session.remove()


# 上市公司基本信息
def initStockCompany():
    fields = 'ts_code,exchange,chairman,manager,secretary,reg_capital,setup_date,province,city,introduction,website,email,office,employees,main_business,business_scope'
    df = pro.query('stock_company', exchange='SZSE', fields=fields)
    data = json.loads(df.to_json(orient='records'))
    items = []
    with schedulers.app.app_context():
        for i in range(len(data)):
            item = StockCompany()
            item.code = data[i]['ts_code'][0:6]
            item.symbol = data[i]['ts_code']
            item.exchange = data[i]['exchange']
            item.chairman = data[i]['chairman']
            item.manager = data[i]['manager']
            item.secretary = data[i]['secretary']
            item.reg_capital = data[i]['reg_capital']
            item.setup_date = data[i]['setup_date']
            item.province = data[i]['province']
            item.city = data[i]['city']
            item.introduction = data[i]['introduction']
            item.website = data[i]['website']
            item.email = data[i]['email']
            item.office = data[i]['office']
            item.business_scope = data[i]['business_scope']
            item.employees = data[i]['employees']
            item.main_business = data[i]['main_business']
            # 判断是否存在
            flag = StockCompany.query.filter(StockCompany.symbol == data[i]['ts_code']).first()
            if flag is not None:
                flag.exchange = data[i]['exchange']
                flag.chairman = data[i]['chairman']
                flag.manager = data[i]['manager']
                flag.secretary = data[i]['secretary']
                flag.reg_capital = data[i]['reg_capital']
                flag.setup_date = data[i]['setup_date']
                flag.province = data[i]['province']
                flag.city = data[i]['city']
                flag.introduction = data[i]['introduction']
                flag.website = data[i]['website']
                flag.email = data[i]['email']
                flag.office = data[i]['office']
                flag.business_scope = data[i]['business_scope']
                flag.employees = data[i]['employees']
                flag.main_business = data[i]['main_business']
                db.session.commit()
                continue
            items.append(item)
        # 添加不存在的
        if items:
            print(threading.currentThread().ident)
            db.session.add_all(items)
            db.session.commit()
    db.session.remove()


# 上市IPO新股列表
def initStockNewShare():
    fields = 'ts_code,sub_code,name,ipo_date,issue_date,amount,market_amount,price,pe,limit_amount,funds,ballot'
    end_date = datetime.now().strftime('%Y%m%d')
    df = pro.query('new_share', start_date='20080101', end_date=end_date, fields=fields)
    data = json.loads(df.to_json(orient='records'))
    items = []
    with schedulers.app.app_context():
        for i in range(len(data)):
            item = StockNewShare()
            item.symbol = data[i]['ts_code']
            item.code = data[i]['ts_code'][0:6]
            item.sub_code = data[i]['sub_code']
            item.name = data[i]['name']
            item.ipo_date = data[i]['ipo_date']
            item.issue_date = data[i]['issue_date']
            item.amount = data[i]['amount']
            item.market_amount = data[i]['market_amount']
            item.price = data[i]['price']
            item.pe = data[i]['pe']
            item.limit_amount = data[i]['limit_amount']
            item.funds = data[i]['funds']
            item.ballot = data[i]['ballot']
            # 判断是否存在
            flag = StockNewShare.query.filter(StockNewShare.symbol == data[i]['ts_code']).first()
            if flag is not None:
                continue
            items.append(item)
        # 添加不存在的
        if items:
            print(threading.currentThread().ident)
            db.session.add_all(items)
            db.session.commit()
    db.session.remove()


# 日线行情
def initStockDaily():
    fields = 'ts_code,trade_date,open,high,low,close,pre_close,change,pct_chg,vol,amount'
    end_date = datetime.now().strftime('%Y%m%d')
    with schedulers.app.app_context():
        stockBasics = StockBasic.query.all()
        for j in range(len(stockBasics)):
            # 查询最新的一天记录日期,然后根据时间去跑数据
            daily = StockDaily.query.filter(StockDaily.symbol == stockBasics[j].symbol).order_by(StockDaily.trade_date_str.desc()).first()
            if daily is not None:
                df = pro.query('daily', ts_code=stockBasics[j].symbol, start_date=daily.trade_date_str, end_date=end_date, fields=fields)
            else:
                df = pro.query('daily', ts_code=stockBasics[j].symbol, start_date='19901201', end_date=end_date, fields=fields)
            data = json.loads(df.to_json(orient='records'))
            items = []
            for i in range(len(data)):
                item = StockDaily()
                item.name = stockBasics[j].name
                item.symbol = data[i]['ts_code']
                item.code = data[i]['ts_code'][0:6]
                item.trade_date = datetime.datetime.strptime(data[i]['trade_date'], '%Y%m%d')
                item.trade_date_str = data[i]['trade_date']
                item.open = data[i]['open']
                item.high = data[i]['high']
                item.low = data[i]['low']
                item.close = data[i]['close']
                item.pre_close = data[i]['pre_close']
                item.change = data[i]['change']
                item.pct_chg = data[i]['pct_chg']
                item.vol = data[i]['vol']
                item.amount = data[i]['amount']
                # 判断是否存在
                flag = StockDaily.query.filter(StockDaily.symbol == data[i]['ts_code']).first()
                if flag is not None:
                    continue
                items.append(item)
            # 添加不存在的
            if items:
                db.session.add_all(items)
                db.session.commit()
    db.session.remove()


# 周线行情
def initStockWeekly():
    fields = 'ts_code,trade_date,open,high,low,close,pre_close,change,pct_chg,vol,amount'
    start_date = datetime.now().strftime('%Y%m%d')
    with schedulers.app.app_context():
        stockBasics = StockBasic.query.all()
        for j in range(len(stockBasics)):
            params = {'ts_code': stockBasics[j].symbol, 'trade_date': '', 'start_date': ''}
            data = query('weekly', fields, **params)
            items = []
            for i in range(len(data)):
                item = StockWeekly()
                item.name = stockBasics[j].name
                item.symbol = data[i][0]
                item.code = data[i][0][0:6]
                date_time = data[i][1][0:4] + "-" + data[i][1][4:6] + "-" + data[i][1][6:8]
                item.trade_date = datetime.strptime(date_time, "%Y-%m-%d")
                item.trade_date_str = data[i][1]
                item.open = data[i][2]
                item.high = data[i][3]
                item.low = data[i][4]
                item.close = data[i][5]
                item.pre_close = data[i][6]
                item.change = data[i][7]
                item.pct_chg = data[i][8]
                item.vol = data[i][9]
                item.amount = data[i][10]
                # 判断是否存在
                flag = StockWeekly.query.filter(StockWeekly.symbol == data[i][0]).first()
                if flag is not None:
                    continue
                items.append(item)
            # 添加不存在的
            if items:
                db.session.add_all(items)
                db.session.commit()
    db.session.remove()


# 月线行情
def initStockMonthly():
    fields = 'ts_code,trade_date,open,high,low,close,pre_close,change,pct_chg,vol,amount'
    start_date = datetime.now().strftime('%Y%m%d')
    with schedulers.app.app_context():
        stockBasics = StockBasic.query.all()
        for j in range(len(stockBasics)):
            params = {'ts_code': stockBasics[j].symbol, 'trade_date': '', 'start_date': ''}
            data = query('monthly', fields, **params)
            items = []
            for i in range(len(data)):
                item = StockMonthly()
                item.name = stockBasics[j].name
                item.symbol = data[i][0]
                item.code = data[i][0][0:6]
                date_time = data[i][1][0:4] + "-" + data[i][1][4:6] + "-" + data[i][1][6:8]
                item.trade_date = datetime.strptime(date_time, "%Y-%m-%d")
                item.trade_date_str = data[i][1]
                item.open = data[i][2]
                item.high = data[i][3]
                item.low = data[i][4]
                item.close = data[i][5]
                item.pre_close = data[i][6]
                item.change = data[i][7]
                item.pct_chg = data[i][8]
                item.vol = data[i][9]
                item.amount = data[i][10]
                # 判断是否存在
                flag = StockMonthly.query.filter(StockMonthly.symbol == data[i][0]).first()
                if flag is not None:
                    continue
                items.append(item)
            # 添加不存在的
            if items:
                db.session.add_all(items)
                db.session.commit()
    db.session.remove()

# 每日指标
def initDailyBasic():
    fields = 'ts_code,trade_date,close,turnover_rate,turnover_rate_f,volume_ratio,pe,pe_ttm,pb,ps,ps_ttm,total_share,float_share,free_share,total_mv,circ_mv'
    start_date = datetime.now().strftime('%Y%m%d')
    with schedulers.app.app_context():
        stockBasics = StockBasic.query.all()
        for j in range(len(stockBasics)):
            df = pro.query('daily_basic', ts_code=stockBasics[j].symbol, fields=fields)
            data = json.loads(df.to_json(orient='records'))
            items = []
            for i in range(len(data)):
                item = StockDailyBasic()
                item.name = stockBasics[j].name
                item.symbol = data[i]['ts_code']
                item.code = data[i]['ts_code'][0:6]
                date_time = data[i]['trade_date'][0:4] + "-" + data[i]['trade_date'][4:6] + "-" + data[i]['trade_date'][6:8]
                item.trade_date = datetime.strptime(date_time, "%Y-%m-%d")
                item.trade_date_str = data[i]['trade_date']
                item.close = data[i]['close']
                item.turnover_rate = data[i]['turnover_rate']
                item.turnover_rate_f = data[i]['turnover_rate_f']
                item.volume_ratio = data[i]['volume_ratio']
                item.pe = data[i]['pe']
                item.pe_ttm = data[i]['pe_ttm']
                item.pb = data[i]['pb']
                item.ps = data[i]['ps']
                item.ps_ttm = data[i]['ps_ttm']
                item.total_share = data[i]['total_share']
                item.float_share = data[i]['float_share']
                item.free_share = data[i]['free_share']
                item.total_mv = data[i]['total_mv']
                item.circ_mv = data[i]['circ_mv']
                # 判断是否存在
                flag = StockDailyBasic.query.filter(StockDailyBasic.symbol == data[i]['ts_code'], StockDailyBasic.trade_date_str == data[i]['trade_date']).first()
                if flag is not None:
                    continue
                items.append(item)
            # 添加不存在的
            if items:
                db.session.add_all(items)
                db.session.commit()
    db.session.remove()


# 利润表
def initStockIncome():
    fields = ''
    start_date = datetime.now().strftime('%Y%m%d')
    with schedulers.app.app_context():
        stockBasics = StockBasic.query.all()
        for j in range(len(stockBasics)):
            params = {'ts_code': stockBasics[j].symbol, 'trade_date': '', 'start_date': ''}
            data = query('income', fields, **params)
            items = []
            for i in range(len(data)):
                item = StockIncome()
                item.name = stockBasics[j].name
                item.symbol = data[i][0]
                item.code = data[i][0][0:6]
                date_time = data[i][1][0:4] + "-" + data[i][1][4:6] + "-" + data[i][1][6:8]
                item.ann_date = datetime.strptime(date_time, "%Y-%m-%d")
                item.ann_date_str = data[i][1]
                item.f_ann_date = data[i][2]
                item.end_date = data[i][3]
                item.report_type = data[i][4]
                item.comp_type = data[i][5]
                item.basic_eps = data[i][6]
                item.diluted_eps = data[i][7]
                item.total_revenue = data[i][8]
                item.revenue = data[i][9]
                item.int_income = data[i][10]
                item.prem_earned = data[i][11]
                item.comm_income = data[i][12]
                item.n_commis_income = data[i][13]
                item.n_oth_income = data[i][14]
                item.n_oth_b_income = data[i][15]
                item.prem_income = data[i][16]
                item.out_prem = data[i][17]
                item.une_prem_reser = data[i][18]
                item.reins_income = data[i][19]
                item.n_sec_tb_income = data[i][20]
                item.n_sec_uw_income = data[i][21]
                item.n_asset_mg_income = data[i][22]
                item.oth_b_income = data[i][23]
                item.fv_value_chg_gain = data[i][24]
                item.invest_income = data[i][25]
                item.ass_invest_income = data[i][26]
                item.forex_gain = data[i][27]
                item.total_cogs = data[i][28]
                item.oper_cost = data[i][29]
                item.int_exp = data[i][30]
                item.comm_exp = data[i][31]
                item.biz_tax_surchg = data[i][32]
                item.sell_exp = data[i][33]
                item.admin_exp = data[i][34]
                item.fin_exp = data[i][35]
                item.assets_impair_loss = data[i][36]
                item.prem_refund = data[i][37]
                item.compens_payout = data[i][38]
                item.reser_insur_liab = data[i][39]
                item.div_payt = data[i][40]
                item.reins_exp = data[i][41]
                item.oper_exp = data[i][42]
                item.compens_payout_refu = data[i][43]
                item.insur_reser_refu = data[i][44]
                item.reins_cost_refund = data[i][45]
                item.other_bus_cost = data[i][46]
                item.operate_profit = data[i][47]
                item.non_oper_income = data[i][48]
                item.non_oper_exp = data[i][49]
                item.nca_disploss = data[i][50]
                item.total_profit = data[i][51]
                item.income_tax = data[i][52]
                item.n_income = data[i][53]
                item.n_income_attr_p = data[i][54]
                item.minority_gain = data[i][55]
                item.oth_compr_income = data[i][56]
                item.t_compr_income = data[i][57]
                item.compr_inc_attr_p = data[i][58]
                item.compr_inc_attr_m_s = data[i][59]
                item.ebit = data[i][60]
                item.ebitda = data[i][61]
                item.insurance_exp = data[i][62]
                item.undist_profit = data[i][63]
                item.distable_profit = data[i][64]
                # 判断是否存在
                flag = StockIncome.query.filter(StockIncome.symbol == data[i][0]).first()
                if flag is not None:
                    continue
                items.append(item)
            # 添加不存在的
            if items:
                db.session.add_all(items)
                db.session.commit()
    db.session.remove()


# 负债
def initBalanceSheet():
    fields = ''
    start_date = datetime.now().strftime('%Y%m%d')
    with schedulers.app.app_context():
        stockBasics = StockBasic.query.all()
        for j in range(len(stockBasics)):
            params = {'ts_code': stockBasics[j].symbol, 'trade_date': '', 'start_date': ''}
            data = query('balancesheet', fields, **params)
            items = []
            for i in range(len(data)):
                item = StockBalanceSheet()
                item.name = stockBasics[j].name
                item.symbol = data[i][0]
                item.code = data[i][0][0:6]
                date_time = data[i][1][0:4] + "-" + data[i][1][4:6] + "-" + data[i][1][6:8]
                item.ann_date = datetime.strptime(date_time, "%Y-%m-%d")
                item.ann_date_str = data[i][1]
                item.f_ann_date = data[i][2]
                item.end_date = data[i][3]
                item.report_type = data[i][4]
                item.comp_type = data[i][5]
                item.total_share = data[i][6]
                item.cap_rese = data[i][7]
                item.undistr_porfit = data[i][8]
                item.surplus_rese = data[i][9]
                item.special_rese = data[i][10]
                item.money_cap = data[i][11]
                item.trad_asset = data[i][12]
                item.notes_receiv = data[i][13]
                item.accounts_receiv = data[i][14]
                item.oth_receiv = data[i][15]
                item.prepayment = data[i][16]
                item.div_receiv = data[i][17]
                item.int_receiv = data[i][18]
                item.inventories = data[i][19]
                item.amor_exp = data[i][20]
                item.nca_within_1y = data[i][21]
                item.sett_rsrv = data[i][22]
                item.loanto_oth_bank_fi = data[i][23]
                item.premium_receiv = data[i][24]
                item.reinsur_receiv = data[i][25]
                item.reinsur_res_receiv = data[i][26]
                item.pur_resale_fa = data[i][27]
                item.oth_cur_assets = data[i][28]
                item.total_cur_assets = data[i][29]
                item.fa_avail_for_sale = data[i][30]
                item.htm_invest = data[i][31]
                item.lt_eqt_invest = data[i][32]
                item.invest_real_estate = data[i][33]
                item.time_deposits = data[i][34]
                item.oth_assets = data[i][35]
                item.lt_rec = data[i][36]
                item.fix_assets = data[i][37]
                item.cip = data[i][38]
                item.const_materials = data[i][39]
                item.fixed_assets_disp = data[i][40]
                item.produc_bio_assets = data[i][41]
                item.oil_and_gas_assets = data[i][42]
                item.intan_assets = data[i][43]
                item.r_and_d = data[i][44]
                item.goodwill = data[i][45]
                item.lt_amor_exp = data[i][46]
                item.defer_tax_assets = data[i][47]
                item.decr_in_disbur = data[i][48]
                item.oth_nca = data[i][49]
                item.total_nca = data[i][50]
                item.cash_reser_cb = data[i][51]
                item.depos_in_oth_bfi = data[i][52]
                item.prec_metals = data[i][53]
                item.deriv_assets = data[i][54]
                item.rr_reins_une_prem = data[i][55]
                item.rr_reins_outstd_cla = data[i][56]
                item.rr_reins_lins_liab = data[i][57]
                item.rr_reins_lthins_liab = data[i][58]
                item.refund_depos = data[i][59]
                item.ph_pledge_loans = data[i][60]
                item.refund_cap_depos = data[i][61]
                item.indep_acct_assets = data[i][62]
                item.client_depos = data[i][63]
                item.client_prov = data[i][64]
                item.transac_seat_fee = data[i][65]
                item.invest_as_receiv = data[i][66]
                item.total_assets = data[i][67]
                item.lt_borr = data[i][68]
                item.st_borr = data[i][69]
                item.cb_borr = data[i][70]
                item.depos_ib_deposits = data[i][71]
                item.loan_oth_bank = data[i][72]
                item.trading_fl = data[i][73]
                item.notes_payable = data[i][74]
                item.acct_payable = data[i][75]
                item.adv_receipts = data[i][76]
                item.sold_for_repur_fa = data[i][77]
                item.comm_payable = data[i][78]
                item.payroll_payable = data[i][79]
                item.taxes_payable = data[i][80]
                item.int_payable = data[i][81]
                item.div_payable = data[i][82]
                item.oth_payable = data[i][83]
                item.acc_exp = data[i][84]
                item.deferred_inc = data[i][85]
                item.st_bonds_payable = data[i][86]
                item.payable_to_reinsurer = data[i][87]
                item.rsrv_insur_cont = data[i][88]
                item.acting_trading_sec = data[i][89]
                item.acting_uw_sec = data[i][90]
                item.non_cur_liab_due_1y = data[i][91]
                item.oth_cur_liab = data[i][92]
                item.total_cur_liab = data[i][93]
                item.bond_payable = data[i][94]
                item.lt_payable = data[i][95]
                item.specific_payables = data[i][96]
                item.estimated_liab = data[i][97]
                item.defer_tax_liab = data[i][98]
                item.defer_inc_non_cur_liab = data[i][99]
                item.oth_ncl = data[i][100]
                item.total_ncl = data[i][101]
                item.depos_oth_bfi = data[i][102]
                item.deriv_liab = data[i][103]
                item.depos = data[i][104]
                item.agency_bus_liab = data[i][105]
                item.oth_liab = data[i][106]
                item.prem_receiv_adva = data[i][107]
                item.depos_received = data[i][108]
                item.ph_invest = data[i][109]
                item.reser_une_prem = data[i][110]
                item.reser_outstd_claims = data[i][111]
                item.reser_lins_liab = data[i][112]
                item.reser_lthins_liab = data[i][113]
                item.indept_acc_liab = data[i][114]
                item.pledge_borr = data[i][115]
                item.indem_payable = data[i][116]
                item.policy_div_payable = data[i][117]
                item.total_liab = data[i][118]
                item.treasury_share = data[i][119]
                item.ordin_risk_reser = data[i][120]
                item.forex_differ = data[i][121]
                item.invest_loss_unconf = data[i][122]
                item.minority_int = data[i][123]
                item.total_hldr_eqy_exc_min_int = data[i][124]
                item.total_hldr_eqy_inc_min_int = data[i][125]
                item.total_liab_hldr_eqy = data[i][126]
                item.lt_payroll_payable = data[i][127]
                item.oth_comp_income = data[i][128]
                item.oth_eqt_tools = data[i][129]
                item.oth_eqt_tools_p_shr = data[i][130]
                item.lending_funds = data[i][131]
                item.acc_receivable = data[i][132]
                item.st_fin_payable = data[i][133]
                item.payables = data[i][134]
                item.hfs_assets = data[i][135]
                item.hfs_sales = data[i][136]
                # 判断是否存在
                flag = StockBalanceSheet.query.filter(StockBalanceSheet.symbol == data[i][0]).first()
                if flag is not None:
                    continue
                items.append(item)
            # 添加不存在的
            if items:
                db.session.add_all(items)
                db.session.commit()
    db.session.remove()


# 现金流量
def initStockCashFlow():
    fields = ''
    start_date = datetime.now().strftime('%Y%m%d')
    with schedulers.app.app_context():
        stockBasics = StockBasic.query.all()
        for j in range(len(stockBasics)):
            params = {'ts_code': stockBasics[j].symbol, 'trade_date': '', 'start_date': ''}
            data = query('cashflow', fields, **params)
            items = []
            for i in range(len(data)):
                item = StockCashFlow()
                item.name = stockBasics[j].name
                item.symbol = data[i][0]
                item.code = data[i][0][0:6]
                date_time = data[i][1][0:4] + "-" + data[i][1][4:6] + "-" + data[i][1][6:8]
                item.ann_date = datetime.strptime(date_time, "%Y-%m-%d")
                item.ann_date_str = data[i][1]
                item.f_ann_date = data[i][2]
                item.end_date = data[i][3]
                item.report_type = data[i][4]
                item.net_profit = data[i][5]
                item.finan_exp = data[i][6]
                item.c_fr_sale_sg = data[i][7]
                item.recp_tax_rends = data[i][8]
                item.n_depos_incr_fi = data[i][9]
                item.n_incr_loans_cb = data[i][10]
                item.n_inc_borr_oth_fi = data[i][11]
                item.prem_fr_orig_contr = data[i][12]
                item.n_incr_insured_dep = data[i][13]
                item.n_reinsur_prem = data[i][14]
                item.n_incr_disp_tfa = data[i][15]
                item.ifc_cash_incr = data[i][16]
                item.n_incr_disp_faas = data[i][17]
                item.n_incr_loans_oth_bank = data[i][18]
                item.n_cap_incr_repur = data[i][19]
                item.c_fr_oth_operate_a = data[i][20]
                item.c_inf_fr_operate_a = data[i][21]
                item.c_paid_goods_s = data[i][22]
                item.c_paid_to_for_empl = data[i][23]
                item.c_paid_for_taxes = data[i][24]
                item.n_incr_clt_loan_adv = data[i][25]
                item.n_incr_dep_cbob = data[i][26]
                item.c_pay_claims_orig_inco = data[i][27]
                item.pay_handling_chrg = data[i][28]
                item.pay_comm_insur_plcy = data[i][29]
                item.oth_cash_pay_oper_act = data[i][30]
                item.st_cash_out_act = data[i][31]
                item.n_cashflow_act = data[i][32]
                item.oth_recp_ral_inv_act = data[i][33]
                item.c_disp_withdrwl_invest = data[i][34]
                item.c_recp_return_invest = data[i][35]
                item.n_recp_disp_fiolta = data[i][36]
                item.n_recp_disp_sobu = data[i][37]
                item.stot_inflows_inv_act = data[i][38]
                item.c_pay_acq_const_fiolta = data[i][39]
                item.c_paid_invest = data[i][40]
                item.n_disp_subs_oth_biz = data[i][41]
                item.oth_pay_ral_inv_act = data[i][42]
                item.n_incr_pledge_loan = data[i][43]
                item.stot_out_inv_act = data[i][44]
                item.n_cashflow_inv_act = data[i][45]
                item.c_recp_borrow = data[i][46]
                item.proc_issue_bonds = data[i][47]
                item.oth_cash_recp_ral_fnc_act = data[i][48]
                item.stot_cash_in_fnc_act = data[i][49]
                item.free_cashflow = data[i][50]
                item.c_prepay_amt_borr = data[i][51]
                item.c_pay_dist_dpcp_int_exp = data[i][52]
                item.incl_dvd_profit_paid_sc_ms = data[i][53]
                item.oth_cashpay_ral_fnc_act = data[i][54]
                item.stot_cashout_fnc_act = data[i][55]
                item.n_cash_flows_fnc_act = data[i][56]
                item.eff_fx_flu_cash = data[i][57]
                item.n_incr_cash_cash_equ = data[i][58]
                item.c_cash_equ_beg_period = data[i][59]
                item.c_cash_equ_end_period = data[i][60]
                item.c_recp_cap_contrib = data[i][61]
                item.incl_cash_rec_saims = data[i][62]
                item.uncon_invest_loss = data[i][63]
                item.prov_depr_assets = data[i][64]
                item.depr_fa_coga_dpba = data[i][65]
                item.amort_intang_assets = data[i][66]
                item.lt_amort_deferred_exp = data[i][67]
                item.decr_deferred_exp = data[i][68]
                item.incr_acc_exp = data[i][69]
                item.loss_disp_fiolta = data[i][70]
                item.loss_scr_fa = data[i][71]
                item.loss_fv_chg = data[i][72]
                item.invest_loss = data[i][73]
                item.decr_def_inc_tax_assets = data[i][74]
                item.incr_def_inc_tax_liab = data[i][75]
                item.decr_inventories = data[i][76]
                item.decr_oper_payable = data[i][77]
                item.incr_oper_payable = data[i][78]
                item.others = data[i][79]
                item.im_net_cashflow_oper_act = data[i][80]
                item.conv_debt_into_cap = data[i][81]
                item.conv_copbonds_due_within_1y = data[i][82]
                item.fa_fnc_leases = data[i][83]
                item.end_bal_cash = data[i][84]
                item.beg_bal_cash = data[i][85]
                item.end_bal_cash_equ = data[i][86]
                item.beg_bal_cash_equ = data[i][87]
                item.im_n_incr_cash_equ = data[i][88]
                # 判断是否存在
                flag = StockCashFlow.query.filter(StockCashFlow.symbol == data[i][0]).first()
                if flag is not None:
                    continue
                items.append(item)
            # 添加不存在的
            if items:
                db.session.add_all(items)
                db.session.commit()
    db.session.remove()


# 业绩预告
def initStockForeCast():
    fields = ''
    start_date = datetime.now().strftime('%Y%m%d')
    with schedulers.app.app_context():
        stockBasics = StockBasic.query.all()
        for j in range(len(stockBasics)):
            params = {'ts_code': stockBasics[j].symbol, 'trade_date': '', 'start_date': ''}
            data = query('forecast', fields, **params)
            items = []
            for i in range(len(data)):
                item = StockForeCast()
                item.name = stockBasics[j].name
                item.symbol = data[i][0]
                item.code = data[i][0][0:6]
                date_time = data[i][1][0:4] + "-" + data[i][1][4:6] + "-" + data[i][1][6:8]
                item.ann_date = datetime.strptime(date_time, "%Y-%m-%d")
                item.ann_date_str = data[i][1]
                item.f_ann_date = data[i][2]
                item.end_date = data[i][3]
                item.type = data[i][4]
                item.p_change_min = data[i][5]
                item.p_change_max = data[i][6]
                item.net_profit_min = data[i][7]
                item.net_profit_max = data[i][8]
                item.last_parent_net = data[i][9]
                item.first_ann_date = data[i][10]
                item.summary = data[i][11]
                item.change_reason = data[i][12]
                # 判断是否存在
                flag = StockForeCast.query.filter(StockForeCast.symbol == data[i][0]).first()
                if flag is not None:
                    continue
                items.append(item)
            # 添加不存在的
            if items:
                db.session.add_all(items)
                db.session.commit()
    db.session.remove()


# 业绩快报
def initStockExpress():
    fields = ''
    start_date = datetime.now().strftime('%Y%m%d')
    with schedulers.app.app_context():
        stockBasics = StockBasic.query.all()
        for j in range(len(stockBasics)):
            params = {'ts_code': stockBasics[j].symbol, 'trade_date': '', 'start_date': ''}
            data = query('express', fields, **params)
            items = []
            for i in range(len(data)):
                item = StockExpress()
                item.name = stockBasics[j].name
                item.symbol = data[i][0]
                item.code = data[i][0][0:6]
                date_time = data[i][1][0:4] + "-" + data[i][1][4:6] + "-" + data[i][1][6:8]
                item.ann_date = datetime.strptime(date_time, "%Y-%m-%d")
                item.ann_date_str = data[i][1]
                item.revenue = data[i][2]
                item.operate_profit = data[i][3]
                item.total_profit = data[i][4]
                item.n_income = data[i][5]
                item.total_assets = data[i][6]
                item.total_hldr_eqy_exc_min_int = data[i][7]
                item.diluted_eps = data[i][8]
                item.diluted_roe = data[i][9]
                item.yoy_net_profit = data[i][10]
                item.bps = data[i][11]
                item.yoy_sales = data[i][12]
                item.yoy_op = data[i][13]
                item.yoy_tp = data[i][14]
                item.yoy_dedu_np = data[i][15]
                item.yoy_eps = data[i][16]
                item.yoy_roe = data[i][17]
                item.growth_assets = data[i][18]
                item.yoy_equity = data[i][19]
                item.growth_bps = data[i][20]
                item.or_last_year = data[i][21]
                item.op_last_year = data[i][22]
                item.tp_last_year = data[i][23]
                item.np_last_year = data[i][24]
                item.eps_last_year = data[i][25]
                item.open_net_assets = data[i][26]
                item.open_bps = data[i][27]
                item.perf_summary = data[i][28]
                item.is_audit = data[i][29]
                item.remark = data[i][30]
                # 判断是否存在
                flag = StockExpress.query.filter(StockExpress.symbol == data[i][0]).first()
                if flag is not None:
                    continue
                items.append(item)
            # 添加不存在的
            if items:
                db.session.add_all(items)
                db.session.commit()
    db.session.remove()


# 分红送股
def initStockDividend():
    fields = ''
    start_date = datetime.now().strftime('%Y%m%d')
    with schedulers.app.app_context():
        stockBasics = StockBasic.query.all()
        for j in range(len(stockBasics)):
            params = {'ts_code': stockBasics[j].symbol, 'trade_date': '', 'start_date': ''}
            data = query('dividend', fields, **params)
            items = []
            for i in range(len(data)):
                item = StockDividend()
                item.name = stockBasics[j].name
                item.symbol = data[i][0]
                item.code = data[i][0][0:6]
                date_time = data[i][1][0:4] + "-" + data[i][1][4:6] + "-" + data[i][1][6:8]
                item.ann_date = datetime.strptime(date_time, "%Y-%m-%d")
                item.ann_date_str = data[i][1]
                item.div_proc = data[i][2]
                item.stk_div = data[i][3]
                item.stk_bo_rate = data[i][4]
                item.stk_co_rate = data[i][5]
                item.cash_div = data[i][6]
                item.cash_div_tax = data[i][7]
                item.record_date = data[i][8]
                item.ex_date = data[i][9]
                item.pay_date = data[i][10]
                item.div_listdate = data[i][11]
                item.imp_ann_date = data[i][12]
                # 判断是否存在
                flag = StockDividend.query.filter(StockDividend.symbol == data[i][0]).first()
                if flag is not None:
                    continue
                items.append(item)
            # 添加不存在的
            if items:
                db.session.add_all(items)
                db.session.commit()
    db.session.remove()


# 分红送股
def initStockDividend():
    fields = ''
    start_date = datetime.now().strftime('%Y%m%d')
    with schedulers.app.app_context():
        stockBasics = StockBasic.query.all()
        for j in range(len(stockBasics)):
            params = {'ts_code': stockBasics[j].symbol, 'trade_date': '', 'start_date': ''}
            data = query('dividend', fields, **params)
            items = []
            for i in range(len(data)):
                item = StockDividend()
                item.name = stockBasics[j].name
                item.symbol = data[i][0]
                item.code = data[i][0][0:6]
                date_time = data[i][1][0:4] + "-" + data[i][1][4:6] + "-" + data[i][1][6:8]
                item.ann_date = datetime.strptime(date_time, "%Y-%m-%d")
                item.ann_date_str = data[i][1]
                item.div_proc = data[i][2]
                item.stk_div = data[i][3]
                item.stk_bo_rate = data[i][4]
                item.stk_co_rate = data[i][5]
                item.cash_div = data[i][6]
                item.cash_div_tax = data[i][7]
                item.record_date = data[i][8]
                item.ex_date = data[i][9]
                item.pay_date = data[i][10]
                item.div_listdate = data[i][11]
                item.imp_ann_date = data[i][12]
                # 判断是否存在
                flag = StockDividend.query.filter(StockDividend.symbol == data[i][0]).first()
                if flag is not None:
                    continue
                items.append(item)
            # 添加不存在的
            if items:
                db.session.add_all(items)
                db.session.commit()
    db.session.remove()


# 分红送股
def initStockDividend():
    fields = ''
    start_date = datetime.now().strftime('%Y%m%d')
    with schedulers.app.app_context():
        stockBasics = StockBasic.query.all()
        for j in range(len(stockBasics)):
            params = {'ts_code': stockBasics[j].symbol, 'trade_date': '', 'start_date': ''}
            data = query('dividend', fields, **params)
            items = []
            for i in range(len(data)):
                item = StockDividend()
                item.name = stockBasics[j].name
                item.symbol = data[i][0]
                item.code = data[i][0][0:6]
                date_time = data[i][1][0:4] + "-" + data[i][1][4:6] + "-" + data[i][1][6:8]
                item.ann_date = datetime.strptime(date_time, "%Y-%m-%d")
                item.ann_date_str = data[i][1]
                item.div_proc = data[i][2]
                item.stk_div = data[i][3]
                item.stk_bo_rate = data[i][4]
                item.stk_co_rate = data[i][5]
                item.cash_div = data[i][6]
                item.cash_div_tax = data[i][7]
                item.record_date = data[i][8]
                item.ex_date = data[i][9]
                item.pay_date = data[i][10]
                item.div_listdate = data[i][11]
                item.imp_ann_date = data[i][12]
                # 判断是否存在
                flag = StockDividend.query.filter(StockDividend.symbol == data[i][0]).first()
                if flag is not None:
                    continue
                items.append(item)
            # 添加不存在的
            if items:
                db.session.add_all(items)
                db.session.commit()
    db.session.remove()
