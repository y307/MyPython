#!/url/bin/env python3
# -*- coding: utf-8 -*-

#import sys
#import urllib.request
#import urllib.parse
#import time
from requests_html import HTMLSession

url_host = 'https://hst-api.wialon.com'
url_param = '/wialon/ajax.html?svc='
resurs = 'token/login&params='
token = '"833a8c3b52ab7c3df8ce46fb83f0604e0A3A1435887AD59852F113A3C01664D8FBE909F8"'
body = '{"token":' + token +',"fl":1}'
url_params = url_param + resurs + body
# print(url_params)

session = HTMLSession()
res = session.get(url_host + url_params)

if res.status_code != 200:
    exit(res.status_code)

data = res.json()
sid = data["eid"]
print(sid)
# ==================================================
resurs = 'core/search_items&sid=' + sid + '&params='
body = '{"spec":{"itemsType":"avl_resource","propName":"reporttemplates,sys_name,*","propValueMask":"*,*",\
        "sortType":"sys_id"},"force":1,"flags":8193,"from":0,"to":0}'
# print(body)
url_params = url_param + resurs + body
# print(url_params)
# print(url_host + url_params)
session = HTMLSession()
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
    # print(reportResourceId)



