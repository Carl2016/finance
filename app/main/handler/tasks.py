# coding = utf-8
# @Time    : 2018/1/30 0030 23:20
# @Author  : Carl
# @Site    : 
# @File    : tasks.py
# @Software: PyCharm
from celery import Celery


# celery多线程、异步任务
def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['redis://localhost'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

#celery = make_celery(app)
