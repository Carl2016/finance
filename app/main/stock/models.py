# coding:utf-8
from app.main import db
from sqlalchemy.sql import func


# 股票列表
class StockBasic(db.Model):
    __tablename__ = 'stock_basic'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(20), index=True, comment=u"股票代码")
    name = db.Column(db.String(30), index=True, comment=u"股票名称")
    industry = db.Column(db.String(30), comment=u"所属行业")
    area = db.Column(db.String(30), comment=u"地区")
    fullname = db.Column(db.String(50), comment=u"股票全称")
    enname = db.Column(db.String(200), comment=u"英文全称")
    market = db.Column(db.String(30), comment=u"市场类型 （主板/中小板/创业板）")
    exchange = db.Column(db.String(30), comment=u"交易所代码")
    curr_type = db.Column(db.String(30), comment=u"交易货币")
    list_status = db.Column(db.String(30), comment=u"上市状态： L上市 D退市 P暂停上市")
    list_date = db.Column(db.Date, comment=u"上市日期")
    delist_date = db.Column(db.Date, comment=u"退市日期")
    is_hs = db.Column(db.String(30), comment=u"是否沪深港通标的，N否 H沪股通 S深股通")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def save(self):
        db.session.add(self)
        db.session.commit()


# 股票上市公司基本信息
class StockCompany(db.Model):
    __tablename__ = 'stock_company'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    exchange = db.Column(db.String(50), comment=u"交易所代码 ，SSE上交所 SZSE深交所")
    chairman = db.Column(db.String(50), comment=u"法人代表")
    manager = db.Column(db.String(50), comment=u"总经理")
    secretary = db.Column(db.String(50), comment=u"董秘")
    reg_capital = db.Column(db.DECIMAL(20, 4), comment=u"注册资本")
    setup_date = db.Column(db.String(30), comment=u"注册日期")
    province = db.Column(db.String(30), comment=u"所在省份")
    city = db.Column(db.String(30), comment=u"所在城市")
    introduction = db.Column(db.String(1000), comment=u"公司介绍")
    website = db.Column(db.String(1000), comment=u"公司主页")
    email = db.Column(db.String(200), comment=u"电子邮件")
    office = db.Column(db.String(200), comment=u"办公室")
    employees = db.Column(db.Integer(), comment=u"员工人数")
    main_business = db.Column(db.String(1000), comment=u"主要业务及产品")
    business_scope = db.Column(db.String(2500), comment=u"经营范围")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockCompany %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 股票IPO新股列表
class StockNewShare(db.Model):
    __tablename__ = 'stock_new_share'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    sub_code = db.Column(db.String(30), comment=u"申购代码")
    ipo_date = db.Column(db.String(50), comment=u"上网发行日期")
    issue_date = db.Column(db.String(50), comment=u"上市日期")
    amount = db.Column(db.DECIMAL(20, 4), comment=u"发行总量（万股）")
    market_amount = db.Column(db.DECIMAL(20, 4), comment=u"发行价格")
    price = db.Column(db.DECIMAL(20, 4), comment=u"发行价格")
    pe = db.Column(db.DECIMAL(20, 4), comment=u"市盈率")
    limit_amount = db.Column(db.DECIMAL(20, 4), comment=u"个人申购上限（万股）")
    funds = db.Column(db.DECIMAL(20, 4), comment=u"募集资金（亿元）")
    ballot = db.Column(db.DECIMAL(20, 4), comment=u"中签率")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockCompany %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 股票日线行情
class StockDaily(db.Model):
    __tablename__ = 'stock_daily'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    trade_date_str = db.Column(db.String(50), comment=u"交易日期")
    trade_date = db.Column(db.Date, index=True, comment=u"交易日期")
    open = db.Column(db.DECIMAL(20, 4), comment=u"开盘价")
    high = db.Column(db.DECIMAL(20, 4), comment=u"最高价")
    low = db.Column(db.DECIMAL(20, 4), comment=u"最低价")
    close = db.Column(db.DECIMAL(20, 4), comment=u"收盘价")
    pre_close = db.Column(db.DECIMAL(20, 4), comment=u"昨收价")
    change = db.Column(db.String(50), comment=u"涨跌额")
    pct_chg = db.Column(db.DECIMAL(20, 4), comment=u"涨跌幅 （未复权，如果是复权请用 通用行情接口 ）")
    vol = db.Column(db.DECIMAL(20, 4), comment=u"成交量 （手）")
    amount = db.Column(db.DECIMAL(20, 4), comment=u"成交额 （千元）")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockDaily %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 股票周线行情
class StockWeekly(db.Model):
    __tablename__ = 'stock_weekly'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    trade_date_str = db.Column(db.String(50), comment=u"交易日期")
    trade_date = db.Column(db.Date, index=True, comment=u"交易日期")
    open = db.Column(db.DECIMAL(20, 4), comment=u"周开盘价")
    high = db.Column(db.DECIMAL(20, 4), comment=u"周最高价")
    low = db.Column(db.DECIMAL(20, 4), comment=u"周最低价")
    close = db.Column(db.DECIMAL(20, 4), comment=u"周收盘价")
    pre_close = db.Column(db.DECIMAL(20, 4), comment=u"上一周收盘价")
    change = db.Column(db.String(50), comment=u"周涨跌额")
    pct_chg = db.Column(db.DECIMAL(20, 4), comment=u"周涨跌幅 （未复权，如果是复权请用 通用行情接口 ）")
    vol = db.Column(db.DECIMAL(20, 4), comment=u"周成交量 （手）")
    amount = db.Column(db.DECIMAL(20, 4), comment=u"周成交额 （千元）")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockWeekly %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 股票月线行情
class StockMonthly(db.Model):
    __tablename__ = 'stock_monthly'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    trade_date_str = db.Column(db.String(50), comment=u"交易日期")
    trade_date = db.Column(db.Date, index=True, comment=u"交易日期")
    open = db.Column(db.DECIMAL(20, 4), comment=u"月开盘价")
    high = db.Column(db.DECIMAL(20, 4), comment=u"月最高价")
    low = db.Column(db.DECIMAL(20, 4), comment=u"月最低价")
    close = db.Column(db.DECIMAL(20, 4), comment=u"月收盘价")
    pre_close = db.Column(db.DECIMAL(20, 4), comment=u"上月收盘价")
    change = db.Column(db.String(50), comment=u"月涨跌额")
    pct_chg = db.Column(db.DECIMAL(20, 4), comment=u"月涨跌幅 （未复权，如果是复权请用 通用行情接口 ）")
    vol = db.Column(db.DECIMAL(20, 4), comment=u"月成交量 （手）")
    amount = db.Column(db.DECIMAL(20, 4), comment=u"月成交额 （千元）")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockMonthly %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 股票A股复权行情
class StockProBar(db.Model):
    __tablename__ = 'stock_pro_bar'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    start_date = db.Column(db.String(50), comment=u"开始日期 (格式：YYYYMMDD)")
    end_date = db.Column(db.String(50), comment=u"结束日期 (格式：YYYYMMDD)")
    asset = db.Column(db.String(50), comment=u"资产类别：E股票 I沪深指数 C数字货币 F期货 FD基金 O期权，默认E")
    adj = db.Column(db.String(50), comment=u"复权类型(只针对股票)：None未复权 qfq前复权 hfq后复权 , 默认None")
    freq = db.Column(db.String(50), comment=u"数据频度 ：1MIN表示1分钟（1/5/15/30/60分钟） D日线 ，默认D")
    ma = db.Column(db.DECIMAL(20, 4), comment=u"均线，支持任意周期的均价和均量，输入任意合理int数值")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockProBar %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 股票复权因子
class StockAdjFactor(db.Model):
    __tablename__ = 'stock_adj_factor'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    trade_date = db.Column(db.String(50), comment=u"交易日期")
    adj_factor = db.Column(db.DECIMAL(20, 4), comment=u"复权因子")
    start_date = db.Column(db.String(50), comment=u"开始日期")
    end_date = db.Column(db.String(50), comment=u"结束日期")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockAdjFactor %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 个股资金流向
class StockMoneyflow(db.Model):
    __tablename__ = 'stock_money_flow'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    trade_date = db.Column(db.Date, comment=u"交易日期")
    trade_date_str = db.Column(db.String(50), comment=u"交易日期")
    buy_sm_vol = db.Column(db.DECIMAL(20, 4), comment=u"小单买入量（手）")
    buy_sm_amount = db.Column(db.DECIMAL(20, 4), comment=u"小单买入金额（万元）")
    sell_sm_vol = db.Column(db.DECIMAL(20, 4), comment=u"小单卖出量（手）")
    sell_sm_amount = db.Column(db.DECIMAL(20, 4), comment=u"小单卖出金额（万元）")
    buy_md_vol = db.Column(db.DECIMAL(20, 4), comment=u"中单买入量（手）")
    buy_md_amount = db.Column(db.DECIMAL(20, 4), comment=u"中单买入金额（万元）")
    sell_md_vol = db.Column(db.DECIMAL(20, 4), comment=u"市净率（中单卖出量（手）")
    sell_md_amount = db.Column(db.DECIMAL(20, 4), comment=u"中单卖出金额（万元）")
    buy_lg_vol = db.Column(db.DECIMAL(20, 4), comment=u"大单买入量（手）")
    buy_lg_amount = db.Column(db.DECIMAL(20, 4), comment=u"大单买入金额（万元）")
    sell_lg_vol = db.Column(db.DECIMAL(20, 4), comment=u"大单卖出量（手）")
    sell_lg_amount = db.Column(db.DECIMAL(20, 4), comment=u"大单卖出金额（万元）")
    buy_elg_vol = db.Column(db.DECIMAL(20, 4), comment=u"特大单买入量（手）")
    buy_elg_amount = db.Column(db.DECIMAL(20, 4), comment=u"特大单买入金额（万元）")
    sell_elg_vol = db.Column(db.DECIMAL(20, 4), comment=u"特大单卖出量（手）")
    sell_elg_amount = db.Column(db.DECIMAL(20, 4), comment=u"特大单卖出金额（万元）")
    net_mf_vol = db.Column(db.DECIMAL(20, 4), comment=u"净流入量（手）")
    net_mf_amount = db.Column(db.DECIMAL(20, 4), comment=u"净流入额（万元）")

    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockMoneyflow %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 指数基本信息
