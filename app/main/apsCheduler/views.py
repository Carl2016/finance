# coding = utf-8
# @Time    : 2018/2/8 0008 22:51
# @Author  : Carl
# @Site    : 
# @File    : views.py
# @Software: PyCharm
from flask import request, jsonify, render_template, globals
from app.main.apsCheduler import scheduler
from app.main.apsCheduler.config import schedulers
from datetime import datetime
from app.main.common.alchemyEncoder import AlchemyEncoder
from flask_login import login_required
import json


@scheduler.route('/list', methods=['GET', 'POST'])
@login_required
def list():
    if request.method == 'POST':
        page = request.form['page']
        limit = request.form['limit']
        current_page = int(page)
        current_limit = int(limit)
        start = (current_page - 1) * current_limit  # 10 20 (current_page-1)*10
        end = current_page * current_limit  # 20 30  current_page*10

        jobs = schedulers.get_jobs()
        total = jobs.__len__()
        jobs = jobs[start:end]
        data = []
        for index in range(jobs.__len__()):
            item = {}
            cron = ''
            job = jobs[index]
            item["id"] = job.id
            item["next_run_time"] = None if job.next_run_time is None else job.next_run_time.strftime("%Y-%m-%d %H:%M:%S")
            item["state"] = '1' if job.next_run_time is None else '2'
            item["name"] = job.name
            trigger = job.trigger
            fields = trigger.fields
            for i in range(len(fields)):
                string = '* ' if fields[i].expressions[0].step is None else '*/' + str(fields[i].expressions[0].step)
                cron = cron + string
            # item["startDate"] = job.trigger.start_date
            # item["endDate"] = job.trigger.end_date
            item["args"] = job.args
            item["cron"] = cron
            item["max_instances"] = job.max_instances
            item["misfire_grace_time"] = job.misfire_grace_time
            item["func_ref"] = job.func_ref
            data.append(item)
        result = dict(code='0000', msg='获取成功', count=total, data=data)
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    return render_template('system/scheduler.html')


def jobfromparm(**jobargs):
    id = None if jobargs['id'] == '' else jobargs['id']
    name = None if jobargs['name'] == '' else jobargs['name']
    func = None if jobargs['func'] == '' else jobargs['func']
    args = None if jobargs['args'] == '' else eval(jobargs['args'])
    second = None if jobargs['second'] == '' else jobargs['second']
    minute = None if jobargs['minute'] == '' else jobargs['minute']
    hour = None if jobargs['hour'] == '' else jobargs['hour']
    day = None if jobargs['day'] == '' else jobargs['day']
    month = None if jobargs['month'] == '' else jobargs['month']
    year = None if jobargs['year'] == '' else jobargs['year']
    day_of_week = None if jobargs['dayOfWeek'] == '' else jobargs['dayOfWeek']
    week = None if jobargs['week'] == '' else jobargs['week']
    start_date = None if jobargs['startDate'] == '' else datetime.strptime(jobargs['startDate'], "%Y-%m-%d %H:%M:%S")
    end_date = None if jobargs['endDate'] == '' else datetime.strptime(jobargs['endDate'], "%Y-%m-%d %H:%M:%S")
    max_instances = None if jobargs['maxInstances'] == '' else jobargs['maxInstances']
    remark = None if jobargs['remark'] == '' else jobargs['remark']
    if id is None:
        schedulers.add_job(func=func, args=args, trigger='cron', second=second, minute=minute, hour=hour, day=day, month=month, year=year, day_of_week=day_of_week, week=week,
                           start_date=start_date, end_date=end_date, max_instances=1, misfire_grace_time=60, replace_existing=True)  # 间隔3秒钟执行一次
    else:
        # current_app.schedulers.modify_job(job_id=id, args=args, trigger='cron', second=second, minute=minute, hour=hour, day=day, month=month, year=year, day_of_week=day_of_week, week=week,
        #                       start_date=start_date, end_date=end_date, max_instances=1)
        schedulers.reschedule_job(job_id=id, trigger='cron', second=second, minute=minute, hour=hour, day=day, month=month, year=year, day_of_week=day_of_week, week=week,
                              start_date=start_date, end_date=end_date)
    return None


