# coding:utf-8
import json
import datetime
from app.main.stock.models import *
from app.main import schedulers
import threading
import tushare as ts
import time
from app.main.stock import Session


pro = ts.pro_api('db4b417b6de48a4b11c7c2d3d81661bea8d0fa1bf5f4040f85688b4e')


# 股票列表
def initStock():
    fields = 'ts_code,symbol,name,area,industry,fullname,enname,exchange,curr_type,list_status,is_hs,market,list_date,delist_date'
    df = pro.query('stock_basic', list_status='L', fields=fields)
    data = json.loads(df.to_json(orient='records'))
    items = []
    session = Session()
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
        if data[i]['list_date'] is not None:
            stock.delist_date = datetime.datetime.strptime(data[i]['list_date'], '%Y%m%d')
        if data[i]['delist_date'] is not None:
            stock.list_date = datetime.datetime.strptime(data[i]['delist_date'], '%Y%m%d')
        # 判断是否存在
        flag = session.query(StockBasic).filter(StockBasic.code == data[i]['symbol']).first()
        if flag is not None:
            continue
        items.append(stock)
    # 添加不存在的
    if items:
        print(threading.currentThread().ident)
        session.add_all(items)
        session.commit()
    session.close()


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
    end_date = datetime.datetime.now().strftime('%Y%m%d')
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
    end_date = datetime.datetime.now().strftime('%Y%m%d')
    session = Session()
    stocks = session.query(StockBasic).all()
    for j in range(len(stocks)):
        # 查询最新的一天记录日期,然后根据时间去跑数据
        time.sleep(0.8)
        daily = session.query(StockDaily).filter(StockDaily.symbol == stocks[j].symbol).order_by(StockDaily.trade_date_str.desc()).first()
        if daily is not None:
            df = pro.query('daily', ts_code=stocks[j].symbol, start_date=daily.trade_date_str, end_date=end_date, fields=fields)
        else:
            df = pro.query('daily', ts_code=stocks[j].symbol, start_date='19901201', end_date=end_date, fields=fields)
        data = json.loads(df.to_json(orient='records'))
        items = []
        for i in range(len(data)):
            item = StockDaily()
            item.name = stocks[j].name
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
            flag = session.query(StockDaily).filter(StockDaily.symbol == data[i]['ts_code'], StockDaily.trade_date_str == data[i]['trade_date']).first()
            if flag is not None:
                continue
            items.append(item)
        # 添加不存在的
        if items:
            session.add_all(items)
            session.commit()
    session.close()


# 周线行情
def initStockWeekly():
    fields = 'ts_code,trade_date,open,high,low,close,pre_close,change,pct_chg,vol,amount'
    end_date = datetime.datetime.now().strftime('%Y%m%d')
    session = Session()
    stocks = session.query(StockBasic).all()
    for j in range(len(stocks)):
        # 查询最新的一天记录日期,然后根据时间去跑数据
        time.sleep(0.8)
        weekly = session.query(StockWeekly).filter(StockWeekly.symbol == stocks[j].symbol).order_by(StockWeekly.trade_date_str.desc()).first()
        if weekly is not None:
            df = pro.query('weekly', ts_code=stocks[j].symbol, start_date=weekly.trade_date_str, end_date=end_date, fields=fields)
        else:
            df = pro.query('weekly', ts_code=stocks[j].symbol, start_date='19901201', end_date=end_date, fields=fields)
        data = json.loads(df.to_json(orient='records'))
        items = []
        for i in range(len(data)):
            item = StockWeekly()
            item.name = stocks[j].name
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
            flag = session.query(StockWeekly).filter(StockWeekly.symbol == data[i]['ts_code'], StockWeekly.trade_date_str == data[i]['trade_date']).first()
            if flag is not None:
                continue
            items.append(item)
        # 添加不存在的
        if items:
            session.add_all(items)
            session.commit()
    session.close()


# 月线行情
def initStockMonthly():
    fields = 'ts_code,trade_date,open,high,low,close,pre_close,change,pct_chg,vol,amount'
    end_date = datetime.datetime.now().strftime('%Y%m%d')
    session = Session()
    stocks = session.query(StockBasic).all()
    for j in range(len(stocks)):
        # 查询最新的一天记录日期,然后根据时间去跑数据
        time.sleep(0.8)
        monthly = session.query(StockMonthly).filter(StockMonthly.symbol == stocks[j].symbol).order_by(StockMonthly.trade_date_str.desc()).first()
        if monthly is not None:
            df = pro.query('monthly', ts_code=stocks[j].symbol, start_date=monthly.trade_date_str, end_date=end_date, fields=fields)
        else:
            df = pro.query('monthly', ts_code=stocks[j].symbol, start_date='19901201', end_date=end_date, fields=fields)
        data = json.loads(df.to_json(orient='records'))
        items = []
        for i in range(len(data)):
            item = StockMonthly()
            item.name = stocks[j].name
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
            flag = session.query(StockMonthly).filter(StockMonthly.symbol == data[i]['ts_code'], StockMonthly.trade_date_str == data[i]['trade_date']).first()
            if flag is not None:
                continue
            items.append(item)
        # 添加不存在的
        if items:
            session.add_all(items)
            session.commit()
    session.close()


