# coding:utf-8
import requests
import json


def req_http_api(req_params):
    req = requests.post('http://api.waditu.com', json.dumps(req_params).encode('utf-8'))
    req.encoding
    result = json.loads(req.text)
    if result['code'] != 0:
        raise Exception(result['msg'])
    return result['data']


def query(api_name, fields, **kwargs):
    req_params = {
        'api_name': api_name,
        'token': '9fa73a58ea99ddfe8fa4a2cf2b9b265a486ea47f50376d7226faab40',
        'params': kwargs,
        'fields': fields
    }

    data = req_http_api(req_params)
    columns = data['fields']
    items = data['items']
    return items