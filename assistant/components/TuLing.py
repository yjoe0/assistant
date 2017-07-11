# -*- coding: utf-8 -*-
import requests
import json
import urllib

def load_TuLing(core):
    core.getTuLingRes = getTuLingRes
    core.setTuLingKey = setTuLingKey

def setTuLingKey(self, key):
    self.TuLingkey = key

def getTuLingRes(self, info):
    postData = {
        "key": self.TuLingkey,
        "info": info,
        "userid":"12345678"
    }
    r = requests.post('http://www.tuling123.com/openapi/api', data = postData)
    if r.status_code == 200:
        data = json.loads(r.content)['text']
        return data.encode('utf-8')
    else:
        return '请求失败'
def getQYKRes(self, info):
    r = requests.get('http://api.qingyunke.com/api.php?key=free&appid=0&msg=%s'%(info))
    if r.status_code == 200:
        data = json.loads(r.content)['content']
        return data.encode('utf-8').replace('br','')
    else:
        return '请求失败'

