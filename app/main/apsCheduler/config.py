# coding = utf-8
# @Time    : 2018/3/27 0027 23:33
# @Author  : Carl
# @Site    : 
# @File    : config.py
# @Software: PyCharm
from apscheduler.schedulers.background import BackgroundScheduler

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

# The "apscheduler." prefix is hard coded
# schedulers = BackgroundScheduler({
#     'apscheduler.jobstores.default': {
#         'type': 'sqlalchemy',
#         'url': 'mysql+mysqldb://root:123456@localhost:3306/finance?charset=utf8'
#     },
#     'apscheduler.executors.default': {
#         'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
#         'max_workers': '20'
#     },
#     'apscheduler.executors.processpool': {
#         'type': 'processpool',
#         'max_workers': '5'
#     },
#     'apscheduler.job_defaults.coalesce': 'false',
#     'apscheduler.job_defaults.max_instances': '3',
#     'apscheduler.timezone': 'UTC',
# })


import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.events import EVENT_JOB_MAX_INSTANCES, EVENT_JOB_ERROR, EVENT_JOB_MISSED
from config import DevelopmentConfig

def err_listener(ev):
    msg = ''
    if ev.code == EVENT_JOB_ERROR:
        msg = ev.traceback
    elif ev.code == EVENT_JOB_MISSED:
        msg = 'missed job, job_id:%s, schedule_run_time:%s' % (ev.job_id, ev.scheduled_run_time)
    elif ev.code == EVENT_JOB_MAX_INSTANCES:
        msg = 'reached maximum of running instances, job_id:%s' % (ev.job_id)


jobstores = {
    'default': SQLAlchemyJobStore(url=DevelopmentConfig.SQLALCHEMY_DATABASE_URI)
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(10)
}
job_defaults = {
    'coalesce': True,
    'max_instances': 1
}

tz = pytz.timezone('Asia/Shanghai')
schedulers = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=tz, daemonic=False)
schedulers.add_listener(err_listener, EVENT_JOB_MAX_INSTANCES | EVENT_JOB_MISSED | EVENT_JOB_ERROR)
schedulers.start()






