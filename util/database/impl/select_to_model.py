#coding:utf-8
from json import dumps, loads, JSONEncoder, JSONDecoder
import pickle
from app.model.Jsonable import Jsonable
from sqlalchemy.ext.declarative import DeclarativeMeta
import jira
from jira.resources import User
import datetime
import json

#python对象编码为json对象统一方法，用法为 json.dumps(project, cls=PythonObjectEncoder)
class PythonObjectEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (list, dict, str, int, float, bool, type(None), Jsonable, jira.resources.Resource)):
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    # this will fail on non-encodable values, like other classes
                    dumps(data)
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields
        return JSONEncoder.default(self, obj)


class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            # for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata' and not hasattr(obj.__class__.__bases__,x)]:
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata' and x != 'query' and x != 'query_class']:
                data = obj.__getattribute__(field)
                try:
                    # this will fail on non-encodable values, like other classes
                    json.dumps(data)
                    fields[field] = data
                except TypeError:    # 添加了对datetime的处理
                    if isinstance(data, datetime.datetime):
                        #fields[field] = data.isoformat()
                        fields[field] = data.strftime('%Y-%m-%d %H:%M:%S')
                    elif isinstance(data, datetime.date):
                        #fields[field] = data.isoformat()
                        fields[field] = data.strftime('%Y-%m-%d')
                    elif isinstance(data, datetime.timedelta):
                        fields[field] = (
                            datetime.datetime.min + data).time().isoformat()
                    # elif isinstance(data.__class__, DeclarativeMeta):
                    #     json.dumps(data,cls=AlchemyEncoder)
                    #     pass
                    else:
                        fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj.__class__, DeclarativeMeta):
            return dumps(obj,cls=AlchemyEncoder)
        else:
            return json.JSONEncoder.default(self, obj)


class ModelToJsonObject(object):
    def to_json(self,obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            return json.loads(json.dumps(obj,AlchemyEncoder))
        else:
            return json.loads