class StockIndexBasic(db.Model):
    __tablename__ = 'stock_index_basic'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    index_code = db.Column(db.String(30), index=True, comment=u"指数代码")
    index_name = db.Column(db.String(50), comment=u"指数名称")
    exp_date = db.Column(db.Date, comment=u"终止日期")
    exp_date_str = db.Column(db.String(50), comment=u"终止日期")
    c_name = db.Column(db.String(100), comment=u"简称")
    fullname = db.Column(db.String(100), comment=u"指数全称")
    market = db.Column(db.String(100), comment=u"市场")
    publisher = db.Column(db.String(100), comment=u"发布方")
    index_type = db.Column(db.String(100), comment=u"指数风格")
    category = db.Column(db.String(100), comment=u"指数类别")
    base_date = db.Column(db.String(100), comment=u"基期")
    base_point = db.Column(db.DECIMAL(20, 4), comment=u"基点")
    list_date = db.Column(db.String(50), comment=u"发布日期")
    weight_rule = db.Column(db.String(100), comment=u"加权方式")
    desc = db.Column(db.String(200), comment=u"描述")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockIndexBasic %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 指数日线行情
class StockIndexDaily(db.Model):
    __tablename__ = 'stock_index_daily'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    index_code = db.Column(db.String(30), index=True, comment=u"指数代码")
    index_name = db.Column(db.String(50), comment=u"指数名称")
    trade_date = db.Column(db.DATE, index=True, comment=u"交易日期")
    trade_date_str = db.Column(db.String(50), comment=u"交易日期")
    close = db.Column(db.DECIMAL(20, 4), comment=u"收盘点位")
    open = db.Column(db.DECIMAL(20, 4), comment=u"开盘点位")
    high = db.Column(db.DECIMAL(20, 4), comment=u"最高点位")
    low = db.Column(db.DECIMAL(20, 4), comment=u"最低点位")
    pre_close = db.Column(db.DECIMAL(20, 4), comment=u"昨日收盘点")
    change = db.Column(db.DECIMAL(20, 4), comment=u"涨跌点")
    pct_chg = db.Column(db.DECIMAL(20, 4), comment=u"涨跌幅（%）")
    vol = db.Column(db.DECIMAL(20, 4), comment=u"成交量（手）")
    amount = db.Column(db.DECIMAL(20, 4), comment=u"成交额（千元）")

    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockIndexDaily %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 指数周线行情
class StockIndexWeekly(db.Model):
    __tablename__ = 'stock_index_weekly'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    index_code = db.Column(db.String(30), index=True, comment=u"指数代码")
    index_name = db.Column(db.String(50), comment=u"指数名称")
    trade_date = db.Column(db.DATE, index=True, comment=u"交易日期")
    trade_date_str = db.Column(db.String(50), comment=u"交易日期")
    close = db.Column(db.DECIMAL(20, 4), comment=u"收盘点位")
    open = db.Column(db.DECIMAL(20, 4), comment=u"开盘点位")
    high = db.Column(db.DECIMAL(20, 4), comment=u"最高点位")
    low = db.Column(db.DECIMAL(20, 4), comment=u"最低点位")
    pre_close = db.Column(db.DECIMAL(20, 4), comment=u"昨日收盘点")
    change = db.Column(db.DECIMAL(20, 4), comment=u"涨跌点")
    pct_chg = db.Column(db.DECIMAL(20, 4), comment=u"涨跌幅（%）")
    vol = db.Column(db.DECIMAL(20, 4), comment=u"成交量（手）")
    amount = db.Column(db.DECIMAL(20, 4), comment=u"成交额（千元）")

    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockIndexWeekly %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 指数月线行情
class StockIndexMonthly(db.Model):
    __tablename__ = 'stock_index_monthly'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    index_code = db.Column(db.String(30), index=True, comment=u"指数代码")
    index_name = db.Column(db.String(50), comment=u"指数名称")
    trade_date = db.Column(db.DATE, index=True, comment=u"交易日期")
    trade_date_str = db.Column(db.String(50), comment=u"交易日期")
    close = db.Column(db.DECIMAL(20, 4), comment=u"收盘点位")
    open = db.Column(db.DECIMAL(20, 4), comment=u"开盘点位")
    high = db.Column(db.DECIMAL(20, 4), comment=u"最高点位")
    low = db.Column(db.DECIMAL(20, 4), comment=u"最低点位")
    pre_close = db.Column(db.DECIMAL(20, 4), comment=u"昨日收盘点")
    change = db.Column(db.DECIMAL(20, 4), comment=u"涨跌点")
    pct_chg = db.Column(db.DECIMAL(20, 4), comment=u"涨跌幅（%）")
    vol = db.Column(db.DECIMAL(20, 4), comment=u"成交量（手）")
    amount = db.Column(db.DECIMAL(20, 4), comment=u"成交额（千元）")

    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockIndexMonthly %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 指数成分和权重
class StockIndexWeight(db.Model):
    __tablename__ = 'stock_index_weight'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    index_code = db.Column(db.String(50), comment=u"指数代码")
    trade_date = db.Column(db.DATE, index=True, comment=u"交易日期")
    trade_date_str = db.Column(db.String(50), comment=u"交易日期")
    weight = db.Column(db.DECIMAL(20, 4), comment=u"权重")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockIndexWeight %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 大盘指数每日指标
class StockIndexDailyBasic(db.Model):
    __tablename__ = 'stock_index_daily_basic'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    index_code = db.Column(db.String(50), comment=u"指数代码")
    trade_date = db.Column(db.DATE, index=True, comment=u"交易日期")
    trade_date_str = db.Column(db.String(50), comment=u"交易日期")
    total_mv = db.Column(db.DECIMAL(20, 4), comment=u"当日总市值（元）")
    float_mv = db.Column(db.DECIMAL(20, 4), comment=u"当日流通市值（元）")
    total_share = db.Column(db.DECIMAL(20, 4), comment=u"当日总股本（股）")
    float_share = db.Column(db.DECIMAL(20, 4), comment=u"当日流通股本（股）")
    free_share = db.Column(db.DECIMAL(20, 4), comment=u"当日自由流通股本（股）")
    turnover_rate = db.Column(db.DECIMAL(20, 4), comment=u"换手率")
    turnover_rate_f = db.Column(db.DECIMAL(20, 4), comment=u"换手率(基于自由流通股本)")
    pe = db.Column(db.DECIMAL(20, 4), comment=u"市盈率")
    pe_ttm = db.Column(db.DECIMAL(20, 4), comment=u"市盈率TTM")
    pb = db.Column(db.DECIMAL(20, 4), comment=u"市净率")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockIndexWeight %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 股票每日指标
class StockDailyBasic(db.Model):
    __tablename__ = 'stock_daily_basic'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    trade_date = db.Column(db.Date, comment=u"交易日期")
    trade_date_str = db.Column(db.String(50), comment=u"交易日期")
    close = db.Column(db.DECIMAL(20, 4), comment=u"当日收盘价")
    turnover_rate = db.Column(db.DECIMAL(20, 4), comment=u"换手率")
    turnover_rate_f = db.Column(db.DECIMAL(20, 4), comment=u"换手率（自由流通股）")
    volume_ratio = db.Column(db.DECIMAL(20, 4), comment=u"量比")
    pe = db.Column(db.DECIMAL(20, 4), comment=u"市盈率（总市值/净利润）")
    pe_ttm = db.Column(db.DECIMAL(20, 4), comment=u"市盈率（TTM）")
    pb = db.Column(db.DECIMAL(20, 4), comment=u"市净率（总市值/净资产）")
    ps = db.Column(db.DECIMAL(20, 4), comment=u"市销率")
    ps_ttm = db.Column(db.DECIMAL(20, 4), comment=u"市销率（TTM）")
    total_share = db.Column(db.DECIMAL(20, 4), comment=u"总股本 （万）")
    float_share = db.Column(db.DECIMAL(20, 4), comment=u"流通股本 （万）")
    free_share = db.Column(db.DECIMAL(20, 4), comment=u"自由流通股本 （万）")
    total_mv = db.Column(db.DECIMAL(20, 4), comment=u"总市值 （万元）")
    circ_mv = db.Column(db.DECIMAL(20, 4), comment=u"流通市值（万元）")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockAdjFactor %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 股票停复牌信息
class StockSuspend(db.Model):
    __tablename__ = 'stock_suspend'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    suspend_date = db.Column(db.String(50), comment=u"停牌日期")
    resume_date = db.Column(db.String(50), comment=u"复牌日期")
    ann_date = db.Column(db.String(50), comment=u"公告日期")
    suspend_reason = db.Column(db.String(50), comment=u"停牌原因")
    reason_type = db.Column(db.String(50), comment=u"停牌原因类别")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<SmallBoardCategory %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 股票利润表
