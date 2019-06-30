# coding:utf-8
from gevent import monkey
monkey.patch_socket

import multiprocessing

debug = False
# 并行工作进程数
workers = multiprocessing.cpu_count() * 2 + 1
# 指定每个工作者的线程数
#threads = 2
# 监听内网端口5000
bind = '127.0.0.1:5000'
# 设置守护进程,将进程交给supervisor管理
daemon = 'false'
# 工作模式协程
worker_class = 'gunicorn.workers.ggevent.GeventWorker'
# 设置最大并发量
worker_connections = 2000
# 设置进程文件目录
pidfile = '/var/run/gunicorn.pid'
# 设置访问日志和错误信息日志路径
accesslog = '/data/logs/gunicorn_acess.log'
errorlog = '/data/logs/gunicorn_error.log'

x_forwarded_for_header = 'X-FORWARDED-FOR'
# 设置日志记录水平
loglevel = 'warning'
