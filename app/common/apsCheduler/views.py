# coding = utf-8
# @Time    : 2018/2/8 0008 22:51
# @Author  : Carl
# @Site    : 
# @File    : views.py
# @Software: PyCharm
from flask import request
from flask_apscheduler import scheduler
from app.common.apsCheduler import scheduler


def job1(a, b):
    print(str(a) + ' ' + str(b))


def jobfromparm(**jobargs):
    id = jobargs['id']
    func = jobargs['func']
    args = eval(jobargs['args'])
    trigger = jobargs['trigger']
    seconds = jobargs['seconds']
    print('add job: ',id)
    job = scheduler.add_job(func=func,id=id, args=args,trigger=trigger,seconds=seconds,replace_existing=True)
    return 'sucess'


@scheduler.route('/pause')
def pausejob():
    scheduler.pause_job('job1')
    return "Success!"


@scheduler.route('/resume')
def resumejob():
    scheduler.resume_job('job1')
    return "Success!"


@scheduler.route('/addjob', methods=['GET', 'POST'])
def addjob():
    data = request.get_json(force=True)
    job = jobfromparm(**data)