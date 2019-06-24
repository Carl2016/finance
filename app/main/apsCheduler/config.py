# coding = utf-8
# @Time    : 2018/3/27 0027 23:33
# @Author  : Carl
# @Site    : 
# @File    : config.py
# @Software: PyCharm
import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.redis import RedisJobStore
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
# jobstores = {
#     'default': RedisJobStore(db=1,
#                             jobs_key='apscheduler.jobs',
#                             run_times_key='apscheduler.run_times',
#                             host='127.0.0.1',
#                             port='6379',
#                             password='',
#     )
# }


executors = {
    'default': {'type': 'threadpool', 'max_workers': 20},
    'processpool': ProcessPoolExecutor(max_workers=10)
}

job_defaults = {
    'coalesce': True,
    'max_instances': 10
}

tz = pytz.timezone('Asia/Shanghai')
schedulers = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=tz, daemonic=False)
schedulers.add_listener(err_listener, EVENT_JOB_MAX_INSTANCES | EVENT_JOB_MISSED | EVENT_JOB_ERROR)
schedulers.start()






