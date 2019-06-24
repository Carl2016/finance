# coding:utf-8
import psutil, time, datetime
import gevent

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


########
# 获取开机以来 接收/发送 的字节数
# 依赖: psutil 库
# 参数(sent): Ture--返回发送的字节数 , False--不返回
# 参数(recv): Ture--返回接收的字节数 , False--不返回
# 两个参数都为(True): 返回包含 接收/发送 字节数的列表
# 函数失败返回: None
def io_get_bytes(sent=False, recv=False):
    internet = psutil.net_io_counters()  # 获取与网络IO相关的信息
    if internet == None:                 # 如果获取IO信息失败
        return None
    io_sent = internet.bytes_sent        # 开机以来发送的所有字节数
    io_recv = internet.bytes_recv        # 开机以来接收的所有字节数
    if sent == True and recv == True:
        return [io_sent, io_recv]
    elif sent == True:
        return io_sent
    elif recv == True:
        return io_recv
    else:
        return None


# 获取系统下载、上载速度
def get_network(interval, type):
    k = 1024  # K 所包含的字节数
    m = 1024 * 1024  # M 所包含的字节数
    byteSent1 = io_get_bytes(sent=True)  # 获取开机以来上传的字节数
    byteRecv1 = io_get_bytes(recv=True)  # 获取开机以来下载的字节数
    gevent.sleep(1)  # 间隔 interval 秒
    byteSent2 = io_get_bytes(sent=True)  # 再次获取开机以来上传的字节数
    byteRecv2 = io_get_bytes(recv=True)  # 再次获取开机以来下载的字节数
    sent = byteSent2 - byteSent1  # interval 秒内所获取的上传字节数
    recv = byteRecv2 - byteRecv1  # interval 秒内所获取的下载字节数
    # 转换成KB
    if type == 'M':  # 字节数达到 m 级别时以 M 作为单位
        sent = round(sent / m, 2)
        recv = round(recv / m, 2)
    if type == 'K':  # 字节数达到 k 级别时以 K 作为单位
        sent = round(sent / k, 2)
        recv = round(recv / k, 2)
    return [recv, sent]