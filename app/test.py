# coding:utf-8
from sqlalchemy import create_engine
import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt

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

df = ts.get_report_data(2014,3)
#df = ts.get_stock_basics()
print(df)
#engine = create_engine('mysql://root:123456@127.0.0.1/stock?charset=utf8')

# 存入数据库
#df.to_sql('tick_data',engine)

# 追加数据到现有表
# df.to_sql('tick_data', engine, if_exists='append')
#df.to_sql('tick_data',engine,if_exists='append')