class StockIncome(db.Model):
    __tablename__ = 'stock_income'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    ann_date = db.Column(db.Date, index=True, comment=u"公告日期")
    ann_date_str = db.Column(db.String(50), comment=u"公告日期")
    f_ann_date = db.Column(db.String(50), comment=u"实际公告日期，即发生过数据变更的最终日期")
    end_date = db.Column(db.String(50), comment=u"报告期")
    report_type = db.Column(db.String(50), comment=u"报告类型： 参考下表说明")
    comp_type = db.Column(db.String(50), comment=u"公司类型：1一般工商业 2银行 3保险 4证券")
    basic_eps = db.Column(db.DECIMAL(20, 4), comment=u"基本每股收益")
    diluted_eps = db.Column(db.DECIMAL(20, 4), comment=u"稀释每股收益")
    total_revenue = db.Column(db.DECIMAL(20, 4), comment=u"营业总收入 (元，下同)")
    revenue = db.Column(db.DECIMAL(20, 4), comment=u"营业收入")
    int_income = db.Column(db.DECIMAL(20, 4), comment=u"利息收入")
    prem_earned = db.Column(db.DECIMAL(20, 4), comment=u"已赚保费")
    comm_income = db.Column(db.DECIMAL(20, 4), comment=u"手续费及佣金收入")
    n_commis_income = db.Column(db.DECIMAL(20, 4), comment=u"手续费及佣金净收入")
    n_oth_income = db.Column(db.DECIMAL(20, 4), comment=u"其他经营净收益")
    n_oth_b_income = db.Column(db.DECIMAL(20, 4), comment=u"加:其他业务净收益")
    prem_income = db.Column(db.DECIMAL(20, 4), comment=u"保险业务收入")
    out_prem = db.Column(db.DECIMAL(20, 4), comment=u"减:分出保费")
    une_prem_reser = db.Column(db.DECIMAL(20, 4), comment=u"提取未到期责任准备金")
    reins_income = db.Column(db.DECIMAL(20, 4), comment=u"其中:分保费收入")
    n_sec_tb_income = db.Column(db.DECIMAL(20, 4), comment=u"代理买卖证券业务净收入")
    n_sec_uw_income = db.Column(db.DECIMAL(20, 4), comment=u"证券承销业务净收入")
    n_asset_mg_income = db.Column(db.DECIMAL(20, 4), comment=u"受托客户资产管理业务净收入")
    oth_b_income = db.Column(db.DECIMAL(20, 4), comment=u"其他业务收入")
    fv_value_chg_gain = db.Column(db.DECIMAL(20, 4), comment=u"加:公允价值变动净收益")
    invest_income = db.Column(db.DECIMAL(20, 4), comment=u"加:投资净收益")
    ass_invest_income = db.Column(db.DECIMAL(20, 4), comment=u"其中:对联营企业和合营企业的投资收益")
    forex_gain = db.Column(db.DECIMAL(20, 4), comment=u"加:汇兑净收益")
    total_cogs = db.Column(db.DECIMAL(20, 4), comment=u"营业总成本")
    oper_cost = db.Column(db.DECIMAL(20, 4), comment=u"减:营业成本")
    int_exp = db.Column(db.DECIMAL(20, 4), comment=u"减:利息支出")
    comm_exp = db.Column(db.DECIMAL(20, 4), comment=u"减:手续费及佣金支出")
    biz_tax_surchg = db.Column(db.DECIMAL(20, 4), comment=u"减:营业税金及附加")
    sell_exp = db.Column(db.DECIMAL(20, 4), comment=u"减:销售费用")
    admin_exp = db.Column(db.DECIMAL(20, 4), comment=u"减:管理费用")
    fin_exp = db.Column(db.DECIMAL(20, 4), comment=u"减:财务费用")
    assets_impair_loss = db.Column(db.DECIMAL(20, 4), comment=u"减:资产减值损失")
    prem_refund = db.Column(db.DECIMAL(20, 4), comment=u"退保金")
    compens_payout = db.Column(db.DECIMAL(20, 4), comment=u"赔付总支出")
    reser_insur_liab = db.Column(db.DECIMAL(20, 4), comment=u"提取保险责任准备金")
    div_payt = db.Column(db.DECIMAL(20, 4), comment=u"保户红利支出")
    reins_exp = db.Column(db.DECIMAL(20, 4), comment=u"分保费用")
    oper_exp = db.Column(db.DECIMAL(20, 4), comment=u"营业支出")
    compens_payout_refu = db.Column(db.DECIMAL(20, 4), comment=u"减:摊回赔付支出")
    insur_reser_refu = db.Column(db.DECIMAL(20, 4), comment=u"减:摊回保险责任准备金")
    reins_cost_refund = db.Column(db.DECIMAL(20, 4), comment=u"减:摊回分保费用")
    other_bus_cost = db.Column(db.DECIMAL(20, 4), comment=u"其他业务成本")
    operate_profit = db.Column(db.DECIMAL(20, 4), comment=u"营业利润")
    non_oper_income = db.Column(db.DECIMAL(20, 4), comment=u"加:营业外收入")
    non_oper_exp = db.Column(db.DECIMAL(20, 4), comment=u"减:营业外支出")
    nca_disploss = db.Column(db.DECIMAL(20, 4), comment=u"其中:减:非流动资产处置净损失")
    total_profit = db.Column(db.DECIMAL(20, 4), comment=u"利润总额")
    income_tax = db.Column(db.DECIMAL(20, 4), comment=u"所得税费用")
    n_income = db.Column(db.DECIMAL(20, 4), comment=u"净利润(含少数股东损益)")
    n_income_attr_p = db.Column(db.DECIMAL(20, 4), comment=u"净利润(不含少数股东损益)")
    minority_gain = db.Column(db.DECIMAL(20, 4), comment=u"少数股东损益")
    oth_compr_income = db.Column(db.DECIMAL(20, 4), comment=u"其他综合收益")
    t_compr_income = db.Column(db.DECIMAL(20, 4), comment=u"综合收益总额")
    compr_inc_attr_p = db.Column(db.DECIMAL(20, 4), comment=u"归属于母公司(或股东)的综合收益总额")
    compr_inc_attr_m_s = db.Column(db.DECIMAL(20, 4), comment=u"归属于少数股东的综合收益总额")
    ebit = db.Column(db.DECIMAL(20, 4), comment=u"息税折旧摊销前利润")
    ebitda = db.Column(db.DECIMAL(20, 4), comment=u"保险业务支出")
    insurance_exp = db.Column(db.DECIMAL(20, 4), comment=u"年初未分配利润")
    undist_profit = db.Column(db.DECIMAL(20, 4), comment=u"可分配利润")

    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockIncome %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 股票资产负债表