# 每日指标
def initDailyBasic():
    fields = 'ts_code,trade_date,close,turnover_rate,turnover_rate_f,volume_ratio,pe,pe_ttm,pb,ps,ps_ttm,total_share,float_share,free_share,total_mv,circ_mv'
    end_date = datetime.datetime.now().strftime('%Y%m%d')
    with schedulers.app.app_context():
        stocks = StockBasic.query.all()
        for j in range(len(stocks)):
            # 查询最新的一天记录日期,然后根据时间去跑数据
            basic = StockDailyBasic.query.filter(StockDailyBasic.symbol == stocks[j].symbol).order_by(StockDailyBasic.trade_date_str.desc()).first()
            if basic is not None:
                df = pro.query('daily_basic', ts_code=stocks[j].symbol, start_date=basic.trade_date_str, end_date=end_date, fields=fields)
            else:
                df = pro.query('daily_basic', ts_code=stocks[j].symbol, start_date='19901201', end_date=end_date, fields=fields)
            data = json.loads(df.to_json(orient='records'))
            items = []
            for i in range(len(data)):
                item = StockDailyBasic()
                item.name = stocks[j].name
                item.symbol = data[i]['ts_code']
                item.code = data[i]['ts_code'][0:6]
                item.trade_date = datetime.datetime.strptime(data[i]['trade_date'], '%Y%m%d')
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
    end_date = datetime.datetime.now().strftime('%Y%m%d')
    with schedulers.app.app_context():
        stocks = StockBasic.query.all()
        for j in range(len(stocks)):
            # 查询最新的一天记录日期,然后根据时间去跑数据
            time.sleep(1.5)
            income = StockIncome.query.filter(StockIncome.symbol == stocks[j].symbol).order_by(StockIncome.ann_date_str.desc()).first()
            if income is not None:
                df = pro.query('income', ts_code=stocks[j].symbol, start_date=income.ann_date_str, end_date=end_date, fields=fields)
            else:
                df = pro.query('income', ts_code=stocks[j].symbol, start_date='19901201', end_date=end_date, fields=fields)
            data = json.loads(df.to_json(orient='records'))
            items = []
            for i in range(len(data)):
                item = StockIncome()
                item.name = stocks[j].name
                item.symbol = data[i]['ts_code']
                item.code = data[i]['ts_code'][0:6]
                item.ann_date = datetime.datetime.strptime(data[i]['ann_date'], '%Y%m%d')
                item.ann_date_str = data[i]['ann_date']
                item.f_ann_date = data[i]['f_ann_date']
                item.end_date = data[i]['end_date']
                item.report_type = data[i]['report_type']
                item.comp_type = data[i]['comp_type']
                item.basic_eps = data[i]['basic_eps']
                item.diluted_eps = data[i]['diluted_eps']
                item.total_revenue = data[i]['total_revenue']
                item.revenue = data[i]['revenue']
                item.int_income = data[i]['int_income']
                item.prem_earned = data[i]['prem_earned']
                item.comm_income = data[i]['comm_income']
                item.n_commis_income = data[i]['n_commis_income']
                item.n_oth_income = data[i]['n_oth_income']
                item.n_oth_b_income = data[i]['n_oth_b_income']
                item.prem_income = data[i]['prem_income']
                item.out_prem = data[i]['out_prem']
                item.une_prem_reser = data[i]['une_prem_reser']
                item.reins_income = data[i]['reins_income']
                item.n_sec_tb_income = data[i]['n_sec_tb_income']
                item.n_sec_uw_income = data[i]['n_sec_uw_income']
                item.n_asset_mg_income = data[i]['n_asset_mg_income']
                item.oth_b_income = data[i]['oth_b_income']
                item.fv_value_chg_gain = data[i]['fv_value_chg_gain']
                item.invest_income = data[i]['invest_income']
                item.ass_invest_income = data[i]['ass_invest_income']
                item.forex_gain = data[i]['forex_gain']
                item.total_cogs = data[i]['total_cogs']
                item.oper_cost = data[i]['oper_cost']
                item.int_exp = data[i]['int_exp']
                item.comm_exp = data[i]['comm_exp']
                item.biz_tax_surchg = data[i]['biz_tax_surchg']
                item.sell_exp = data[i]['sell_exp']
                item.admin_exp = data[i]['admin_exp']
                item.fin_exp = data[i]['fin_exp']
                item.assets_impair_loss = data[i]['assets_impair_loss']
                item.prem_refund = data[i]['prem_refund']
                item.compens_payout = data[i]['compens_payout']
                item.reser_insur_liab = data[i]['reser_insur_liab']
                item.div_payt = data[i]['div_payt']
                item.reins_exp = data[i]['reins_exp']
                item.oper_exp = data[i]['oper_exp']
                item.compens_payout_refu = data[i]['compens_payout_refu']
                item.insur_reser_refu = data[i]['insur_reser_refu']
                item.reins_cost_refund = data[i]['reins_cost_refund']
                item.other_bus_cost = data[i]['other_bus_cost']
                item.operate_profit = data[i]['operate_profit']
                item.non_oper_income = data[i]['non_oper_income']
                item.non_oper_exp = data[i]['non_oper_exp']
                item.nca_disploss = data[i]['nca_disploss']
                item.total_profit = data[i]['total_profit']
                item.income_tax = data[i]['income_tax']
                item.n_income = data[i]['n_income']
                item.n_income_attr_p = data[i]['n_income_attr_p']
                item.minority_gain = data[i]['minority_gain']
                item.oth_compr_income = data[i]['oth_compr_income']
                item.t_compr_income = data[i]['t_compr_income']
                item.compr_inc_attr_p = data[i]['compr_inc_attr_p']
                item.compr_inc_attr_m_s = data[i]['compr_inc_attr_m_s']
                item.ebit = data[i]['ebit']
                item.ebitda = data[i]['ebitda']
                item.insurance_exp = data[i]['insurance_exp']
                item.undist_profit = data[i]['undist_profit']
                item.distable_profit = data[i]['distable_profit']
                # 判断是否存在
                flag = StockIncome.query.filter(StockIncome.symbol == data[i]['ts_code'], StockIncome.ann_date_str == data[i]['ann_date']).first()
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
    end_date = datetime.datetime.now().strftime('%Y%m%d')
    with schedulers.app.app_context():
        stocks = StockBasic.query.all()
        for j in range(len(stocks)):
            # 查询最新的一天记录日期,然后根据时间去跑数据
            time.sleep(1.5)
            sheet = StockBalanceSheet.query.filter(StockBalanceSheet.symbol == stocks[j].symbol).order_by(StockBalanceSheet.ann_date_str.desc()).first()
            if sheet is not None:
                df = pro.query('balancesheet', ts_code=stocks[j].symbol, start_date=sheet.ann_date_str, end_date=end_date, fields=fields)
            else:
                df = pro.query('balancesheet', ts_code=stocks[j].symbol, start_date='19901201', end_date=end_date, fields=fields)
            data = json.loads(df.to_json(orient='records'))
            items = []
            for i in range(len(data)):
                item = StockBalanceSheet()
                item.name = stocks[j].name
                item.symbol = data[i]['ts_code']
                item.code = data[i]['ts_code'][0:6]
                item.ann_date = datetime.datetime.strptime(data[i]['ann_date'], '%Y%m%d')
                item.ann_date_str = data[i]['ann_date']
                item.f_ann_date = data[i]['f_ann_date']
                item.end_date = data[i]['end_date']
                item.report_type = data[i]['report_type']
                item.comp_type = data[i]['comp_type']
                item.total_share = data[i]['total_share']
                item.cap_rese = data[i]['cap_rese']
                item.undistr_porfit = data[i]['undistr_porfit']
                item.surplus_rese = data[i]['surplus_rese']
                item.special_rese = data[i]['special_rese']
                item.money_cap = data[i]['money_cap']
                item.trad_asset = data[i]['trad_asset']
                item.notes_receiv = data[i]['notes_receiv']
                item.accounts_receiv = data[i]['accounts_receiv']
                item.oth_receiv = data[i]['oth_receiv']
                item.prepayment = data[i]['prepayment']
                item.div_receiv = data[i]['div_receiv']
                item.int_receiv = data[i]['int_receiv']
                item.inventories = data[i]['inventories']
                item.amor_exp = data[i]['amor_exp']
                item.nca_within_1y = data[i]['nca_within_1y']
                item.sett_rsrv = data[i]['sett_rsrv']
                item.loanto_oth_bank_fi = data[i]['loanto_oth_bank_fi']
                item.premium_receiv = data[i]['premium_receiv']
                item.reinsur_receiv = data[i]['reinsur_receiv']
                item.reinsur_res_receiv = data[i]['reinsur_res_receiv']
                item.pur_resale_fa = data[i]['pur_resale_fa']
                item.oth_cur_assets = data[i]['oth_cur_assets']
                item.total_cur_assets = data[i]['total_cur_assets']
                item.fa_avail_for_sale = data[i]['fa_avail_for_sale']
                item.htm_invest = data[i]['htm_invest']
                item.lt_eqt_invest = data[i]['lt_eqt_invest']
                item.invest_real_estate = data[i]['invest_real_estate']
                item.time_deposits = data[i]['time_deposits']
                item.oth_assets = data[i]['oth_assets']
                item.lt_rec = data[i]['lt_rec']
                item.fix_assets = data[i]['fix_assets']
                item.cip = data[i]['cip']
                item.const_materials = data[i]['const_materials']
                item.fixed_assets_disp = data[i]['fixed_assets_disp']
                item.produc_bio_assets = data[i]['produc_bio_assets']
                item.oil_and_gas_assets = data[i]['oil_and_gas_assets']
                item.intan_assets = data[i]['intan_assets']
                item.r_and_d = data[i]['r_and_d']
                item.goodwill = data[i]['goodwill']
                item.lt_amor_exp = data[i]['lt_amor_exp']
                item.defer_tax_assets = data[i]['defer_tax_assets']
                item.decr_in_disbur = data[i]['decr_in_disbur']
                item.oth_nca = data[i]['oth_nca']
                item.total_nca = data[i]['total_nca']
                item.cash_reser_cb = data[i]['cash_reser_cb']
                item.depos_in_oth_bfi = data[i]['depos_in_oth_bfi']
                item.prec_metals = data[i]['prec_metals']
                item.deriv_assets = data[i]['deriv_assets']
                item.rr_reins_une_prem = data[i]['rr_reins_une_prem']
                item.rr_reins_outstd_cla = data[i]['rr_reins_outstd_cla']
                item.rr_reins_lins_liab = data[i]['rr_reins_lins_liab']
                item.rr_reins_lthins_liab = data[i]['rr_reins_lthins_liab']
                item.refund_depos = data[i]['refund_depos']
                item.ph_pledge_loans = data[i]['ph_pledge_loans']
                item.refund_cap_depos = data[i]['refund_cap_depos']
                item.indep_acct_assets = data[i]['indep_acct_assets']
                item.client_depos = data[i]['client_depos']
                item.client_prov = data[i]['client_prov']
                item.transac_seat_fee = data[i]['transac_seat_fee']
                item.invest_as_receiv = data[i]['invest_as_receiv']
                item.total_assets = data[i]['total_assets']
                item.lt_borr = data[i]['lt_borr']
                item.st_borr = data[i]['st_borr']
                item.cb_borr = data[i]['cb_borr']
                item.depos_ib_deposits = data[i]['depos_ib_deposits']
                item.loan_oth_bank = data[i]['loan_oth_bank']
                item.trading_fl = data[i]['trading_fl']
                item.notes_payable = data[i]['notes_payable']
                item.acct_payable = data[i]['acct_payable']
                item.adv_receipts = data[i]['adv_receipts']
                item.sold_for_repur_fa = data[i]['sold_for_repur_fa']
                item.comm_payable = data[i]['comm_payable']
                item.payroll_payable = data[i]['payroll_payable']
                item.taxes_payable = data[i]['taxes_payable']
                item.int_payable = data[i]['int_payable']
                item.div_payable = data[i]['div_payable']
                item.oth_payable = data[i]['oth_payable']
                item.acc_exp = data[i]['acc_exp']
                item.deferred_inc = data[i]['deferred_inc']
                item.st_bonds_payable = data[i]['st_bonds_payable']
                item.payable_to_reinsurer = data[i]['payable_to_reinsurer']
                item.rsrv_insur_cont = data[i]['rsrv_insur_cont']
                item.acting_trading_sec = data[i]['acting_trading_sec']
                item.acting_uw_sec = data[i]['acting_uw_sec']
                item.non_cur_liab_due_1y = data[i]['non_cur_liab_due_1y']
                item.oth_cur_liab = data[i]['oth_cur_liab']
                item.total_cur_liab = data[i]['total_cur_liab']
                item.bond_payable = data[i]['bond_payable']
                item.lt_payable = data[i]['lt_payable']
                item.specific_payables = data[i]['specific_payables']
                item.estimated_liab = data[i]['estimated_liab']
                item.defer_tax_liab = data[i]['defer_tax_liab']
                item.defer_inc_non_cur_liab = data[i]['defer_inc_non_cur_liab']
                item.oth_ncl = data[i]['oth_ncl']
                item.total_ncl = data[i]['total_ncl']
                item.depos_oth_bfi = data[i]['depos_oth_bfi']
                item.deriv_liab = data[i]['deriv_liab']
                item.depos = data[i]['depos']
                item.agency_bus_liab = data[i]['agency_bus_liab']
                item.oth_liab = data[i]['oth_liab']
                item.prem_receiv_adva = data[i]['prem_receiv_adva']
                item.depos_received = data[i]['depos_received']
                item.ph_invest = data[i]['ph_invest']
                item.reser_une_prem = data[i]['reser_une_prem']
                item.reser_outstd_claims = data[i]['reser_outstd_claims']
                item.reser_lins_liab = data[i]['reser_lins_liab']
                item.reser_lthins_liab = data[i]['reser_lthins_liab']
                item.indept_acc_liab = data[i]['indept_acc_liab']
                item.pledge_borr = data[i]['pledge_borr']
                item.indem_payable = data[i]['indem_payable']
                item.policy_div_payable = data[i]['policy_div_payable']
                item.total_liab = data[i]['total_liab']
                item.treasury_share = data[i]['treasury_share']
                item.ordin_risk_reser = data[i]['ordin_risk_reser']
                item.forex_differ = data[i]['forex_differ']
                item.invest_loss_unconf = data[i]['invest_loss_unconf']
                item.minority_int = data[i]['minority_int']
                item.total_hldr_eqy_exc_min_int = data[i]['total_hldr_eqy_exc_min_int']
                item.total_hldr_eqy_inc_min_int = data[i]['total_hldr_eqy_inc_min_int']
                item.total_liab_hldr_eqy = data[i]['total_liab_hldr_eqy']
                item.lt_payroll_payable = data[i]['lt_payroll_payable']
                item.oth_comp_income = data[i]['oth_comp_income']
                item.oth_eqt_tools = data[i]['oth_eqt_tools']
                item.oth_eqt_tools_p_shr = data[i]['oth_eqt_tools_p_shr']
                item.lending_funds = data[i]['lending_funds']
                item.acc_receivable = data[i]['acc_receivable']
                item.st_fin_payable = data[i]['st_fin_payable']
                item.payables = data[i]['payables']
                item.hfs_assets = data[i]['hfs_assets']
                item.hfs_sales = data[i]['hfs_sales']
                # 判断是否存在
                flag = StockBalanceSheet.query.filter(StockBalanceSheet.symbol == data[i][0], StockBalanceSheet.ann_date_str == data[i]['ann_date']).first()
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
    end_date = datetime.datetime.now().strftime('%Y%m%d')
    with schedulers.app.app_context():
        stocks = StockBasic.query.all()
        for j in range(len(stocks)):
            # 查询最新的一天记录日期,然后根据时间去跑数据
            time.sleep(1.5)
            flow = StockCashFlow.query.filter(StockCashFlow.symbol == stocks[j].symbol).order_by(StockCashFlow.ann_date_str.desc()).first()
            if flow is not None:
                df = pro.query('cashflow', ts_code=stocks[j].symbol, start_date=flow.ann_date_str, end_date=end_date, fields=fields)
            else:
                df = pro.query('cashflow', ts_code=stocks[j].symbol, start_date='19901201', end_date=end_date, fields=fields)
            data = json.loads(df.to_json(orient='records'))
            items = []
            for i in range(len(data)):
                item = StockCashFlow()
                item.name = stocks[j].name
                item.symbol = data[i]['ts_code']
                item.code = data[i]['ts_code'][0:6]
                item.ann_date = datetime.datetime.strptime(data[i]['ann_date'], '%Y%m%d')
                item.ann_date_str = data[i]['ann_date']
                item.f_ann_date = data[i]['f_ann_date']
                item.end_date = data[i]['end_date']
                item.report_type = data[i]['report_type']
                item.net_profit = data[i]['net_profit']
                item.finan_exp = data[i]['finan_exp']
                item.c_fr_sale_sg = data[i]['c_fr_sale_sg']
                item.recp_tax_rends = data[i]['recp_tax_rends']
                item.n_depos_incr_fi = data[i]['n_depos_incr_fi']
                item.n_incr_loans_cb = data[i]['n_incr_loans_cb']
                item.n_inc_borr_oth_fi = data[i]['n_inc_borr_oth_fi']
                item.prem_fr_orig_contr = data[i]['prem_fr_orig_contr']
                item.n_incr_insured_dep = data[i]['n_incr_insured_dep']
                item.n_reinsur_prem = data[i]['n_reinsur_prem']
                item.n_incr_disp_tfa = data[i]['n_incr_disp_tfa']
                item.ifc_cash_incr = data[i]['ifc_cash_incr']
                item.n_incr_disp_faas = data[i]['n_incr_disp_faas']
                item.n_incr_loans_oth_bank = data[i]['n_incr_loans_oth_bank']
                item.n_cap_incr_repur = data[i]['n_cap_incr_repur']
                item.c_fr_oth_operate_a = data[i]['c_fr_oth_operate_a']
                item.c_inf_fr_operate_a = data[i]['c_inf_fr_operate_a']
                item.c_paid_goods_s = data[i]['c_paid_goods_s']
                item.c_paid_to_for_empl = data[i]['c_paid_to_for_empl']
                item.c_paid_for_taxes = data[i]['c_paid_for_taxes']
                item.n_incr_clt_loan_adv = data[i]['n_incr_clt_loan_adv']
                item.n_incr_dep_cbob = data[i]['n_incr_dep_cbob']
                item.c_pay_claims_orig_inco = data[i]['c_pay_claims_orig_inco']
                item.pay_handling_chrg = data[i]['pay_handling_chrg']
                item.pay_comm_insur_plcy = data[i]['pay_comm_insur_plcy']
                item.oth_cash_pay_oper_act = data[i]['oth_cash_pay_oper_act']
                item.st_cash_out_act = data[i]['st_cash_out_act']
                item.n_cashflow_act = data[i]['n_cashflow_act']
                item.oth_recp_ral_inv_act = data[i]['oth_recp_ral_inv_act']
                item.c_disp_withdrwl_invest = data[i]['c_disp_withdrwl_invest']
                item.c_recp_return_invest = data[i]['c_recp_return_invest']
                item.n_recp_disp_fiolta = data[i]['n_recp_disp_fiolta']
                item.n_recp_disp_sobu = data[i]['n_recp_disp_sobu']
                item.stot_inflows_inv_act = data[i]['stot_inflows_inv_act']
                item.c_pay_acq_const_fiolta = data[i]['c_pay_acq_const_fiolta']
                item.c_paid_invest = data[i]['c_paid_invest']
                item.n_disp_subs_oth_biz = data[i]['n_disp_subs_oth_biz']
                item.oth_pay_ral_inv_act = data[i]['oth_pay_ral_inv_act']
                item.n_incr_pledge_loan = data[i]['stot_out_inv_act']
                item.stot_out_inv_act = data[i]['stot_out_inv_act']
                item.n_cashflow_inv_act = data[i]['n_cashflow_inv_act']
                item.c_recp_borrow = data[i]['c_recp_borrow']
                item.proc_issue_bonds = data[i]['proc_issue_bonds']
                item.oth_cash_recp_ral_fnc_act = data[i]['oth_cash_recp_ral_fnc_act']
                item.stot_cash_in_fnc_act = data[i]['stot_cash_in_fnc_act']
                item.free_cashflow = data[i]['free_cashflow']
                item.c_prepay_amt_borr = data[i]['c_prepay_amt_borr']
                item.c_pay_dist_dpcp_int_exp = data[i]['c_pay_dist_dpcp_int_exp']
                item.incl_dvd_profit_paid_sc_ms = data[i]['incl_dvd_profit_paid_sc_ms']
                item.oth_cashpay_ral_fnc_act = data[i]['oth_cashpay_ral_fnc_act']
                item.stot_cashout_fnc_act = data[i]['stot_cashout_fnc_act']
                item.n_cash_flows_fnc_act = data[i]['n_cash_flows_fnc_act']
                item.eff_fx_flu_cash = data[i]['eff_fx_flu_cash']
                item.n_incr_cash_cash_equ = data[i]['n_incr_cash_cash_equ']
                item.c_cash_equ_beg_period = data[i]['c_cash_equ_beg_period']
                item.c_cash_equ_end_period = data[i]['c_cash_equ_end_period']
                item.c_recp_cap_contrib = data[i]['c_recp_cap_contrib']
                item.incl_cash_rec_saims = data[i]['incl_cash_rec_saims']
                item.uncon_invest_loss = data[i]['uncon_invest_loss']
                item.prov_depr_assets = data[i]['prov_depr_assets']
                item.depr_fa_coga_dpba = data[i]['depr_fa_coga_dpba']
                item.amort_intang_assets = data[i]['amort_intang_assets']
                item.lt_amort_deferred_exp = data[i]['lt_amort_deferred_exp']
                item.decr_deferred_exp = data[i]['decr_deferred_exp']
                item.incr_acc_exp = data[i]['incr_acc_exp']
                item.loss_disp_fiolta = data[i]['loss_disp_fiolta']
                item.loss_scr_fa = data[i]['loss_scr_fa']
                item.loss_fv_chg = data[i]['loss_fv_chg']
                item.invest_loss = data[i]['invest_loss']
                item.decr_def_inc_tax_assets = data[i]['decr_def_inc_tax_assets']
                item.incr_def_inc_tax_liab = data[i]['incr_def_inc_tax_liab']
                item.decr_inventories = data[i]['decr_inventories']
                item.decr_oper_payable = data[i]['decr_oper_payable']
                item.incr_oper_payable = data[i]['incr_oper_payable']
                item.others = data[i]['others']
                item.im_net_cashflow_oper_act = data[i]['im_net_cashflow_oper_act']
                item.conv_debt_into_cap = data[i]['conv_debt_into_cap']
                item.conv_copbonds_due_within_1y = data[i]['conv_copbonds_due_within_1y']
                item.fa_fnc_leases = data[i]['fa_fnc_leases']
                item.end_bal_cash = data[i]['end_bal_cash']
                item.beg_bal_cash = data[i]['beg_bal_cash']
                item.end_bal_cash_equ = data[i]['end_bal_cash_equ']
                item.beg_bal_cash_equ = data[i]['im_n_incr_cash_equ']
                item.im_n_incr_cash_equ = data[i]['im_n_incr_cash_equ']
                # 判断是否存在
                flag = StockCashFlow.query.filter(StockCashFlow.symbol == data[i]['ts_code'], StockCashFlow.ann_date_str == data[i]['ann_date']).first()
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
    end_date = datetime.datetime.now().strftime('%Y%m%d')
    with schedulers.app.app_context():
        stocks = StockBasic.query.all()
        for j in range(len(stocks)):
            # 查询最新的一天记录日期,然后根据时间去跑数据
            # 睡眠一秒,因为接口调用有次数限制
            time.sleep(1)
            cast = StockForeCast.query.filter(StockForeCast.symbol == stocks[j].symbol).order_by(StockForeCast.ann_date_str.desc()).first()
            if cast is not None:
                df = pro.query('forecast', ts_code=stocks[j].symbol, start_date=cast.ann_date_str, end_date=end_date, fields=fields)
            else:
                df = pro.query('forecast', ts_code=stocks[j].symbol, start_date='19901201', end_date=end_date, fields=fields)
            data = json.loads(df.to_json(orient='records'))
            items = []
            for i in range(len(data)):
                item = StockForeCast()
                item.name = stocks[j].name
                item.symbol = data[i]['ts_code']
                item.code = data[i]['ts_code'][0:6]
                item.ann_date = datetime.datetime.strptime(data[i]['ann_date'], '%Y%m%d')
                item.ann_date_str = data[i]['ann_date']
                item.end_date = data[i]['end_date']
                item.type = data[i]['type']
                item.p_change_min = data[i]['p_change_min']
                item.p_change_max = data[i]['p_change_max']
                item.net_profit_min = data[i]['net_profit_min']
                item.net_profit_max = data[i]['net_profit_max']
                item.last_parent_net = data[i]['last_parent_net']
                item.first_ann_date = data[i]['first_ann_date']
                item.summary = data[i]['summary']
                item.change_reason = data[i]['change_reason']
                # 判断是否存在
                flag = StockForeCast.query.filter(StockForeCast.symbol == data[i]['ts_code'], StockForeCast.ann_date_str == data[i]['ann_date']).first()
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
    fields = 'ts_code,ann_date,end_date,revenue,operate_profit,operate_profit,total_profit,n_income,total_assets,total_hldr_eqy_exc_min_int,diluted_eps,diluted_roe,' \
             'yoy_net_profit,bps,yoy_sales,yoy_op,yoy_tp,yoy_dedu_np,yoy_eps,yoy_roe,growth_assets,yoy_equity,growth_bps,or_last_year,op_last_year,tp_last_year,np_last_year,' \
             'eps_last_year,open_net_assets,open_bps,perf_summary,is_audit,remark'
    end_date = datetime.datetime.now().strftime('%Y%m%d')
    with schedulers.app.app_context():
        stocks = StockBasic.query.all()
        for j in range(len(stocks)):
            # 查询最新的一天记录日期,然后根据时间去跑数据
            # 睡眠一秒,因为接口调用有次数限制
            time.sleep(1.5)
            express = StockExpress.query.filter(StockExpress.symbol == stocks[j].symbol).order_by(StockExpress.ann_date_str.desc()).first()
            if express is not None:
                df = pro.query('express', ts_code=stocks[j].symbol, start_date=express.ann_date_str, end_date=end_date, fields=fields)
            else:
                df = pro.query('express', ts_code=stocks[j].symbol, start_date='19901201', end_date=end_date, fields=fields)
            data = json.loads(df.to_json(orient='records'))
            items = []
            for i in range(len(data)):
                item = StockExpress()
                item.name = stocks[j].name
                item.symbol = data[i]['ts_code']
                item.code = data[i]['ts_code'][0:6]
                item.ann_date = datetime.datetime.strptime(data[i]['ann_date'], '%Y%m%d')
                item.ann_date_str = data[i]['ann_date']
                item.revenue = data[i]['revenue']
                item.operate_profit = data[i]['operate_profit']
                item.total_profit = data[i]['total_profit']
                item.n_income = data[i]['n_income']
                item.total_assets = data[i]['total_assets']
                item.total_hldr_eqy_exc_min_int = data[i]['total_hldr_eqy_exc_min_int']
                item.diluted_eps = data[i]['diluted_eps']
                item.diluted_roe = data[i]['diluted_roe']
                item.yoy_net_profit = data[i]['yoy_net_profit']
                item.bps = data[i]['bps']
                item.yoy_sales = data[i]['yoy_sales']
                item.yoy_op = data[i]['yoy_op']
                item.yoy_tp = data[i]['yoy_tp']
                item.yoy_dedu_np = data[i]['yoy_dedu_np']
                item.yoy_eps = data[i]['yoy_eps']
                item.yoy_roe = data[i]['yoy_roe']
                item.growth_assets = data[i]['growth_assets']
                item.yoy_equity = data[i]['yoy_equity']
                item.growth_bps = data[i]['growth_bps']
                item.or_last_year = data[i]['or_last_year']
                item.op_last_year = data[i]['op_last_year']
                item.tp_last_year = data[i]['tp_last_year']
                item.np_last_year = data[i]['np_last_year']
                item.eps_last_year = data[i]['eps_last_year']
                item.open_net_assets = data[i]['open_net_assets']
                item.open_bps = data[i]['open_bps']
                item.perf_summary = data[i]['perf_summary']
                item.is_audit = data[i]['is_audit']
                item.remark = data[i]['remark']
                # 判断是否存在
                flag = StockExpress.query.filter(StockExpress.symbol == data[i]['ts_code'], StockExpress.ann_date_str == data[i]['ann_date']).first()
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
    fields = 'ts_code,ts_code,ann_date,div_proc,stk_div,stk_bo_rate,stk_co_rate,cash_div,cash_div_tax,record_date,ex_date,pay_date,div_listdate,' \
             'imp_ann_date,base_date,base_share'
    end_date = datetime.datetime.now().strftime('%Y%m%d')
    with schedulers.app.app_context():
        stocks = StockBasic.query.all()
        for j in range(len(stocks)):
            # 查询最新的一天记录日期,然后根据时间去跑数据
            # 睡眠一秒,因为接口调用有次数限制
            time.sleep(1)
            express = StockDividend.query.filter(StockDividend.symbol == stocks[j].symbol).order_by(StockDividend.ann_date_str.desc()).first()
            if express is not None:
                df = pro.query('dividend', ts_code=stocks[j].symbol, start_date=express.ann_date_str, end_date=end_date, fields=fields)
            else:
                df = pro.query('dividend', ts_code=stocks[j].symbol, start_date='19901201', end_date=end_date, fields=fields)
            data = json.loads(df.to_json(orient='records'))
            items = []
            for i in range(len(data)):
                item = StockDividend()
                item.name = stocks[j].name
                item.symbol = data[i]['ts_code']
                item.code = data[i]['ts_code'][0:6]
                if data[i]['ann_date'] is not None:
                    item.ann_date = datetime.datetime.strptime(data[i]['ann_date'], '%Y%m%d')
                item.ann_date_str = data[i]['ann_date']
                item.div_proc = data[i]['div_proc']
                item.stk_div = data[i]['stk_div']
                item.stk_bo_rate = data[i]['stk_bo_rate']
                item.stk_co_rate = data[i]['stk_co_rate']
                item.cash_div = data[i]['cash_div']
                item.cash_div_tax = data[i]['cash_div_tax']
                item.record_date = data[i]['record_date']
                item.ex_date = data[i]['ex_date']
                item.pay_date = data[i]['pay_date']
                item.div_listdate = data[i]['div_listdate']
                item.imp_ann_date = data[i]['imp_ann_date']
                item.base_date = data[i]['base_date']
                item.base_share = data[i]['base_share']
                # 判断是否存在
                flag = StockDividend.query.filter(StockDividend.symbol == data[i]['ts_code'], StockDividend.ann_date_str == data[i]['ann_date']).first()
                if flag is not None:
                    continue
                items.append(item)
            # 添加不存在的
            if items:
                db.session.add_all(items)
                db.session.commit()
    db.session.remove()


