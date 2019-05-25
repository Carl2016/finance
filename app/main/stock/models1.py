# # coding:utf-8
# from exts import db, db_base
# from sqlalchemy.sql import func
#
#
# # 股票列表
# # 基本面数据
# class Stock(db.Model):
#     __tablename__ = 'stock_details'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(20), index=True, unique=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(30), nullable=False, comment=u"股票名称")
#     industry = db.Column(db.String(30), comment=u"所属行业")
#     area = db.Column(db.String(30), comment=u"地区")
#     pe = db.Column(db.DECIMAL(20,  4), comment=u"市盈率")
#     outStanding = db.Column(db.DECIMAL(20,  4), comment=u"流通股本(亿)")
#     totals = db.Column(db.DECIMAL(20,  4), comment=u"总股本(亿)")
#     totalAssets = db.Column(db.DECIMAL(20,  4), comment=u"总资产(万)")
#     liquidAssets = db.Column(db.DECIMAL(20,  4), comment=u"流动资产")
#     fixedAssets = db.Column(db.DECIMAL(20,  4), comment=u"固定资产")
#     reserved = db.Column(db.DECIMAL(20,  4), comment=u"公积金")
#     reservedPerShare = db.Column(db.DECIMAL(20,  4), comment=u"每股公积金")
#     esp = db.Column(db.DECIMAL(20,  4), comment=u"每股收益")
#     bvps = db.Column(db.DECIMAL(20,  4), comment=u"每股净资")
#     pb = db.Column(db.DECIMAL(20,  4), comment=u"市净率")
#     timeToMarketDateTime = db.Column(db.DateTime, index=True, comment=u"上市日期时间")
#     timeToMarket = db.Column(db.String(20), comment=u"上市日期")
#     undp = db.Column(db.DECIMAL(20,  4), comment=u"未分利润")
#     perundp = db.Column(db.DECIMAL(20,  4), comment=u"每股未分配")
#     rev = db.Column(db.DECIMAL(20,  4), comment=u"收入同比(%)")
#     profit = db.Column(db.DECIMAL(20,  4), comment=u"利润同比(%)")
#     gpr = db.Column(db.DECIMAL(20,  4), comment=u"毛利率(%)")
#     npr = db.Column(db.DECIMAL(20,  4), comment=u"净利润率(%)")
#     holders = db.Column(db.INTEGER, comment=u"股东人数")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
#
#
# # 股票行业分类
# class IndustryCategory(db.Model):
#     __tablename__ = 'stock_industry_category'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), unique=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#     cName = db.Column(db.String(50), nullable=False, comment=u"行业名称")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<IndustryCategory %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 股票概念分类
# class ConceptCategory(db.Model):
#     __tablename__ = 'stock_concept_category'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), unique=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#     cName = db.Column(db.String(50), nullable=False, comment=u"行业名称")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<ConceptCategory %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 股票地域分类
# class AreaCategory(db.Model):
#     __tablename__ = 'stock_area_category'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), unique=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#     area = db.Column(db.String(50), nullable=False, comment=u"地域名称")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<AreaCategory %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 股票 中小板分类
# class SmallBoardCategory(db.Model):
#     __tablename__ = 'stock_small_board_category'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), unique=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<SmallBoardCategory %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 股票 创业板分类
# class GemCategory(db.Model):
#     __tablename__ = 'stock_gem_category'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), unique=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<GemCategory %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 股票风险警示板分类
# class RiskWarningCategory(db.Model):
#     __tablename__ = 'stock_risk_warning_category'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), unique=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<RiskWarningCategory %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 沪深300成份及权重
# class Hs300Weights(db.Model):
#     __tablename__ = 'stock_hs_weights'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), unique=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#
#     dateTime = db.Column(db.DateTime, index=True, comment=u"权重时间")
#     date = db.Column(db.String(20), nullable=False, comment=u"日期")
#     weight = db.Column(db.DECIMAL(20,  4), nullable=False, comment=u"权重")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<Hs300Weights %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 上证50成份股
# class Sz50Weights(db.Model):
#     __tablename__ = 'stock_sz_weights'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), unique=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<Sz50Weights %r>' % self.code
#
#
# # 中证500成份股
# class Zz500Weights(db.Model):
#     __tablename__ = 'stock_zz_weights'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), unique=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<Zz500Weights %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 终止上市股票列表
# class TerminateListing(db.Model):
#     __tablename__ = 'stock_terminate_listing'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), unique=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#     oDate = db.Column(db.String(20), comment=u"上市日期")
#     tDate = db.Column(db.String(20), comment=u"终止上市日期")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<TerminateListing %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 暂停上市股票列表
# class PauseListing(db.Model):
#     __tablename__ = 'stock_pause_listing'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), unique=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#     oDate = db.Column(db.String(20), comment=u"上市日期")
#     tDate = db.Column(db.String(20), comment=u"暂停上市日期")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<PauseListing %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 股票业绩报告
# class Results(db.Model):
#     __tablename__ = 'stock_results'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#     eps = db.Column(db.DECIMAL(20, 4), comment=u"每股收益")
#     bvps = db.Column(db.DECIMAL(20, 4), comment=u"每股净资")
#     epsYoy = db.Column(db.DECIMAL(20, 4), comment=u"每股收益同比(%)")
#     roe = db.Column(db.DECIMAL(20, 4), comment=u"净资产收益率(%)")
#     epcf = db.Column(db.DECIMAL(20, 4), comment=u"每股现金流量(元)")
#     netProfits = db.Column(db.DECIMAL(20, 4), comment=u"净利润(万元)")
#     profitsYoy = db.Column(db.DECIMAL(20, 4), comment=u"净利润同比(%)")
#     distrib = db.Column(db.String(30), comment=u"分配方案")
#     reportDate = db.Column(db.String(20), comment=u"发布日期")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<Results %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 股票盈利能力
# class Profit(db.Model):
#     __tablename__ = 'stock_profit'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#     year = db.Column(db.String(4), index=True, nullable=False, comment=u"年份")
#     month = db.Column(db.String(2), index=True, nullable=False, comment=u"月份")
#     date = db.Column(db.Date, nullable=False, comment=u"时间")
#     roe = db.Column(db.DECIMAL(20, 4), comment=u"净资产收益率(%)")
#     netProfitRatio = db.Column(db.DECIMAL(20, 4), comment=u"净利率(%)")
#     esp = db.Column(db.DECIMAL(20, 4), comment=u"每股收益")
#     grossProfitRate = db.Column(db.DECIMAL(20, 4), comment=u"毛利率(%)")
#     netProfits = db.Column(db.DECIMAL(20, 4), comment=u"净利润(万元)")
#     businessIncome = db.Column(db.DECIMAL(20, 4), comment=u"营业收入(百万元)")
#     bips = db.Column(db.DECIMAL(20, 4), comment=u"每股主营业务收入(元)")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<Profit %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 股票运营能力
# class Operating(db.Model):
#     __tablename__ = 'stock_operating'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#     year = db.Column(db.String(4), index=True, nullable=False, comment=u"年份")
#     month = db.Column(db.String(2), index=True, nullable=False, comment=u"月份")
#     date = db.Column(db.Date, nullable=False, comment=u"时间")
#     arturnOver = db.Column(db.DECIMAL(20, 4), comment=u"应收账款周转率(次)")
#     arturnDays = db.Column(db.DECIMAL(20, 4), comment=u"应收账款周转天数(天)")
#     inventoryTurnover = db.Column(db.DECIMAL(20, 4), comment=u"存货周转率(次)")
#     inventoryDays = db.Column(db.DECIMAL(20, 4), comment=u"存货周转天数(天)")
#     currentAssetTurnover = db.Column(db.DECIMAL(20, 4), comment=u"流动资产周转率(次)")
#     currentAssetDays = db.Column(db.DECIMAL(20, 4), comment=u"流动资产周转天数(天)")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<Operating %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 股票成长能力
# class Growth(db.Model):
#     __tablename__ = 'stock_growth'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#     year = db.Column(db.String(4), index=True, nullable=False, comment=u"年份")
#     month = db.Column(db.String(2), index=True, nullable=False, comment=u"月份")
#     date = db.Column(db.Date, nullable=False, comment=u"时间")
#     mbrg = db.Column(db.DECIMAL(20, 4), comment=u"主营业务收入增长率(%)")
#     nprg = db.Column(db.DECIMAL(20, 4), comment=u"净利润增长率(%)")
#     nav = db.Column(db.DECIMAL(20, 4), comment=u"净资产增长率")
#     targ = db.Column(db.DECIMAL(20, 4), comment=u"总资产增长率")
#     epsg = db.Column(db.DECIMAL(20, 4), comment=u"每股收益增长率")
#     seg = db.Column(db.DECIMAL(20, 4), comment=u"股东权益增长率")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<Growth %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 股票偿债能力
# class Solvency(db.Model):
#     __tablename__ = 'stock_solvency'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#     year = db.Column(db.String(4), index=True, nullable=False, comment=u"年份")
#     month = db.Column(db.String(2), index=True, nullable=False, comment=u"月份")
#     date = db.Column(db.Date, nullable=False, comment=u"时间")
#     currentRatio = db.Column(db.DECIMAL(20, 4), comment=u"流动比率")
#     quickRatio = db.Column(db.DECIMAL(20, 4), comment=u"速动比率")
#     cashRatio = db.Column(db.DECIMAL(20, 4), comment=u"现金比率")
#     icRatio = db.Column(db.DECIMAL(20, 4), comment=u"利息支付倍数")
#     sheqRatio = db.Column(db.DECIMAL(20, 4), comment=u"股东权益比率")
#     adRatio = db.Column(db.DECIMAL(20, 4), comment=u"股东权益增长率")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<Solvency %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 股票现金流量
# class CashFlow(db.Model):
#     __tablename__ = 'stock_cash_flow'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#     year = db.Column(db.String(4), index=True, nullable=False, comment=u"年份")
#     month = db.Column(db.String(2), index=True, nullable=False, comment=u"月份")
#     date = db.Column(db.Date, nullable=False, comment=u"时间")
#     cfSales = db.Column(db.DECIMAL(20,  4), comment=u"经营现金净流量对销售收入比率")
#     rateOfReturn = db.Column(db.DECIMAL(20, 4), comment=u"资产的经营现金流量回报率")
#     cfNm = db.Column(db.DECIMAL(20, 4), comment=u"经营现金净流量与净利润的比率")
#     cfLiabilities = db.Column(db.DECIMAL(20, 4), comment=u"经营现金净流量对负债比率")
#     cashFlowRatio = db.Column(db.DECIMAL(20, 4), comment=u"现金流量比率")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<CashFlow %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 交易数据
# # 股票历史行情
# class HistoricalQuotes(db.Model):
#     __tablename__ = 'stock_historical_quotes'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#
#     date = db.Column(db.String(20), comment=u"日期")
#     open = db.Column(db.DECIMAL(20, 4), comment=u"开盘价")
#     high = db.Column(db.DECIMAL(20, 4), comment=u"最高价")
#     close = db.Column(db.DECIMAL(20, 4), comment=u"收盘价")
#     low = db.Column(db.DECIMAL(20, 4), comment=u"最低价")
#     volume = db.Column(db.DECIMAL(20, 4), comment=u"成交量")
#     priceChange = db.Column(db.DECIMAL(20, 4), comment=u"价格变动")
#     pChange = db.Column(db.DECIMAL(20, 4), comment=u"涨跌幅")
#     ma5 = db.Column(db.DECIMAL(20, 4), comment=u"5日均价")
#     ma10 = db.Column(db.DECIMAL(20, 4), comment=u"10日均价")
#     ma20 = db.Column(db.DECIMAL(20, 4), comment=u"20日均价")
#     vMa5 = db.Column(db.DECIMAL(20, 4), comment=u"5日均量")
#     vMa10 = db.Column(db.DECIMAL(20, 4), comment=u"10日均量")
#     vMa20 = db.Column(db.DECIMAL(20, 4), comment=u"20日均量")
#     turnover = db.Column(db.DECIMAL(20, 4), comment=u"换手率[注：指数无此项]")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<HistoricalQuotes %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 股票复权数据
# class RecoverData(db.Model):
#     __tablename__ = 'stock_recover_data'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#
#     date = db.Column(db.String(30), comment=u"交易日期 (index)")
#     open = db.Column(db.DECIMAL(20, 4), comment=u"开盘价")
#     high = db.Column(db.DECIMAL(20, 4), comment=u"最高价")
#     close = db.Column(db.DECIMAL(20, 4), comment=u"收盘价")
#     low = db.Column(db.DECIMAL(20, 4), comment=u"收盘价")
#     volume = db.Column(db.INTEGER, comment=u"成交量")
#     amount = db.Column(db.DECIMAL(20, 4), comment=u"成交金额")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<RecoverData %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 股票实时行情
# class RealTimeMarket(db.Model):
#     __tablename__ = 'stock_real_time_market'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#
#     changePercent = db.Column(db.DECIMAL(20,  4), comment=u"涨跌幅")
#     trade = db.Column(db.DECIMAL(20, 4), comment=u"现价")
#     open = db.Column(db.DECIMAL(20, 4), comment=u"开盘价")
#     high = db.Column(db.DECIMAL(20, 4), comment=u"最高价")
#     low = db.Column(db.DECIMAL(20, 4), comment=u"最低价")
#     settlement = db.Column(db.DECIMAL(20, 4), comment=u"昨日收盘价")
#     volume = db.Column(db.INTEGER, comment=u"成交量")
#     turnoverRatio = db.Column(db.DECIMAL(20, 4), comment=u"换手率")
#     amount = db.Column(db.INTEGER, comment=u"成交金额")
#     per = db.Column(db.DECIMAL(20, 4), comment=u"市盈率")
#     pb = db.Column(db.DECIMAL(20, 4), comment=u"市净率")
#     mktcap = db.Column(db.DECIMAL(20, 4), comment=u"总市值")
#     nmc = db.Column(db.DECIMAL(20, 4), comment=u"流通市值")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<RealTimeMarket %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 股票历史分笔
# class HistoryPen(db.Model):
#     __tablename__ = 'stock_history_pen'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), index=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#
#     dateTime = db.Column(db.DateTime, index=True, comment=u"当日时间")
#     time = db.Column(db.String(30), comment=u"当日时间字符串")
#     price = db.Column(db.DECIMAL(20, 4), comment=u"成交价格")
#     change = db.Column(db.String(30), comment=u"价格变动")
#     volume = db.Column(db.INTEGER, comment=u"成交手")
#     amount = db.Column(db.DECIMAL(20, 4), comment=u"成交金额(元)")
#     type = db.Column(db.String(20), comment=u"买卖类型【买盘、卖盘、中性盘】")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<HistoryPen %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 股票实时分笔
# class RealTimePen(db.Model):
#     __tablename__ = 'stock_real_time_pen'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#
#     open = db.Column(db.DECIMAL(20,  4), comment=u"开盘价")
#     preClose = db.Column(db.DECIMAL(20, 4), comment=u"昨日收盘价")
#     price = db.Column(db.DECIMAL(20, 4), comment=u"当前价格")
#     high = db.Column(db.DECIMAL(20, 4), comment=u"今日最高价")
#     low = db.Column(db.DECIMAL(20, 4), comment=u"今日最低价")
#     bid = db.Column(db.DECIMAL(20,  4), comment=u"竞买价，即“买一”报价")
#     ask = db.Column(db.INTEGER, comment=u"竞卖价，即“卖一”报价")
#     volume = db.Column(db.DECIMAL(20,  4), comment=u"成交量 maybe you need do volume/100")
#     amount = db.Column(db.INTEGER, comment=u"成交金额（元 CNY）")
#     b1Volume = db.Column(db.DECIMAL(20,  4), comment=u"委买一（笔数 bid volume）")
#     b1Price = db.Column(db.DECIMAL(20,  4), comment=u"委卖一（价格 bid price）")
#     b2Volume = db.Column(db.DECIMAL(20,  4), comment=u"委买二（笔数 bid volume）")
#     b2Price = db.Column(db.DECIMAL(20,  4), comment=u"委买二（价格 bid price）")
#     b3Volume = db.Column(db.DECIMAL(20,  4), comment=u"委买三（笔数 bid volume）")
#     b3Price = db.Column(db.DECIMAL(20,  4), comment=u"委买三（价格 bid price）")
#     b4Volume = db.Column(db.DECIMAL(20,  4), comment=u"委买四（笔数 bid volume）")
#     b4Price = db.Column(db.DECIMAL(20,  4), comment=u"委买四（价格 bid price）")
#     b5Volume = db.Column(db.DECIMAL(20,  4), comment=u"委买五（笔数 bid volume）")
#     b5Price = db.Column(db.DECIMAL(20,  4), comment=u"委买五（价格 bid price）")
#     a1Volume = db.Column(db.DECIMAL(20,  4), comment=u"委卖一（笔数 ask volume）")
#     a1Price = db.Column(db.DECIMAL(20,  4), comment=u"委卖一（价格 bid price）")
#     a2Volume = db.Column(db.DECIMAL(20,  4), comment=u"委卖二（笔数 ask volume）")
#     a2Price = db.Column(db.DECIMAL(20,  4), comment=u"委卖二（价格 bid price）")
#     a3Volume = db.Column(db.DECIMAL(20,  4), comment=u"委卖三（笔数 ask volume）")
#     a3Price = db.Column(db.DECIMAL(20,  4), comment=u"委卖三（价格 bid price）")
#     a4Volume = db.Column(db.DECIMAL(20,  4), comment=u"委卖四（笔数 ask volume）")
#     a4Price = db.Column(db.DECIMAL(20,  4), comment=u"委卖四（价格 bid price）")
#     a5Volume = db.Column(db.DECIMAL(20,  4), comment=u"委卖五（笔数 ask volume）")
#     a5Price = db.Column(db.DECIMAL(20,  4), comment=u"委卖五（价格 bid price）")
#     dateTime = db.Column(db.DateTime, comment=u"当日时间")
#     date = db.Column(db.String(20), comment=u"日期")
#     time = db.Column(db.String(20), comment=u"时间")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<RealTimePen %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 股票当日历史分笔
# class TodayHistoryPen(db.Model):
#     __tablename__ = 'stock_today_history_pen'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#
#     dateTime = db.Column(db.DateTime, comment=u"当日时间")
#     time = db.Column(db.String(30), comment=u"时间")
#     price = db.Column(db.DECIMAL(20,  4), comment=u"当前价格")
#     pChange = db.Column(db.DECIMAL(20,  4), comment=u"涨跌幅")
#     change = db.Column(db.DECIMAL(20,  4), comment=u"价格变动")
#     volume = db.Column(db.INTEGER, comment=u"成交手")
#     amount = db.Column(db.DECIMAL(20,  4), comment=u"成交金额(元)")
#     type = db.Column(db.String(30), comment=u"买卖类型【买盘、卖盘、中性盘】")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<TodayHistoryPen %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 股票大盘指数行情列表
# class MarketIndex(db.Model):
#     __tablename__ = 'stock_market_index'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), unique=True, nullable=False, comment=u"大盘指数代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"大盘指数名称")
#
#     change = db.Column(db.DECIMAL(20,  4), comment=u"涨跌幅")
#     open = db.Column(db.DECIMAL(20,  4), comment=u"开盘点位")
#     preClose = db.Column(db.DECIMAL(20,  4), comment=u"昨日收盘点位")
#     close = db.Column(db.DECIMAL(20,  4), comment=u"收盘点位")
#
#     high = db.Column(db.DECIMAL(20,  4), comment=u"最高点位")
#     low = db.Column(db.DECIMAL(20,  4), comment=u"最低点位")
#     volume = db.Column(db.DECIMAL(20,  4), comment=u"成交量(手)")
#     amount = db.Column(db.DECIMAL(20,  4), comment=u"成交金额（亿元）")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<MarketIndex %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 股票大单交易数据
# class BigSingleTransactionData(db.Model):
#     __tablename__ = 'stock_big_single_transaction_data'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), unique=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#
#     dateTime = db.Column(db.DateTime, comment=u"当日时间")
#     time = db.Column(db.DateTime, comment=u"时间")
#     price = db.Column(db.DECIMAL(20,  4), comment=u"当前价格")
#     volume = db.Column(db.INTEGER, comment=u"成交手")
#     prePrice = db.Column(db.DECIMAL(20,  4), comment=u"上一笔价格")
#     type = db.Column(db.String(30), comment=u"买卖类型【买盘、卖盘、中性盘】")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<BigSingleTransactionData %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 股票分配预案
# class DistributionPlan(db.Model):
#     __tablename__ = 'stock_distribution_plan'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), unique=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#
#     dateTime = db.Column(db.DateTime, comment=u"分配预案时间")
#     year = db.Column(db.String(10), comment=u"分配年份")
#     reportDate = db.Column(db.DateTime, comment=u"公布日期")
#     divi = db.Column(db.DECIMAL(20,  4), comment=u"分红金额（每10股）")
#     shares = db.Column(db.INTEGER, comment=u"转增和送股数（每10股）")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<DistributionPlan %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 股票业绩预告
# class PerformanceNotice(db.Model):
#     __tablename__ = 'stock_performance_notice'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), unique=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#
#     dateTime = db.Column(db.DateTime, comment=u"业绩预告时间")
#     type = db.Column(db.String(10), comment=u"业绩变动类型【预增、预亏等】")
#     reportDate = db.Column(db.DateTime, comment=u"发布日期")
#     preEps = db.Column(db.DECIMAL(20,  4), comment=u"上年同期每股收益")
#     range = db.Column(db.String(30), comment=u"业绩变动范围")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<PerformanceNotice %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 股票限售股解禁
# class RestrictedSharesLifted(db.Model):
#     __tablename__ = 'stock_restricted_shares_lifted'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), unique=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#
#     dateTime = db.Column(db.DateTime, comment=u"限售股解禁时间")
#     date = db.Column(db.String(20), comment=u"解禁日期")
#     count = db.Column(db.DECIMAL(20,  4), comment=u"解禁数量（万股）")
#     ratio = db.Column(db.DECIMAL(20,  4), comment=u"占总盘比率")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<RestrictedSharesLifted %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 股票基金持股
# class FundHoldings(db.Model):
#     __tablename__ = 'stock_fund_holdings'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), unique=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#
#     dateTime = db.Column(db.DateTime, comment=u"基金持股时间")
#     date = db.Column(db.String(20), comment=u"报告日期")
#     nums = db.Column(db.INTEGER, comment=u"基金家数")
#     nlast = db.Column(db.INTEGER, comment=u"与上期相比（增加或减少了）")
#     count = db.Column(db.DECIMAL(20,  4), comment=u"基金持股数（万股）")
#     clast = db.Column(db.DECIMAL(20,  4), comment=u"与上期相比")
#     amount = db.Column(db.DECIMAL(20,  4), comment=u"基金持股市值")
#     ratio = db.Column(db.DECIMAL(20,  4), comment=u"占流通盘比率")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<FundHoldings %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 股票新股数据
# class IpoData(db.Model):
#     __tablename__ = 'stock_ipo_data'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), unique=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(120), nullable=False, comment=u"股票名称")
#
#     ipoDateTime = db.Column(db.DateTime, comment=u"IPO时间")
#     issueDateTime = db.Column(db.DateTime, comment=u"上市时间")
#     ipoDate = db.Column(db.String(20), comment=u"上网发行日期")
#     issueDate = db.Column(db.String(20), comment=u"上市日期")
#     amount = db.Column(db.INTEGER, comment=u"发行数量(万股)")
#     markets = db.Column(db.INTEGER, comment=u"上网发行数量(万股)")
#     price = db.Column(db.DECIMAL(20,  4), comment=u"发行价格(元)")
#     pe = db.Column(db.DECIMAL(20,  4), comment=u"发行市盈率")
#     limit = db.Column(db.DECIMAL(20,  4), comment=u"个人申购上限(万股)")
#     funds = db.Column(db.DECIMAL(20,  4), comment=u"募集资金(亿元)")
#     ballot = db.Column(db.DECIMAL(20,  4), comment=u"网上中签率(%)")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<IpoData %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 股票融资融券（沪市）
# class ShMarginTrading(db.Model):
#     __tablename__ = 'stock_sh_margin_trading'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), unique=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#
#     dateTime = db.Column(db.DateTime, comment=u"交易日期时间")
#     opDate = db.Column(db.String(20), comment=u"信用交易日期")
#     rzye = db.Column(db.DECIMAL(20,  4), comment=u"本日融资余额(元)")
#     rzmre = db.Column(db.DECIMAL(20,  4), comment=u"本日融资买入额(元)")
#     rqyl = db.Column(db.INTEGER, comment=u"本日融券余量")
#     rqylje = db.Column(db.DECIMAL(20,  4), comment=u"本日融券余量金额(元)")
#     rqmcl = db.Column(db.INTEGER, comment=u"本日融券卖出量")
#     rzrqjyzl = db.Column(db.DECIMAL(20,  4), comment=u"本日融资融券余额(元)")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<ShMarginTrading %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 股票融资融券详细（沪市）
# class ShMarginTradingDetails(db.Model):
#     __tablename__ = 'stock_sh_margin_trading_details'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), unique=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#
#     dateTime = db.Column(db.DateTime, comment=u"融资融券详细时间")
#     opDate = db.Column(db.String(20), comment=u"信用交易日期")
#     stockCode = db.Column(db.String(30), comment=u"标的证券代码")
#     securityAbbr = db.Column(db.String(50), comment=u"标的证券简称")
#     rzye = db.Column(db.DECIMAL(20,  4), comment=u"本日融资余额(元)")
#     rzmre = db.Column(db.DECIMAL(20,  4), comment=u"本日融资买入额(元)")
#     rzche = db.Column(db.DECIMAL(20,  4), comment=u"本日融资偿还额(元)")
#     rqyl = db.Column(db.INTEGER, comment=u"本日融券余量")
#     rqmcl = db.Column(db.INTEGER, comment=u"本日融券卖出量")
#     rqchl = db.Column(db.INTEGER, comment=u"本日融券偿还量")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<ShMarginTradingDetails %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 股票融资融券（深市）
# class SzMarginTrading(db.Model):
#     __tablename__ = 'stock_sz_margin_trading'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), unique=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#
#     dateTime = db.Column(db.DateTime, comment=u"融资融券时间")
#     opDate = db.Column(db.String(20), comment=u"信用交易日期")
#     rzye = db.Column(db.DECIMAL(20,  4), comment=u"本日融资余额(元)")
#     rzmre = db.Column(db.DECIMAL(20,  4), comment=u"本日融资买入额(元)")
#     rqyl = db.Column(db.INTEGER, comment=u"本日融券余量")
#     rqye = db.Column(db.DECIMAL(20,  4), comment=u"本日融券余量(元)")
#     rqmcl = db.Column(db.INTEGER, comment=u"本日融券卖出量")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<SzMarginTrading %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 股票融资融券详细（深市）
# class SzMarginTradingDetails(db.Model):
#     __tablename__ = 'stock_sz_margin_trading_details'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), unique=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#
#     dateTime = db.Column(db.DateTime, comment=u"融资融券详细时间")
#     opDate = db.Column(db.String(20), comment=u"信用交易日期")
#     stockCode = db.Column(db.String(30), comment=u"标的证券代码")
#     securityAbbr = db.Column(db.String(30), comment=u"标的证券简称")
#     rzye = db.Column(db.DECIMAL(20,  4), comment=u"本日融资余额(元)")
#     rzmre = db.Column(db.DECIMAL(20,  4), comment=u"本日融资买入额(元)")
#     rqyl = db.Column(db.INTEGER, comment=u"本日融券余量")
#     rqye = db.Column(db.DECIMAL(20,  4), comment=u"本日融券余量(元)")
#     rqmcl = db.Column(db.INTEGER, comment=u"本日融券卖出量")
#     rzrqye = db.Column(db.DECIMAL(20,  4), comment=u"融资融券余额(元)")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<SzMarginTradingDetails %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 每日龙虎榜列表
# class DailyBillboard(db.Model):
#     __tablename__ = 'stock_daily_billboard'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), unique=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#
#     dateTime = db.Column(db.DateTime, comment=u"每日龙虎榜列表时间")
#     pChange = db.Column(db.FLOAT, comment=u"当日涨跌幅")
#     amount = db.Column(db.DECIMAL(20,  4), comment=u"龙虎榜成交额(万)")
#     buy = db.Column(db.DECIMAL(20,  4), comment=u"买入额(万)")
#     bRatio = db.Column(db.FLOAT, comment=u"买入占总成交比例")
#     sell = db.Column(db.DECIMAL(20,  4), comment=u"卖出额(万)")
#     sRatio = db.Column(db.FLOAT, comment=u"卖出占总成交比例")
#     reason = db.Column(db.String(150), comment=u"上榜原因")
#     date = db.Column(db.String(20), comment=u"日期")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<DailyBillboard %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 个股上榜统计
# class StockListCount(db.Model):
#     __tablename__ = 'stock_stock_list_count'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), unique=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#
#     dateTime = db.Column(db.DateTime, comment=u"个股上榜统计时间")
#     count = db.Column(db.INTEGER, comment=u"上榜次数")
#     bamount = db.Column(db.DECIMAL(20,  4), comment=u"累积购买额(万)")
#     samount = db.Column(db.DECIMAL(20,  4), comment=u"累积卖出额(万)")
#     net = db.Column(db.DECIMAL(20,  4), comment=u"净额(万)")
#     bcount = db.Column(db.INTEGER, comment=u"买入席位数")
#     scount = db.Column(db.INTEGER, comment=u"卖出席位数")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<StockListCount %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 营业部上榜统计
# class SalesDepartmentListCount(db.Model):
#     __tablename__ = 'stock_sales_department_list_count'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), unique=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(50), nullable=False, comment=u"股票名称")
#
#     dateTime = db.Column(db.DateTime, comment=u"营业部上榜统计时间")
#     broker = db.Column(db.String(100), comment=u"营业部名称")
#     count = db.Column(db.INTEGER, comment=u"上榜次数")
#     bamount = db.Column(db.DECIMAL(20,  4), comment=u"累积购买额(万)")
#     samount = db.Column(db.DECIMAL(20,  4), comment=u"累积卖出额(万)")
#     bcount = db.Column(db.INTEGER, comment=u"买入席位数")
#     scount = db.Column(db.INTEGER, comment=u"卖出席位数")
#     top3 = db.Column(db.TEXT, comment=u"买入前三股票")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<SalesDepartmentListCount %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 机构席位追踪
# class OrganizationSeatTracking(db.Model):
#     __tablename__ = 'stock_organization_seat_tracking'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), unique=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(120), nullable=False, comment=u"股票名称")
#
#     dateTime = db.Column(db.DateTime, comment=u"机构席位追踪时间")
#     bamount = db.Column(db.DECIMAL(20,  4), comment=u"累积买入额(万)")
#     bcount = db.Column(db.INTEGER, comment=u"买入次数")
#     samount = db.Column(db.DECIMAL(20,  4), comment=u"累积卖出额(万)")
#     scount = db.Column(db.INTEGER, comment=u"卖出次数")
#     net = db.Column(db.DECIMAL(20,  4), comment=u"净额(万)")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<OrganizationSeatTracking %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 机构成交明细
# class AgencyTurnoverDetails(db.Model):
#     __tablename__ = 'stock_agency_turnover_details'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     code = db.Column(db.String(30), unique=True, nullable=False, comment=u"股票代码")
#     name = db.Column(db.String(120), nullable=False, comment=u"股票名称")
#
#     dateTime = db.Column(db.DateTime, comment=u"机构成交明细时间")
#     date = db.Column(db.String(20), comment=u"交易日期")
#     bamount = db.Column(db.DECIMAL(20,  4), comment=u"机构席位买入额(万)")
#     samount = db.Column(db.DECIMAL(20,  4), comment=u"机构席位卖出额(万)")
#     type = db.Column(db.String(100), comment=u"类型")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<AgencyTurnoverDetails %r>' % self.code
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 新闻
# # 即时新闻
# class LatestNews(db.Model):
#     __tablename__ = 'article_latest_news'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     classify = db.Column(db.String(30), nullable=False, comment=u"新闻类别")
#     title = db.Column(db.String(120), nullable=False, comment=u"新闻标题")
#
#     dateTime = db.Column(db.DateTime, comment=u"发布时间")
#     time = db.Column(db.String(20), comment=u"发布时间")
#     url = db.Column(db.DECIMAL(20,  4), comment=u"新闻链接")
#     content = db.Column(db.DECIMAL(20,  4), comment=u"新闻内容（在show_content为True的情况下出现）")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<LatestNews %r>' % self.title
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 信息地雷
# class Notices(db.Model):
#     __tablename__ = 'article_notices'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String(120), nullable=False, comment=u"新闻标题")
#
#     dateTime = db.Column(db.DateTime, comment=u"发布时间")
#     date = db.Column(db.String(20), comment=u"公告日期")
#     type = db.Column(db.DECIMAL(20,  4), comment=u"信息类型")
#     url = db.Column(db.DECIMAL(20,  4), comment=u"信息内容URL")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<Notices %r>' % self.title
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# # 新浪股吧
# class GubaSina(db.Model):
#     __tablename__ = 'article_guba_sina'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String(120), nullable=False, comment=u"新闻标题")
#
#     ptime = db.Column(db.String(30), comment=u"发布时间")
#     rcounts = db.Column(db.INTEGER, comment=u"阅读次数")
#     content = db.Column(db.String(200), comment=u"消息内容（show_content=True的情况下）")
#     createTime = db.Column(db.DateTime, server_default=func.now(), comment=u"创建时间")
#     updateTime = db.Column(db.DateTime, server_default=func.now(), comment=u'修改时间')
#
#     def __repr__(self):
#         return '<GubaSina %r>' % self.title
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()