class StockBalanceSheet(db.Model):
    __tablename__ = 'stock_balance_sheet'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    ann_date = db.Column(db.Date, index=True, comment=u"公告日期")
    ann_date_str = db.Column(db.String(50), comment=u"公告日期")
    f_ann_date = db.Column(db.String(50), comment=u"实际公告日期，即发生过数据变更的最终日期")
    end_date = db.Column(db.String(50), comment=u"报告期")
    report_type = db.Column(db.String(50), comment=u"报告类型： 参考下表说明")
    comp_type = db.Column(db.String(50), comment=u"公司类型：1一般工商业 2银行 3保险 4证券")
    total_share = db.Column(db.DECIMAL(20, 4), comment=u"期末总股本")
    cap_rese = db.Column(db.DECIMAL(20, 4), comment=u"资本公积金 (元，下同)")
    undistr_porfit = db.Column(db.DECIMAL(20, 4), comment=u"未分配利润")
    surplus_rese = db.Column(db.DECIMAL(20, 4), comment=u"盈余公积金")
    special_rese = db.Column(db.DECIMAL(20, 4), comment=u"专项储备")
    money_cap = db.Column(db.DECIMAL(20, 4), comment=u"货币资金")
    trad_asset = db.Column(db.DECIMAL(20, 4), comment=u"交易性金融资产")
    notes_receiv = db.Column(db.DECIMAL(20, 4), comment=u"应收票据")
    accounts_receiv = db.Column(db.DECIMAL(20, 4), comment=u"应收账款")
    oth_receiv = db.Column(db.DECIMAL(20, 4), comment=u"其他应收款")
    prepayment = db.Column(db.DECIMAL(20, 4), comment=u"预付款项")
    div_receiv = db.Column(db.DECIMAL(20, 4), comment=u"应收股利")
    int_receiv = db.Column(db.DECIMAL(20, 4), comment=u"应收利息")
    inventories = db.Column(db.DECIMAL(20, 4), comment=u"存货")
    amor_exp = db.Column(db.DECIMAL(20, 4), comment=u"长期待摊费用")
    nca_within_1y = db.Column(db.DECIMAL(20, 4), comment=u"一年内到期的非流动资产")
    sett_rsrv = db.Column(db.DECIMAL(20, 4), comment=u"结算备付金")
    loanto_oth_bank_fi = db.Column(db.DECIMAL(20, 4), comment=u"拆出资金")
    premium_receiv = db.Column(db.DECIMAL(20, 4), comment=u"应收保费")
    reinsur_receiv = db.Column(db.DECIMAL(20, 4), comment=u"应收分保账款")
    reinsur_res_receiv = db.Column(db.DECIMAL(20, 4), comment=u"应收分保合同准备金")
    pur_resale_fa = db.Column(db.DECIMAL(20, 4), comment=u"买入返售金融资产")
    oth_cur_assets = db.Column(db.DECIMAL(20, 4), comment=u"其他流动资产")
    total_cur_assets = db.Column(db.DECIMAL(20, 4), comment=u"流动资产合计")
    fa_avail_for_sale = db.Column(db.DECIMAL(20, 4), comment=u"可供出售金融资产")
    htm_invest = db.Column(db.DECIMAL(20, 4), comment=u"持有至到期投资")
    lt_eqt_invest = db.Column(db.DECIMAL(20, 4), comment=u"长期股权投资")
    invest_real_estate = db.Column(db.DECIMAL(20, 4), comment=u"投资性房地产")
    time_deposits = db.Column(db.DECIMAL(20, 4), comment=u"定期存款")
    oth_assets = db.Column(db.DECIMAL(20, 4), comment=u"其他资产")
    lt_rec = db.Column(db.DECIMAL(20, 4), comment=u"长期应收款")
    fix_assets = db.Column(db.DECIMAL(20, 4), comment=u"固定资产")
    cip = db.Column(db.DECIMAL(20, 4), comment=u"在建工程")
    const_materials = db.Column(db.DECIMAL(20, 4), comment=u"工程物资")
    fixed_assets_disp = db.Column(db.DECIMAL(20, 4), comment=u"固定资产清理")
    produc_bio_assets = db.Column(db.DECIMAL(20, 4), comment=u"生产性生物资产")
    oil_and_gas_assets = db.Column(db.DECIMAL(20, 4), comment=u"油气资产")
    intan_assets = db.Column(db.DECIMAL(20, 4), comment=u"无形资产")
    r_and_d = db.Column(db.DECIMAL(20, 4), comment=u"研发支出")
    goodwill = db.Column(db.DECIMAL(20, 4), comment=u"商誉")
    lt_amor_exp = db.Column(db.DECIMAL(20, 4), comment=u"长期待摊费用")
    defer_tax_assets = db.Column(db.DECIMAL(20, 4), comment=u"递延所得税资产")
    decr_in_disbur = db.Column(db.DECIMAL(20, 4), comment=u"发放贷款及垫款")
    oth_nca = db.Column(db.DECIMAL(20, 4), comment=u"其他非流动资产")
    total_nca = db.Column(db.DECIMAL(20, 4), comment=u"非流动资产合计")
    cash_reser_cb = db.Column(db.DECIMAL(20, 4), comment=u"现金及存放中央银行款项")
    depos_in_oth_bfi = db.Column(db.DECIMAL(20, 4), comment=u"存放同业和其它金融机构款项")
    prec_metals = db.Column(db.DECIMAL(20, 4), comment=u"贵金属")
    deriv_assets = db.Column(db.DECIMAL(20, 4), comment=u"衍生金融资产")
    rr_reins_une_prem = db.Column(db.DECIMAL(20, 4), comment=u"应收分保未到期责任准备金")
    rr_reins_outstd_cla = db.Column(db.DECIMAL(20, 4), comment=u"应收分保未决赔款准备金")
    rr_reins_lins_liab = db.Column(db.DECIMAL(20, 4), comment=u"应收分保寿险责任准备金")
    rr_reins_lthins_liab = db.Column(db.DECIMAL(20, 4), comment=u"应收分保长期健康险责任准备金")
    refund_depos = db.Column(db.DECIMAL(20, 4), comment=u"存出保证金")
    ph_pledge_loans = db.Column(db.DECIMAL(20, 4), comment=u"保户质押贷款")
    refund_cap_depos = db.Column(db.DECIMAL(20, 4), comment=u"存出资本保证金")
    indep_acct_assets = db.Column(db.DECIMAL(20, 4), comment=u"独立账户资产")
    client_depos = db.Column(db.DECIMAL(20, 4), comment=u"其中：客户资金存款")
    client_prov = db.Column(db.DECIMAL(20, 4), comment=u"其中：客户备付金")
    transac_seat_fee = db.Column(db.DECIMAL(20, 4), comment=u"其中:交易席位费")
    invest_as_receiv = db.Column(db.DECIMAL(20, 4), comment=u"应收款项类投资")
    total_assets = db.Column(db.DECIMAL(20, 4), comment=u"资产总计")
    lt_borr = db.Column(db.DECIMAL(20, 4), comment=u"长期借款")
    st_borr = db.Column(db.DECIMAL(20, 4), comment=u"短期借款")
    cb_borr = db.Column(db.DECIMAL(20, 4), comment=u"向中央银行借款")
    depos_ib_deposits = db.Column(db.DECIMAL(20, 4), comment=u"吸收存款及同业存放")
    loan_oth_bank = db.Column(db.DECIMAL(20, 4), comment=u"拆入资金")
    trading_fl = db.Column(db.DECIMAL(20, 4), comment=u"交易性金融负债")
    notes_payable = db.Column(db.DECIMAL(20, 4), comment=u"应付票据")
    acct_payable = db.Column(db.DECIMAL(20, 4), comment=u"应付账款")
    adv_receipts = db.Column(db.DECIMAL(20, 4), comment=u"预收款项")
    sold_for_repur_fa = db.Column(db.DECIMAL(20, 4), comment=u"卖出回购金融资产款")
    comm_payable = db.Column(db.DECIMAL(20, 4), comment=u"应付手续费及佣金")
    payroll_payable = db.Column(db.DECIMAL(20, 4), comment=u"应付职工薪酬")
    taxes_payable = db.Column(db.DECIMAL(20, 4), comment=u"应交税费")
    int_payable = db.Column(db.DECIMAL(20, 4), comment=u"应付利息")
    div_payable = db.Column(db.DECIMAL(20, 4), comment=u"应付股利")
    oth_payable = db.Column(db.DECIMAL(20, 4), comment=u"其他应付款")
    acc_exp = db.Column(db.DECIMAL(20, 4), comment=u"预提费用")
    deferred_inc = db.Column(db.DECIMAL(20, 4), comment=u"递延收益")
    st_bonds_payable = db.Column(db.DECIMAL(20, 4), comment=u"应付短期债券")
    payable_to_reinsurer = db.Column(db.DECIMAL(20, 4), comment=u"应付分保账款")
    rsrv_insur_cont = db.Column(db.DECIMAL(20, 4), comment=u"保险合同准备金")
    acting_trading_sec = db.Column(db.DECIMAL(20, 4), comment=u"代理买卖证券款")
    acting_uw_sec = db.Column(db.DECIMAL(20, 4), comment=u"代理承销证券款")
    non_cur_liab_due_1y = db.Column(db.DECIMAL(20, 4), comment=u"一年内到期的非流动负债")
    oth_cur_liab = db.Column(db.DECIMAL(20, 4), comment=u"其他流动负债")
    total_cur_liab = db.Column(db.DECIMAL(20, 4), comment=u"流动负债合计")
    bond_payable = db.Column(db.DECIMAL(20, 4), comment=u"应付债券")
    lt_payable = db.Column(db.DECIMAL(20, 4), comment=u"长期应付款")
    specific_payables = db.Column(db.DECIMAL(20, 4), comment=u"专项应付款")
    estimated_liab = db.Column(db.DECIMAL(20, 4), comment=u"预计负债")
    defer_tax_liab = db.Column(db.DECIMAL(20, 4), comment=u"递延所得税负债")
    defer_inc_non_cur_liab = db.Column(db.DECIMAL(20, 4), comment=u"递延收益-非流动负债")
    oth_ncl = db.Column(db.DECIMAL(20, 4), comment=u"其他非流动负债")
    total_ncl = db.Column(db.DECIMAL(20, 4), comment=u"非流动负债合计")
    depos_oth_bfi = db.Column(db.DECIMAL(20, 4), comment=u"同业和其它金融机构存放款项")
    deriv_liab = db.Column(db.DECIMAL(20, 4), comment=u"衍生金融负债")
    depos = db.Column(db.DECIMAL(20, 4), comment=u"吸收存款")
    agency_bus_liab = db.Column(db.DECIMAL(20, 4), comment=u"代理业务负债")
    oth_liab = db.Column(db.DECIMAL(20, 4), comment=u"其他负债")
    prem_receiv_adva = db.Column(db.DECIMAL(20, 4), comment=u"预收保费")
    depos_received = db.Column(db.DECIMAL(20, 4), comment=u"存入保证金")
    ph_invest = db.Column(db.DECIMAL(20, 4), comment=u"保户储金及投资款")
    reser_une_prem = db.Column(db.DECIMAL(20, 4), comment=u"未到期责任准备金")
    reser_outstd_claims = db.Column(db.DECIMAL(20, 4), comment=u"未决赔款准备金")
    reser_lins_liab = db.Column(db.DECIMAL(20, 4), comment=u"寿险责任准备金")
    reser_lthins_liab = db.Column(db.DECIMAL(20, 4), comment=u"长期健康险责任准备金")
    indept_acc_liab = db.Column(db.DECIMAL(20, 4), comment=u"独立账户负债")
    pledge_borr = db.Column(db.DECIMAL(20, 4), comment=u"其中:质押借款")
    indem_payable = db.Column(db.DECIMAL(20, 4), comment=u"应付赔付款")
    policy_div_payable = db.Column(db.DECIMAL(20, 4), comment=u"应付保单红利")
    total_liab = db.Column(db.DECIMAL(20, 4), comment=u"负债合计")
    treasury_share = db.Column(db.DECIMAL(20, 4), comment=u"减:库存股")
    ordin_risk_reser = db.Column(db.DECIMAL(20, 4), comment=u"一般风险准备")
    forex_differ = db.Column(db.DECIMAL(20, 4), comment=u"外币报表折算差额")
    invest_loss_unconf = db.Column(db.DECIMAL(20, 4), comment=u"未确认的投资损失")
    minority_int = db.Column(db.DECIMAL(20, 4), comment=u"少数股东权益")
    total_hldr_eqy_exc_min_int = db.Column(db.DECIMAL(20, 4), comment=u"股东权益合计(不含少数股东权益)")
    total_hldr_eqy_inc_min_int = db.Column(db.DECIMAL(20, 4), comment=u"股东权益合计(含少数股东权益)")
    total_liab_hldr_eqy = db.Column(db.DECIMAL(20, 4), comment=u"负债及股东权益总计")
    lt_payroll_payable = db.Column(db.DECIMAL(20, 4), comment=u"长期应付职工薪酬")
    oth_comp_income = db.Column(db.DECIMAL(20, 4), comment=u"其他综合收益")
    oth_eqt_tools = db.Column(db.DECIMAL(20, 4), comment=u"其他权益工具")
    oth_eqt_tools_p_shr = db.Column(db.DECIMAL(20, 4), comment=u"其他权益工具(优先股)")
    lending_funds = db.Column(db.DECIMAL(20, 4), comment=u"融出资金")
    acc_receivable = db.Column(db.DECIMAL(20, 4), comment=u"应收款项")
    st_fin_payable = db.Column(db.DECIMAL(20, 4), comment=u"应付短期融资款")
    payables = db.Column(db.DECIMAL(20, 4), comment=u"应付款项")
    hfs_assets = db.Column(db.DECIMAL(20, 4), comment=u"持有待售的资产")
    hfs_sales = db.Column(db.DECIMAL(20, 4), comment=u"持有待售的负债")

    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockBalanceSheet %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 股票现金流量表
