# coding:utf-8
from sqlalchemy.ext.declarative import DeclarativeMeta
from decimal import *
from datetime import *
import json


class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                value = None
                try:
                    if isinstance(data, str):
                        value = data
                    elif isinstance(data, int) or isinstance(data, float):
                        value = data
                    elif isinstance(data, Decimal):
                        value = str(data)
                    elif isinstance(data, datetime):
                        value = data.strftime('%Y-%m-%d %M:%H:%S')
                    elif isinstance(data, date):
                        value = data.strftime('%Y-%m-%d')
                    fields[field] = value
                except TypeError:
                    fields[field] = None
            return fields
        return json.JSONEncoder.default(self, obj)
