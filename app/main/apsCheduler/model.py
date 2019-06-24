# coding = utf-8
# @Time    : 2018/3/30 0030 2:06
# @Author  : Carl
# @Site    : 
# @File    : model.py
# @Software: PyCharm
from app.main import db


class Apscheduler(db.Model):
    __tablename__ = 'apscheduler_jobs'
    id = db.Column(db.String(50), primary_key=True)
    next_run_time = db.Column(db.String(50), comment=u"下次执行时间")
    job_state = db.Column(db.LargeBinary(length=65536), nullable=False, comment=u"任务详情")
    remark = db.Column(db.String(200), comment=u"备注")

    def __repr__(self):
        return '<Apscheduler %r>' % self.code

    def save(self):
        db.session.add(self)
        db.session.commit()