class StockCashFlow(db.Model):
    __tablename__ = 'stock_cash_flow'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    ann_date = db.Column(db.Date, index=True, comment=u"公告日期")
    ann_date_str = db.Column(db.String(50), comment=u"公告日期")
    f_ann_date = db.Column(db.String(50), comment=u"实际公告日期，即发生过数据变更的最终日期")
    end_date = db.Column(db.String(50), comment=u"报告期")
    report_type = db.Column(db.String(50), comment=u"报告类型： 参考下表说明")
    comp_type = db.Column(db.String(50), comment=u"公司类型：1一般工商业 2银行 3保险 4证券")
    net_profit = db.Column(db.DECIMAL(20, 4), comment=u"净利润 (元，下同)")
    finan_exp = db.Column(db.DECIMAL(20, 4), comment=u"财务费用")
    c_fr_sale_sg = db.Column(db.DECIMAL(20, 4), comment=u"销售商品、提供劳务收到的现金")
    recp_tax_rends = db.Column(db.DECIMAL(20, 4), comment=u"收到的税费返还")
    n_depos_incr_fi = db.Column(db.DECIMAL(20, 4), comment=u"客户存款和同业存放款项净增加额")
    n_incr_loans_cb = db.Column(db.DECIMAL(20, 4), comment=u"向中央银行借款净增加额")
    n_inc_borr_oth_fi = db.Column(db.DECIMAL(20, 4), comment=u"向其他金融机构拆入资金净增加额")
    prem_fr_orig_contr = db.Column(db.DECIMAL(20, 4), comment=u"收到原保险合同保费取得的现金")
    n_incr_insured_dep = db.Column(db.DECIMAL(20, 4), comment=u"保户储金净增加额")
    n_reinsur_prem = db.Column(db.DECIMAL(20, 4), comment=u"收到再保业务现金净额")
    n_incr_disp_tfa = db.Column(db.DECIMAL(20, 4), comment=u"处置交易性金融资产净增加额")
    ifc_cash_incr = db.Column(db.DECIMAL(20, 4), comment=u"收取利息和手续费净增加额")
    n_incr_disp_faas = db.Column(db.DECIMAL(20, 4), comment=u"处置可供出售金融资产净增加额")
    n_incr_loans_oth_bank = db.Column(db.DECIMAL(20, 4), comment=u"拆入资金净增加额")
    n_cap_incr_repur = db.Column(db.DECIMAL(20, 4), comment=u"回购业务资金净增加额")
    c_fr_oth_operate_a = db.Column(db.DECIMAL(20, 4), comment=u"收到其他与经营活动有关的现金")
    c_inf_fr_operate_a = db.Column(db.DECIMAL(20, 4), comment=u"经营活动现金流入小计")
    c_paid_goods_s = db.Column(db.DECIMAL(20, 4), comment=u"购买商品、接受劳务支付的现金")
    c_paid_to_for_empl = db.Column(db.DECIMAL(20, 4), comment=u"支付给职工以及为职工支付的现金")
    c_paid_for_taxes = db.Column(db.DECIMAL(20, 4), comment=u"支付的各项税费")
    n_incr_clt_loan_adv = db.Column(db.DECIMAL(20, 4), comment=u"客户贷款及垫款净增加额")
    n_incr_dep_cbob = db.Column(db.DECIMAL(20, 4), comment=u"存放央行和同业款项净增加额")
    c_pay_claims_orig_inco = db.Column(db.DECIMAL(20, 4), comment=u"支付原保险合同赔付款项的现金")
    pay_handling_chrg = db.Column(db.DECIMAL(20, 4), comment=u"支付手续费的现金")
    pay_comm_insur_plcy = db.Column(db.DECIMAL(20, 4), comment=u"支付保单红利的现金")
    oth_cash_pay_oper_act = db.Column(db.DECIMAL(20, 4), comment=u"支付其他与经营活动有关的现金")
    st_cash_out_act = db.Column(db.DECIMAL(20, 4), comment=u"经营活动现金流出小计")
    n_cashflow_act = db.Column(db.DECIMAL(20, 4), comment=u"经营活动产生的现金流量净额")
    oth_recp_ral_inv_act = db.Column(db.DECIMAL(20, 4), comment=u"收到其他与投资活动有关的现金")
    c_disp_withdrwl_invest = db.Column(db.DECIMAL(20, 4), comment=u"收回投资收到的现金")
    c_recp_return_invest = db.Column(db.DECIMAL(20, 4), comment=u"取得投资收益收到的现金")
    n_recp_disp_fiolta = db.Column(db.DECIMAL(20, 4), comment=u"处置固定资产、无形资产和其他长期资产收回的现金净额")
    n_recp_disp_sobu = db.Column(db.DECIMAL(20, 4), comment=u"处置子公司及其他营业单位收到的现金净额")
    stot_inflows_inv_act = db.Column(db.DECIMAL(20, 4), comment=u"投资活动现金流入小计")
    c_pay_acq_const_fiolta = db.Column(db.DECIMAL(20, 4), comment=u"购建固定资产、无形资产和其他长期资产支付的现金")
    c_paid_invest = db.Column(db.DECIMAL(20, 4), comment=u"投资支付的现金")
    n_disp_subs_oth_biz = db.Column(db.DECIMAL(20, 4), comment=u"取得子公司及其他营业单位支付的现金净额")
    oth_pay_ral_inv_act = db.Column(db.DECIMAL(20, 4), comment=u"支付其他与投资活动有关的现金")
    n_incr_pledge_loan = db.Column(db.DECIMAL(20, 4), comment=u"质押贷款净增加额")
    stot_out_inv_act = db.Column(db.DECIMAL(20, 4), comment=u"投资活动现金流出小计")
    n_cashflow_inv_act = db.Column(db.DECIMAL(20, 4), comment=u"投资活动产生的现金流量净额")
    c_recp_borrow = db.Column(db.DECIMAL(20, 4), comment=u"取得借款收到的现金")
    c_pay_dist_dpcp_int_exp = db.Column(db.DECIMAL(20, 4), comment=u"分配股利、利润或偿付利息支付的现金")
    incl_dvd_profit_paid_sc_ms = db.Column(db.DECIMAL(20, 4), comment=u"其中:子公司支付给少数股东的股利、利润")
    oth_cashpay_ral_fnc_act = db.Column(db.DECIMAL(20, 4), comment=u"支付其他与筹资活动有关的现金")
    stot_cashout_fnc_act = db.Column(db.DECIMAL(20, 4), comment=u"筹资活动现金流出小计")
    n_cash_flows_fnc_act = db.Column(db.DECIMAL(20, 4), comment=u"筹资活动产生的现金流量净额")
    eff_fx_flu_cash = db.Column(db.DECIMAL(20, 4), comment=u"汇率变动对现金的影响")
    n_incr_cash_cash_equ = db.Column(db.DECIMAL(20, 4), comment=u"现金及现金等价物净增加额")
    c_cash_equ_beg_period = db.Column(db.DECIMAL(20, 4), comment=u"期初现金及现金等价物余额")
    c_cash_equ_end_period = db.Column(db.DECIMAL(20, 4), comment=u"期末现金及现金等价物余额")
    c_recp_cap_contrib = db.Column(db.DECIMAL(20, 4), comment=u"吸收投资收到的现金")
    incl_cash_rec_saims = db.Column(db.DECIMAL(20, 4), comment=u"其中:子公司吸收少数股东投资收到的现金")
    uncon_invest_loss = db.Column(db.DECIMAL(20, 4), comment=u"未确认投资损失")
    prov_depr_assets = db.Column(db.DECIMAL(20, 4), comment=u"加:资产减值准备")
    depr_fa_coga_dpba = db.Column(db.DECIMAL(20, 4), comment=u"固定资产折旧、油气资产折耗、生产性生物资产折旧")
    amort_intang_assets = db.Column(db.DECIMAL(20, 4), comment=u"无形资产摊销")
    lt_amort_deferred_exp = db.Column(db.DECIMAL(20, 4), comment=u"长期待摊费用摊销")
    decr_deferred_exp = db.Column(db.DECIMAL(20, 4), comment=u"待摊费用减少")
    incr_acc_exp = db.Column(db.DECIMAL(20, 4), comment=u"预提费用增加")
    loss_disp_fiolta = db.Column(db.DECIMAL(20, 4), comment=u"处置固定、无形资产和其他长期资产的损失")
    loss_scr_fa = db.Column(db.DECIMAL(20, 4), comment=u"固定资产报废损失")
    loss_fv_chg = db.Column(db.DECIMAL(20, 4), comment=u"公允价值变动损失")
    invest_loss = db.Column(db.DECIMAL(20, 4), comment=u"投资损失")
    decr_def_inc_tax_assets = db.Column(db.DECIMAL(20, 4), comment=u"递延所得税资产减少")
    incr_def_inc_tax_liab = db.Column(db.DECIMAL(20, 4), comment=u"递延所得税负债增加")
    decr_inventories = db.Column(db.DECIMAL(20, 4), comment=u"存货的减少")
    decr_oper_payable = db.Column(db.DECIMAL(20, 4), comment=u"经营性应收项目的减少")
    incr_oper_payable = db.Column(db.DECIMAL(20, 4), comment=u"经营性应付项目的增加")
    others = db.Column(db.DECIMAL(20, 4), comment=u"其他")
    im_net_cashflow_oper_act = db.Column(db.DECIMAL(20, 4), comment=u"经营活动产生的现金流量净额(间接法)")
    conv_debt_into_cap = db.Column(db.DECIMAL(20, 4), comment=u"债务转为资本")
    conv_copbonds_due_within_1y = db.Column(db.DECIMAL(20, 4), comment=u"一年内到期的可转换公司债券")
    fa_fnc_leases = db.Column(db.DECIMAL(20, 4), comment=u"融资租入固定资产")
    end_bal_cash = db.Column(db.DECIMAL(20, 4), comment=u"现金的期末余额")
    beg_bal_cash = db.Column(db.DECIMAL(20, 4), comment=u"减:现金的期初余额")
    end_bal_cash_equ = db.Column(db.DECIMAL(20, 4), comment=u"加:现金等价物的期末余额")
    beg_bal_cash_equ = db.Column(db.DECIMAL(20, 4), comment=u"减:现金等价物的期初余额")
    im_n_incr_cash_equ = db.Column(db.DECIMAL(20, 4), comment=u"现金及现金等价物净增加额(间接法)")

    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<GemCategory %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 股票业绩预告
