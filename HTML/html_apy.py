#!/url/bin/env python3
# -*- coding: utf-8 -*-

#import sys
#import urllib.request
#import urllib.parse
#import time
from requests_html import HTMLSession

url_host = 'https://hst-api.wialon.com'
url_resurs = '/wialon/ajax.html?svc='
params = 'token/login&params='
token = '"833a8c3b52ab7c3df8ce46fb83f0604e0A3A1435887AD59852F113A3C01664D8FBE909F8"'
body = '{"token":' + token +',"fl":1}'
url_params = url_resurs + params + body
# print(url_params)

session = HTMLSession()
res = session.get(url_host + url_params)

if res.status_code != 200:
    exit(res.status_code)

data = res.json()
sid = data["eid"]
print(f'sid: {sid}')
# ==================================================
params = 'core/search_items&sid=' + sid + '&params='
body = '{"spec":{"itemsType":"avl_resource","propName":"reporttemplates,sys_name,*","propValueMask":"*,*",\
        "sortType":"sys_id"},"force":1,"flags":8193,"from":0,"to":0}'
# print(body)
url_params = url_resurs + params + body
# print(url_params)
# print(url_host + url_params)
# session = HTMLSession()
res = session.get(url_host + url_params)

if res.status_code != 200:
    exit(res.status_code)

data = res.json()
# print('Respond:\n' + str(data))
# print(data)
# print(data["items"])
data_list = data["items"]
data_list_items = data_list[0]
# print(data_list_items)
data_nm = data_list_items["nm"]
# print(data_nm)
if data_nm == 'profpererobka':
    reportResourceId = data_list_items["id"]
    print(f'reportResourceId: {reportResourceId}')

params = 'core/search_items&sid=' + sid + '&params='
cur_object = 'AA9186XE'
body = '{"spec":{"itemsType":"avl_unit","propName":"sys_name","propValueMask":"' + cur_object + \
       '","sortType":"sys_name"},"force":1,"flags":1,"from":0,"to":0}'
url_params = url_resurs + params + body

print(f'{url_host}{url_resurs}{params}')

#res = session.get(url_host + url_params)
res = session.post(url_host + url_resurs + params, body) # "Content-Type", "application/json"

if res.status_code != 200:
    exit(res.status_code)

data = res.json()
print(data)
# reportObjectId = data['items'][0]['id']
# print(f'reportObjectId: {reportObjectId}')