@scheduler.route('/batchPause', methods=['GET', 'POST'])
@login_required
def pause():
    ids = request.form.get('jobs')
    id_list = json.loads(ids)
    for i in range(len(id_list)):

        schedulers.pause_job(id_list[i])
    result = dict(code='0000', msg='暂停成功', connt=None, data=None)
    return jsonify(result)


@scheduler.route('/batchExecute', methods=['GET', 'POST'])
@login_required
def execute():
    ids = request.form.get('jobs')
    id_list = json.loads(ids)
    for i in range(len(id_list)):
        schedulers.scheduled_job(id_list[i])
    result = dict(code='0000', msg='立即执行成功', connt=None, data=None)
    return jsonify(result)


@scheduler.route('/batchResume', methods=['GET', 'POST'])
@login_required
def resume():
    ids = request.form.get('jobs')
    id_list = json.loads(ids)
    for i in range(len(id_list)):
        schedulers.resume_job(id_list[i])
    result = dict(code='0000', msg='恢复成功', connt=None, data=None)
    return jsonify(result)


@scheduler.route('/batchDelete', methods=['GET', 'POST'])
@login_required
def delete():
    ids = request.form.get('jobs')
    id_list = json.loads(ids)
    for i in range(len(id_list)):
        schedulers.remove_job(id_list[i])
    result = dict(code='0000', msg='删除成功', connt=None, data=None)
    return jsonify(result)


@scheduler.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        data = {}
        data['id'] = request.values.get("id")
        data['name'] = request.values.get("name")
        data['func'] = request.values.get("func")
        data['args'] = request.values.get("args")
        data['second'] = request.values.get("second")
        data['minute'] = request.values.get("minute")
        data['hour'] = request.values.get("hour")
        data['day'] = request.values.get("day")
        data['month'] = request.values.get("month")
        data['year'] = request.values.get("year")
        data['dayOfWeek'] = request.values.get("dayOfWeek")
        data['week'] = request.values.get("week")
        data['startDate'] = request.values.get("startDate")
        data['endDate'] = request.values.get("endDate")
        data['maxInstances'] = request.values.get("maxInstances")
        data['remark'] = request.values.get("remark")
        jobfromparm(**data)
        result = dict(code='0000', msg='添加成功', connt=None, data=None)
        return jsonify(result)
    return render_template('system/schedule-edit.html')


@scheduler.route('/edit/<id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    if request.method == 'POST':
        data = {}
        data['id'] = request.values.get("id")
        data['name'] = request.values.get("name")
        data['func'] = request.values.get("func")
        data['second'] = request.values.get("second")
        data['minute'] = request.values.get("minute")
        data['hour'] = request.values.get("hour")
        data['day'] = request.values.get("day")
        data['month'] = request.values.get("month")
        data['year'] = request.values.get("year")
        data['dayOfWeek'] = request.values.get("dayOfWeek")
        data['week'] = request.values.get("week")
        data['startDate'] = request.values.get("startDate")
        data['endDate'] = request.values.get("endDate")
        data['maxInstances'] = request.values.get("maxInstances")
        data['remark'] = request.values.get("remark")
        jobfromparm(**data)
        result = dict(code='0000', msg='修改成功', connt=None, data=None)
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    job = schedulers.get_job(id)
    schedule = {}
    schedule["id"] = job.id
    schedule["next_run_time"] = None if job.next_run_time is None else job.next_run_time.strftime("%Y-%m-%d %H:%M:%S")
    schedule["name"] = job.name
    schedule["func"] = job.func_ref
    schedule["args"] = job.args
    fields = job.trigger.fields
    for i in range(len(fields)):
        schedule[fields[i].name] = str(fields[i].expressions[0])
    return render_template('system/schedule-edit.html', **schedule)