class StockForeCast(db.Model):
    __tablename__ = 'stock_fore_cast'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    ann_date = db.Column(db.Date, index=True, comment=u"公告日期")
    ann_date_str = db.Column(db.String(50), comment=u"公告日期")
    end_date = db.Column(db.String(50), comment=u"报告期")
    type = db.Column(db.String(50), comment=u"业绩预告类型(预增/预减/扭亏/首亏/续亏/续盈/略增/略减)")
    p_change_min = db.Column(db.DECIMAL(20, 4), comment=u"预告净利润变动幅度下限（%）")
    p_change_max = db.Column(db.DECIMAL(20, 4), comment=u"预告净利润变动幅度上限（%）")
    net_profit_min = db.Column(db.DECIMAL(20, 4), comment=u"预告净利润下限（万元）")
    net_profit_max = db.Column(db.DECIMAL(20, 4), comment=u"预告净利润上限（万元）")
    last_parent_net = db.Column(db.String(30), comment=u"上年同期归属母公司净利润")
    first_ann_date = db.Column(db.String(50), comment=u"首次公告日")
    summary = db.Column(db.String(150), comment=u"业绩预告摘要")
    change_reason = db.Column(db.TEXT, comment=u"业绩变动原因")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockForecast %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 股票业绩快报
class StockExpress(db.Model):
    __tablename__ = 'stock_express'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    ann_date = db.Column(db.Date, index=True, comment=u"公告日期")
    ann_date_str = db.Column(db.String(50), comment=u"公告日期")
    end_date = db.Column(db.String(50), comment=u"报告期")
    revenue = db.Column(db.DECIMAL(20, 4), comment=u"营业收入(元)")
    operate_profit = db.Column(db.DECIMAL(20, 4), comment=u"营业利润(元)")
    total_profit = db.Column(db.DECIMAL(20, 4), comment=u"利润总额(元)")
    n_income = db.Column(db.DECIMAL(20, 4), comment=u"净利润(元)")
    total_assets = db.Column(db.DECIMAL(20, 4), comment=u"总资产(元)")
    total_hldr_eqy_exc_min_int = db.Column(db.DECIMAL(20, 4), comment=u"股东权益合计(不含少数股东权益)(元)")
    diluted_eps = db.Column(db.DECIMAL(20, 4), comment=u"每股收益(摊薄)(元)")
    diluted_roe = db.Column(db.DECIMAL(20, 4), comment=u"净资产收益率(摊薄)(%)")
    bps = db.Column(db.DECIMAL(20, 4), comment=u"每股净资产")
    yoy_sales = db.Column(db.DECIMAL(20, 4), comment=u"同比增长率:营业收入")
    yoy_op = db.Column(db.DECIMAL(20, 4), comment=u"同比增长率:营业利润")
    yoy_tp = db.Column(db.DECIMAL(20, 4), comment=u"同比增长率:利润总额")
    yoy_dedu_np = db.Column(db.DECIMAL(20, 4), comment=u"同比增长率:归属母公司股东的净利润")
    yoy_eps = db.Column(db.DECIMAL(20, 4), comment=u"同比增长率:基本每股收益")
    yoy_roe = db.Column(db.DECIMAL(20, 4), comment=u"同比增减:加权平均净资产收益率")
    growth_assets = db.Column(db.DECIMAL(20, 4), comment=u"比年初增长率:总资产")
    yoy_equity = db.Column(db.DECIMAL(20, 4), comment=u"比年初增长率:归属母公司的股东权益")
    growth_bps = db.Column(db.DECIMAL(20, 4), comment=u"比年初增长率:归属于母公司股东的每股净资产")
    or_last_year = db.Column(db.DECIMAL(20, 4), comment=u"去年同期营业收入")
    op_last_year = db.Column(db.DECIMAL(20, 4), comment=u"去年同期营业利润")
    tp_last_year = db.Column(db.DECIMAL(20, 4), comment=u"去年同期利润总额")
    np_last_year = db.Column(db.DECIMAL(20, 4), comment=u"去年同期净利润")
    eps_last_year = db.Column(db.DECIMAL(20, 4), comment=u"去年同期每股收益")
    open_net_assets = db.Column(db.DECIMAL(20, 4), comment=u"期初净资产")
    open_bps = db.Column(db.DECIMAL(20, 4), comment=u"期初每股净资产")
    perf_summary = db.Column(db.DECIMAL(20, 4), comment=u"业绩简要说明")
    is_audit = db.Column(db.Integer(), comment=u"是否审计： 1是 0否")
    remark = db.Column(db.String(100), comment=u"备注")

    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockForecast %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 股票分红送股
class StockDividend(db.Model):
    __tablename__ = 'stock_dividend'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    ann_date = db.Column(db.Date, index=True, comment=u"预案公告日")
    ann_date_str = db.Column(db.String(50), comment=u"预案公告日")
    end_date = db.Column(db.String(30), comment=u"分红年度")
    div_proc = db.Column(db.String(30), comment=u"实施进度")
    stk_div = db.Column(db.DECIMAL(20, 8), comment=u"每股送转")
    stk_bo_rate = db.Column(db.DECIMAL(20, 8), comment=u"每股送股比例")
    stk_co_rate = db.Column(db.DECIMAL(20, 8), comment=u"每股转增比例")
    cash_div = db.Column(db.DECIMAL(20, 8), comment=u"每股分红（税后）")
    cash_div_tax = db.Column(db.DECIMAL(20, 8), comment=u"每股分红（税前）")
    record_date = db.Column(db.String(30), comment=u"股权登记日")
    ex_date = db.Column(db.String(30), comment=u"除权除息日")
    pay_date = db.Column(db.String(30), comment=u"派息日")
    div_listdate = db.Column(db.String(30), comment=u"红股上市日")
    imp_ann_date = db.Column(db.String(30), comment=u"实施公告日")
    base_date = db.Column(db.String(30), comment=u"基准日")
    base_share = db.Column(db.DECIMAL(20, 8), comment=u"基准股本（万）")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockDividend %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 财务审计意见
class StockFinaAudit(db.Model):
    __tablename__ = 'stock_fina_audit'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    ann_date = db.Column(db.Date, index=True, comment=u"公告日期")
    ann_date_str = db.Column(db.String(50), comment=u"公告日期")
    end_date = db.Column(db.Date, comment=u"报告期")
    end_date_str = db.Column(db.String(50), comment=u"报告期")
    audit_result = db.Column(db.String(50), comment=u"审计结果")
    audit_fees = db.Column(db.DECIMAL(20, 4), comment=u"审计总费用（元）")
    audit_agency = db.Column(db.String(50), comment=u"会计事务所")
    audit_sign = db.Column(db.String(50), comment=u"签字会计师")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockFinaAudit %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 财务审计意见
class StockFinaIndicator(db.Model):
    __tablename__ = 'stock_fina_indicator'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    ann_date = db.Column(db.Date, index=True, comment=u"公告日期")
    ann_date_str = db.Column(db.String(50), comment=u"公告日期")
    end_date = db.Column(db.Date, comment=u"报告期")
    end_date_str = db.Column(db.String(50), comment=u"报告期")
    audit_result = db.Column(db.String(50), comment=u"审计结果")
    audit_fees = db.Column(db.DECIMAL(20, 4), comment=u"审计总费用（元）")
    audit_agency = db.Column(db.String(50), comment=u"会计事务所")
    audit_sign = db.Column(db.String(50), comment=u"签字会计师")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockFinaIndicator %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 主营业务构成
class StockFinaMainbz(db.Model):
    __tablename__ = 'stock_fina_mainbz'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    end_date = db.Column(db.Date, index=True, comment=u"报告期")
    end_date_str = db.Column(db.String(50), comment=u"报告期")
    bz_item = db.Column(db.String(50), comment=u"主营业务来源")
    bz_sales = db.Column(db.DECIMAL(20, 4), comment=u"主营业务收入(元)")
    bz_profit = db.Column(db.DECIMAL(20, 4), comment=u"主营业务利润(元)")
    bz_cost = db.Column(db.DECIMAL(20, 4), comment=u"主营业务成本(元)")
    curr_type = db.Column(db.String(50), comment=u"货币代码")
    update_flag = db.Column(db.String(50), comment=u"是否更新")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockFinaMainbz %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 沪深港通资金流向
class StockMoneyFlowHsgt(db.Model):
    __tablename__ = 'stock_money_flow_hsgt'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    trade_date = db.Column(db.Date, index=True, comment=u"交易日期")
    trade_date_str = db.Column(db.String(50), comment=u"交易日期")
    ggt_ss = db.Column(db.DECIMAL(20, 4), comment=u"港股通（上海）")
    ggt_sz = db.Column(db.DECIMAL(20, 4), comment=u"港股通（深圳）")
    hgt = db.Column(db.DECIMAL(20, 4), comment=u"沪股通（百万元）")
    sgt = db.Column(db.DECIMAL(20, 4), comment=u"深股通（百万元）")
    north_money = db.Column(db.DECIMAL(20, 4), comment=u"北向资金（百万元）")
    south_money = db.Column(db.DECIMAL(20, 4), comment=u"南向资金（百万元）")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockMoneyFlowHsgt %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 沪深股通十大成交股