# 财务审计意见
def initStockFinaAudit():
    fields = 'ts_code,ann_date,end_date,audit_result,audit_fees,audit_agency,audit_sign'
    end_date = datetime.datetime.now().strftime('%Y%m%d')
    with schedulers.app.app_context():
        stocks = StockBasic.query.all()
        for j in range(len(stocks)):
            # 查询最新的一天记录日期,然后根据时间去跑数据
            # 睡眠一秒,因为接口调用有次数限制
            time.sleep(2)
            express = StockFinaAudit.query.filter(StockFinaAudit.symbol == stocks[j].symbol).order_by(StockFinaAudit.ann_date_str.desc()).first()
            if express is not None:
                df = pro.query('fina_audit', ts_code=stocks[j].symbol, start_date=express.ann_date_str, end_date=end_date, fields=fields)
            else:
                df = pro.query('fina_audit', ts_code=stocks[j].symbol, start_date='19901201', end_date=end_date, fields=fields)
            data = json.loads(df.to_json(orient='records'))
            items = []
            for i in range(len(data)):
                item = StockFinaAudit()
                item.name = stocks[j].name
                item.symbol = data[i]['ts_code']
                item.code = data[i]['ts_code'][0:6]
                item.ann_date = datetime.datetime.strptime(data[i]['ann_date'], '%Y%m%d')
                item.ann_date_str = data[i]['ann_date']
                item.end_date = data[i]['end_date']
                item.audit_result = data[i]['audit_result']
                item.audit_fees = data[i]['audit_fees']
                item.audit_agency = data[i]['audit_agency']
                item.audit_sign = data[i]['audit_sign']
                # 判断是否存在
                flag = StockFinaAudit.query.filter(StockFinaAudit.symbol == data[i]['ts_code'], StockFinaAudit.ann_date_str == data[i]['ann_date']).first()
                if flag is not None:
                    continue
                items.append(item)
            # 添加不存在的
            if items:
                db.session.add_all(items)
                db.session.commit()
    db.session.remove()


