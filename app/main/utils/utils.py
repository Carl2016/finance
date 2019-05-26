# coding:utf-8
import datetime


# date 参数是时间格式的时间， n是要计算前几个月
def getTheMonth(date, n):
    month = date.month
    year = date.year
    for i in range(n):
        if month == 1:
            year -= 1
            month = 12
        else:
            month -= 1
    return datetime.date(year, month, 1).strftime('%Y-%m-%d')