class StockHsgtTop(db.Model):
    __tablename__ = 'stock_hsgt_top'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    trade_date = db.Column(db.Date, index=True, comment=u"交易日期")
    trade_date_str = db.Column(db.String(50), comment=u"交易日期")
    close = db.Column(db.DECIMAL(20, 4), comment=u"收盘价")
    change = db.Column(db.DECIMAL(20, 4), comment=u"涨跌额")
    rank = db.Column(db.Integer, comment=u"资金排名")
    market_type = db.Column(db.String(20), comment=u"市场类型（1：沪市 3：深市）")
    amount = db.Column(db.DECIMAL(20, 4), comment=u"成交金额（元）")
    net_amount = db.Column(db.DECIMAL(20, 4), comment=u"净成交金额（元）")
    buy = db.Column(db.DECIMAL(20, 4), comment=u"买入金额（元）")
    sell = db.Column(db.DECIMAL(20, 4), comment=u"卖出金额（元）")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockHsgtTop %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 港股通十大成交股
class StockGgtTop(db.Model):
    __tablename__ = 'stock_ggt_top'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    trade_date = db.Column(db.Date, index=True, comment=u"交易日期")
    trade_date_str = db.Column(db.String(50), comment=u"交易日期")
    close = db.Column(db.DECIMAL(20, 4), comment=u"收盘价")
    change = db.Column(db.DECIMAL(20, 4), comment=u"涨跌额")
    rank = db.Column(db.Integer, comment=u"资金排名")
    market_type = db.Column(db.String(20), comment=u"市场类型 2：港股通（沪） 4：港股通（深）")
    amount = db.Column(db.DECIMAL(20, 4), comment=u"累计成交金额（元）")
    net_amount = db.Column(db.DECIMAL(20, 4), comment=u"净买入金额（元）")
    sh_amount = db.Column(db.DECIMAL(20, 4), comment=u"沪市成交金额（元）")
    sh_net_amount = db.Column(db.DECIMAL(20, 4), comment=u"沪市净买入金额（元）")
    sh_buy = db.Column(db.DECIMAL(20, 4), comment=u"沪市买入金额（元）")
    sh_sell = db.Column(db.DECIMAL(20, 4), comment=u"沪市卖出金额")
    sz_amount = db.Column(db.DECIMAL(20, 4), comment=u"深市成交金额（元）")
    sz_net_amount = db.Column(db.DECIMAL(20, 4), comment=u"深市净买入金额（元）")
    sz_buy = db.Column(db.DECIMAL(20, 4), comment=u"深市买入金额（元）")
    sz_sell = db.Column(db.DECIMAL(20, 4), comment=u"深市卖出金额（元）")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockGgtTop %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 融资融券交易汇总
class StockMargin(db.Model):
    __tablename__ = 'stock_margin'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    trade_date = db.Column(db.Date, index=True, comment=u"交易日期")
    trade_date_str = db.Column(db.String(50), comment=u"交易日期")
    exchange_id = db.Column(db.String(50), comment=u"交易所代码")
    rzye = db.Column(db.DECIMAL(20, 4), comment=u"融资余额(元)")
    rzmre = db.Column(db.DECIMAL(20, 4), comment=u"融资买入额(元)")
    rzche = db.Column(db.DECIMAL(20, 4), comment=u"融资偿还额(元)")
    rqye = db.Column(db.DECIMAL(20, 4), comment=u"融券余额(元)")
    rqmcl = db.Column(db.DECIMAL(20, 4), comment=u"融券卖出量(股,份,手)")
    rzrqye = db.Column(db.DECIMAL(20, 4), comment=u"融资融券余额(元)")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockMargin %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 融资融券交易明细
class StockMarginDetail(db.Model):
    __tablename__ = 'stock_margin_detail'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    trade_date = db.Column(db.Date, index=True, comment=u"交易日期")
    trade_date_str = db.Column(db.String(50), comment=u"交易日期")
    exchange_id = db.Column(db.String(50), comment=u"交易所代码")
    rzye = db.Column(db.DECIMAL(20, 4), comment=u"融资余额(元)")
    rzmre = db.Column(db.DECIMAL(20, 4), comment=u"融资买入额(元)")
    rzche = db.Column(db.DECIMAL(20, 4), comment=u"融资偿还额(元)")
    rqye = db.Column(db.DECIMAL(20, 4), comment=u"融券余额(元)")
    rqmcl = db.Column(db.DECIMAL(20, 4), comment=u"融券卖出量(股,份,手)")
    rzrqye = db.Column(db.DECIMAL(20, 4), comment=u"融资融券余额(元)")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockMarginDetail %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 前十大股东
class StockTopHolders(db.Model):
    __tablename__ = 'stock_top_holders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    ann_date = db.Column(db.Date, index=True, comment=u"公告日期")
    ann_date_str = db.Column(db.String(50), comment=u"公告日期")
    end_date = db.Column(db.String(50), comment=u"报告期")
    holder_name = db.Column(db.String(50), comment=u"股东名称")
    hold_amount = db.Column(db.DECIMAL(20, 4), comment=u"持有数量（股）")
    hold_ratio = db.Column(db.DECIMAL(20, 4), comment=u"持有比例")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockTopHolders %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 前十大流通股东
class StockTopFloatHolders(db.Model):
    __tablename__ = 'stock_top_float_holders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    ann_date = db.Column(db.Date, index=True, comment=u"公告日期")
    ann_date_str = db.Column(db.String(50), comment=u"公告日期")
    end_date = db.Column(db.String(50), comment=u"报告期")
    holder_name = db.Column(db.String(50), comment=u"股东名称")
    hold_amount = db.Column(db.DECIMAL(20, 4), comment=u"持有数量（股）")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockTopFloatHolders %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 龙虎榜每日明细
class StockTopList(db.Model):
    __tablename__ = 'stock_top_list'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    trade_date = db.Column(db.Date, index=True, comment=u"交易日期")
    trade_date_str = db.Column(db.String(50), comment=u"交易日期")
    close = db.Column(db.DECIMAL(20, 4), comment=u"收盘价")
    pct_change = db.Column(db.DECIMAL(20, 4), comment=u"涨跌幅")
    turnover_rate = db.Column(db.DECIMAL(20, 4), comment=u"换手率")
    l_sell = db.Column(db.DECIMAL(20, 4), comment=u"龙虎榜卖出额")
    l_buy = db.Column(db.DECIMAL(20, 4), comment=u"龙虎榜买入额")
    l_amount = db.Column(db.DECIMAL(20, 4), comment=u"龙虎榜成交额")
    net_amount = db.Column(db.DECIMAL(20, 4), comment=u"龙虎榜净买入额")
    net_rate = db.Column(db.DECIMAL(20, 4), comment=u"龙虎榜净买额占比")
    amount_rate = db.Column(db.DECIMAL(20, 4), comment=u"龙虎榜成交额占比")
    float_values = db.Column(db.DECIMAL(20, 4), comment=u"当日流通市值")
    reason = db.Column(db.String(150), comment=u"上榜理由")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockTopList %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 龙虎榜机构明细
class StockTopInst(db.Model):
    __tablename__ = 'stock_top_inst'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    trade_date = db.Column(db.Date, index=True, comment=u"交易日期")
    trade_date_str = db.Column(db.String(50), comment=u"交易日期")
    exalter = db.Column(db.String(100), comment=u"营业部名称")
    buy = db.Column(db.DECIMAL(20, 4), comment=u"买入额（万）")
    buy_rate = db.Column(db.DECIMAL(20, 4), comment=u"买入占总成交比例")
    sell = db.Column(db.DECIMAL(20, 4), comment=u"卖出额（万）")
    sell_rate = db.Column(db.DECIMAL(20, 4), comment=u"卖出占总成交比例")
    net_buy = db.Column(db.DECIMAL(20, 4), comment=u"净成交额（万）")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockTopInst %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 股权质押统计数据
class StockPledgeStat(db.Model):
    __tablename__ = 'stock_pledge_stat'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    end_date = db.Column(db.Date, index=True, comment=u"截至日期")
    end_date_str = db.Column(db.String(50), comment=u"截至日期")
    pledge_count = db.Column(db.Integer, comment=u"质押次数")
    unrest_pledge = db.Column(db.DECIMAL(20, 4), comment=u"无限售股质押数量（万）")
    rest_pledge = db.Column(db.DECIMAL(20, 4), comment=u"限售股份质押数量（万）")
    total_share = db.Column(db.DECIMAL(20, 4), comment=u"总股本")
    pledge_ratio = db.Column(db.DECIMAL(20, 4), comment=u"质押比例")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockPledgeStat %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 股权质押明细
class StockPledgeDetail(db.Model):
    __tablename__ = 'stock_pledge_detail'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    ann_date = db.Column(db.Date, index=True, comment=u"公告日期")
    ann_date_str = db.Column(db.String(50), comment=u"公告日期")
    holder_name = db.Column(db.String(50), comment=u"股东名称")
    pledge_amount = db.Column(db.DECIMAL(20, 4), comment=u"质押数量")
    start_date = db.Column(db.String(50), comment=u"质押开始日期")
    end_date = db.Column(db.String(50), comment=u"质押结束日期")
    is_release = db.Column(db.String(50), comment=u"是否已解押")
    release_date = db.Column(db.String(50), comment=u"解押日期")
    pledgor = db.Column(db.String(50), comment=u"质押方")
    holding_amount = db.Column(db.DECIMAL(20, 4), comment=u"持股总数")
    pledged_amount = db.Column(db.DECIMAL(20, 4), comment=u"质押总数")
    p_total_ratio = db.Column(db.DECIMAL(20, 4), comment=u"本次质押占总股本比例")
    h_total_ratio = db.Column(db.DECIMAL(20, 4), comment=u"持股总数占总股本比例")
    is_buyback = db.Column(db.String(50), comment=u"是否回购")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockPledgeDetail %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 股票回购
class StockRepurchase(db.Model):
    __tablename__ = 'stock_repurchase'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    ann_date = db.Column(db.Date, index=True, comment=u"公告日期")
    ann_date_str = db.Column(db.String(50), comment=u"公告日期")
    end_date = db.Column(db.String(50), comment=u"截止日期")
    proc = db.Column(db.String(50), comment=u"进度")
    exp_date = db.Column(db.DECIMAL(20, 4), comment=u"过期日期")
    vol = db.Column(db.String(50), comment=u"回购数量")
    amount = db.Column(db.String(50), comment=u"回购金额")
    high_limit = db.Column(db.String(50), comment=u"回购最高价")
    low_limit = db.Column(db.String(50), comment=u"回购最低价")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockRepurchase %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 概念股分类
