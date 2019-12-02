#!/url/bin/env python3
# -*- coding: utf-8 -*-

# from builtins import print
import requests
import json5

url_host = 'https://hst-api.wialon.com/wialon/ajax.html?svc='
param = 'token/login&params='
token = '"833a8c3b52ab7c3df8ce46fb83f0604e0A3A1435887AD59852F113A3C01664D8FBE909F8"'
data_json = '{"token":' + token +',"fl":1}'

# r = requests.get(("{0}{1}{2}".format(url_host, param, data)))
res = requests.get(("{0}{1}{2}".format(url_host, param, data_json)))

if res.status_code != 200:
    exit(res.status_code)

data = json5.loads(res.text)
sid = data['eid']
print('sid: ' + sid)

param = 'core/search_items&sid=' + sid + '&params='

data_level1 = {
    "itemsType":"avl_resource",
    "propName":"reporttemplates,sys_name,*",
    "propValueMask":"*,*",
    "sortType":"sys_id"
}

data_level0 = {
    "spec": data_level1 ,
    "force":1,
    "flags":8193,
    "from":0,
    "to":0
}

data_json = str(json5.loads(data_level0,)).replace("'", "\"")
# print(data_json)

res = requests.get("{0}{1}{2}".format(url_host, param, data_json))
if res.status_code != 200:
    exit(res.status_code)

# data = res.json()
data = json5.loads(res.text)
# print(data)

if data['items'][0]['nm'] != 'profpererobka':
    exit(21)

resource_id = data['items'][0]['id']
print('resource_id: '+str(resource_id))

cur_object = "AA9186XE"

data_level1 = {
    "itemsType":"avl_unit",
    "propName":"sys_name",
    "propValueMask":cur_object,
    "sortType":"sys_name"
}

data_level0 = {
    "spec":data_level1,
    "force":1,
    "flags":1,
    "from":0,
    "to":0
}

# json_data = '{"spec":{"itemsType":"avl_unit","propName":"sys_name","propValueMask":"' + cur_object + \
#             '","sortType":"sys_name"},"force":1,"flags":1,"from":0,"to":0}'

data_json = str(json5.loads(data_level0,)).replace("'", "\"")
# print(data_json)

res = requests.get(("{0}{1}{2}".format(url_host, param, data_json)))
if res.status_code != 200:
    exit(res.status_code)

# data = res.json()
data = json5.loads(res.text)
object_id = data['items'][0]['id']
print('object_id: '+str(object_id))

# #res = requests.post(("{0}{1}".format(url_host, param)), json=json_data)
#