# 主营业务构成
def initStockFinaMainbz():
    fields = 'ts_code,end_date,bz_item,bz_sales,bz_profit,bz_cost,curr_type,update_flag'
    end_date = datetime.datetime.now().strftime('%Y%m%d')
    with schedulers.app.app_context():
        stocks = StockBasic.query.all()
        for j in range(len(stocks)):
            # 查询最新的一天记录日期,然后根据时间去跑数据
            # 睡眠一秒,因为接口调用有次数限制
            time.sleep(1.5)
            express = StockFinaMainbz.query.filter(StockFinaMainbz.symbol == stocks[j].symbol).order_by(StockFinaMainbz.end_date_str.desc()).first()
            if express is not None:
                df = pro.query('fina_mainbz', ts_code=stocks[j].symbol, start_date=express.end_date_str, end_date=end_date, fields=fields)
            else:
                df = pro.query('fina_mainbz', ts_code=stocks[j].symbol, start_date='19901201', end_date=end_date, fields=fields)
            data = json.loads(df.to_json(orient='records'))
            items = []
            for i in range(len(data)):
                item = StockFinaMainbz()
                item.name = stocks[j].name
                item.symbol = data[i]['ts_code']
                item.code = data[i]['ts_code'][0:6]
                item.end_date = datetime.datetime.strptime(data[i]['end_date'], '%Y%m%d')
                item.end_date_str = data[i]['end_date']
                item.bz_item = data[i]['bz_item']
                item.bz_sales = data[i]['bz_sales']
                item.bz_profit = data[i]['bz_profit']
                item.bz_cost = data[i]['bz_cost']
                item.bz_cost = data[i]['bz_cost']
                item.update_flag = data[i]['update_flag']
                # 判断是否存在
                flag = StockFinaMainbz.query.filter(StockFinaMainbz.symbol == data[i]['ts_code'], StockFinaMainbz.end_date_str == data[i]['end_date']).first()
                if flag is not None:
                    continue
                items.append(item)
            # 添加不存在的
            if items:
                db.session.add_all(items)
                db.session.commit()
    db.session.remove()