class StockConcept(db.Model):
    __tablename__ = 'stock_concept'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    ts_id = db.Column(db.String(50), comment=u"概念分类ID")
    ts_name = db.Column(db.String(50), comment=u"概念分类名称")
    src = db.Column(db.String(50), comment=u"来源")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockConcept %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 概念股列表
class StockConceptDetail(db.Model):
    __tablename__ = 'stock_concept_detail'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    ts_id = db.Column(db.String(50), comment=u"概念分类ID")
    ts_name = db.Column(db.String(50), comment=u"概念分类名称")
    in_date = db.Column(db.String(50), comment=u"纳入日期")
    out_date = db.Column(db.String(50), comment=u"剔除日期")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockConceptDetail %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 限售股解禁
class StockShareFloat(db.Model):
    __tablename__ = 'stock_share_float'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    ann_date = db.Column(db.Date, index=True, comment=u"公告日期")
    ann_date_str = db.Column(db.String(50), comment=u"公告日期")
    float_date = db.Column(db.String(50), comment=u"解禁日期")
    float_share = db.Column(db.DECIMAL(20, 4), comment=u"流通股份")
    float_ratio = db.Column(db.DECIMAL(20, 4), comment=u"流通股份占总股本比率")
    holder_name = db.Column(db.String(100), comment=u"股东名称")
    share_type = db.Column(db.String(50), comment=u"股份类型")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockShareFloat %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 大宗交易
class StockBlockTrade(db.Model):
    __tablename__ = 'stock_block_trade'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    trade_date = db.Column(db.Date, index=True, comment=u"交易日历")
    trade_date_str = db.Column(db.String(50), comment=u"交易日历")
    price = db.Column(db.DECIMAL(20, 4), comment=u"成交价")
    vol = db.Column(db.DECIMAL(20, 4), comment=u"成交量（万股）")
    amount = db.Column(db.DECIMAL(20, 4), comment=u"成交金额")
    buyer = db.Column(db.String(100), comment=u"买方营业部")
    seller = db.Column(db.String(100), comment=u"卖方营业部")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockBlockTrade %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 股票账户开户数据
class StockStkAccount(db.Model):
    __tablename__ = 'stock_stk_account'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, index=True, comment=u"统计周期")
    date_str = db.Column(db.String(50), comment=u"统计周期")
    weekly_new = db.Column(db.DECIMAL(20, 4), comment=u"本周新增（万）")
    total = db.Column(db.DECIMAL(20, 4), comment=u"期末总账户数（万）")
    weekly_hold = db.Column(db.DECIMAL(20, 4), comment=u"本周持仓账户数（万）")
    weekly_trade = db.Column(db.DECIMAL(20, 4), comment=u"本周参与交易账户数（万）")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockStkAccount %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 股东人数
class StockStkHolderNumber(db.Model):
    __tablename__ = 'stock_stk_holder_number'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    ann_date = db.Column(db.Date, index=True, comment=u"公告日期")
    ann_date_str = db.Column(db.String(50), comment=u"公告日期")
    end_date = db.Column(db.String(50), comment=u"截止日期")
    holder_num = db.Column(db.DECIMAL(20, 4), comment=u"股东户数")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockStkHolderNumber %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 股东增减持
class StockStkHolderTrade(db.Model):
    __tablename__ = 'stock_stk_holder_trade'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    ann_date = db.Column(db.Date, index=True, comment=u"公告日期")
    ann_date_str = db.Column(db.String(50), comment=u"公告日期")
    holder_name = db.Column(db.String(100), comment=u"股东名称")
    holder_type = db.Column(db.String(50), comment=u"股东类型G高管P个人C公司")
    in_de = db.Column(db.String(100), comment=u"类型IN增持DE减持")
    change_vol = db.Column(db.DECIMAL(20, 4), comment=u"变动数量")
    change_ratio = db.Column(db.DECIMAL(20, 4), comment=u"占流通比例（%）")
    after_share = db.Column(db.DECIMAL(20, 4), comment=u"变动后持股")
    after_ratio = db.Column(db.DECIMAL(20, 4), comment=u"变动后占流通比例（%）")
    avg_price = db.Column(db.DECIMAL(20, 4), comment=u"平均价格")
    total_share = db.Column(db.DECIMAL(20, 4), comment=u"持股总数")
    begin_date = db.Column(db.String(50), comment=u"增减持开始日期")
    close_date = db.Column(db.String(50), comment=u"增减持结束日期")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockStkHolderTrade %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 新闻数据
# 电影月度票房
class StockBoMonthly(db.Model):
    __tablename__ = 'stock_bo_monthly'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), comment=u"影片名称")
    date = db.Column(db.String(50), index=True, comment=u"日期")
    list_date = db.Column(db.Date, index=True, comment=u"上映日期")
    list_date_str = db.Column(db.String(50), comment=u"上映日期")
    avg_price = db.Column(db.DECIMAL(20, 4), comment=u"平均票价")
    month_amount = db.Column(db.DECIMAL(20, 4), comment=u"当月票房（万）")
    list_day = db.Column(db.Integer, comment=u"月内天数")
    p_pc = db.Column(db.Integer, comment=u"场均人次")
    wom_index = db.Column(db.DECIMAL(20, 4), comment=u"口碑指数")
    m_ratio = db.Column(db.DECIMAL(20, 4), comment=u"月度占比（%）")
    rank = db.Column(db.DECIMAL(20, 4), comment=u"排名")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockBoMonthly %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 电影周度票房
class StockBoWeekly(db.Model):
    __tablename__ = 'stock_bo_weekly'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), comment=u"影片名称")
    date = db.Column(db.Date, index=True, comment=u"上映日期")
    date_str = db.Column(db.String(50), comment=u"上映日期")
    avg_price = db.Column(db.DECIMAL(20, 4), comment=u"平均票价")
    week_amount = db.Column(db.DECIMAL(20, 4), comment=u"当周票房（万）")
    total = db.Column(db.DECIMAL(20, 4), comment=u"累计票房（万）")
    list_day = db.Column(db.Integer, comment=u"上映天数")
    p_pc = db.Column(db.Integer, comment=u"场均人次")
    wom_index = db.Column(db.DECIMAL(20, 4), comment=u"口碑指数")
    up_ratio = db.Column(db.DECIMAL(20, 4), comment=u"环比变化(%)")
    rank = db.Column(db.Integer, comment=u"排名")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockBoWeekly %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 电影日度票房
class StockBoDaily(db.Model):
    __tablename__ = 'stock_bo_daily'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), comment=u"影片名称")
    date = db.Column(db.Date, index=True, comment=u"上映日期")
    date_str = db.Column(db.String(50), comment=u"上映日期")
    avg_price = db.Column(db.DECIMAL(20, 4), comment=u"平均票价")
    day_amount = db.Column(db.DECIMAL(20, 4), comment=u"当日票房（万）")
    total = db.Column(db.DECIMAL(20, 4), comment=u"累计票房（万）")
    list_day = db.Column(db.Integer, comment=u"上映天数")
    p_pc = db.Column(db.Integer, comment=u"场均人次")
    wom_index = db.Column(db.DECIMAL(20, 4), comment=u"口碑指数")
    up_ratio = db.Column(db.DECIMAL(20, 4), comment=u"环比变化(%)")
    rank = db.Column(db.Integer, comment=u"排名")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockBoDaily %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 影院每日票房
class StockBoCinema(db.Model):
    __tablename__ = 'stock_bo_cinema'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), comment=u"影院名称")
    aud_count = db.Column(db.Integer, comment=u"观众人数")
    att_ratio = db.Column(db.DECIMAL(20, 4), comment=u"上座率")
    date = db.Column(db.Date, index=True, comment=u"日期")
    date_str = db.Column(db.String(50), comment=u"日期")
    day_amount = db.Column(db.DECIMAL(20, 4), comment=u"当日票房（万）")
    day_showcount = db.Column(db.DECIMAL(20, 4), comment=u"当日场次（万）")
    avg_price = db.Column(db.DECIMAL(20, 4), comment=u"场均票价（元）")
    p_pc = db.Column(db.DECIMAL(20, 4), comment=u"场均人次")
    rank = db.Column(db.Integer, comment=u"排名")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockBoCinema %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 新闻资讯
class StockNews(db.Model):
    __tablename__ = 'stock_news'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, index=True, comment=u"新闻时间")
    date_str = db.Column(db.String(50), comment=u"新闻时间")
    channels = db.Column(db.String(50), comment=u"分类")
    title = db.Column(db.String(200), comment=u"标题")
    content = db.Column(db.TEXT, comment=u"内容")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockNews %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 新闻联播
class StockCctvNews(db.Model):
    __tablename__ = 'stock_cctv_news'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, index=True, comment=u"新闻时间")
    date_str = db.Column(db.String(50), comment=u"新闻时间")
    channels = db.Column(db.String(50), comment=u"分类")
    title = db.Column(db.String(200), comment=u"标题")
    content = db.Column(db.TEXT, comment=u"内容")
    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockCctvNews %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()


# 上市公司公告(信息地雷)
class StockAnns(db.Model):
    __tablename__ = 'stock_anns'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(30), index=True, comment=u"TS代码")
    code = db.Column(db.String(30), index=True, comment=u"股票代码")
    name = db.Column(db.String(50), comment=u"股票名称")
    ann_date = db.Column(db.Date, index=True, comment=u"公告日期")
    ann_date_str = db.Column(db.String(50), comment=u"公告日期")

    ann_type = db.Column(db.String(50), index=True, comment=u"公告类型")
    title = db.Column(db.String(200), comment=u"公告标题")
    content = db.Column(db.TEXT, comment=u"公告内容")
    pub_time = db.Column(db.String(50), comment=u"公告发布时间")

    createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
    updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')

    def __repr__(self):
        return '<StockAnns %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()