# coding:utf-8
from sqlalchemy import create_engine
import tushare as ts
import json
from werkzeug.security import generate_password_hash, check_password_hash
import pandas as pd

import time
import os
import psutil

# # %% 获取中国平安三年内K线数据
# ZGPA = ts.get_hist_data('000001')
# ZGPA.index = pd.to_datetime(ZGPA.index)
# print(ZGPA.index)
# # %% 相关指数
# print(ZGPA.tail())
# plt.plot(ZGPA['close'], label='收盘价')
# plt.plot(ZGPA['ma5'], label='MA5')
# plt.plot(ZGPA['ma20'], label='MA20')
# plt.legend()
# plt.xlabel('日期')
# plt.ylabel('股价')
# plt.title('中国平安收盘价，MA5，MA20时间序列')

#df = ts.get_report_data(2014,3)
# df = ts.get_hist_data('600848') #一次性获取全部日k线数据
# dd = json.loads(df.to_json(orient='records'))
# #df = ts.get_stock_basics()
# print(dd[0]['open'])
# #(dd[0]['open'])
# engine = create_engine('mysql+pymysql://root:123456@127.0.0.1/stock?charset=utf8')
#
# # 存入数据库
# df.to_sql('tick_data', engine)

# 追加数据到现有表
#df.to_sql('tick_data', engine, if_exists='append')
#df.to_sql('tick_data', engine, if_exists='append')

# pro = ts.pro_api('9fa73a58ea99ddfe8fa4a2cf2b9b265a486ea47f50376d7226faab40')
#
# df = pro.daily_basic(ts_code='', trade_date='20180726', fields='ts_code,trade_date,turnover_rate,volume_ratio,pe,pb')
#
# #df = pro.query('daily_basic', ts_code='', trade_date='20180726', fields='ts_code,trade_date,turnover_rate,volume_ratio,pe,pb')
#
#
# dd = json.loads(df.to_json(orient='records'))
#
# print(dd[0]['ts_code'])

# admin = generate_password_hash('admin')
# print(admin)