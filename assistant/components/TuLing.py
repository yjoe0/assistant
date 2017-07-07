# -*- coding: utf-8 -*-
import requests
import json
import urllib

def load_TuLing(core):
    core.getResTuLing = getResTuLing

def getResTuLing(self, info):
    postData = {
        "key": "1cd3fb922c85135f9e198c4319cae0fe",
        "info": info,
        "userid":"12345678"
    }
    r = requests.post('http://www.tuling123.com/openapi/api', data = postData)
    if r.status_code == 200:
        data = json.loads(r.content)['text']
        return data.encode('utf-8')
    else:
        return '请求失败'
def getResQYK(self, info):
    r = requests.get('http://api.qingyunke.com/api.php?key=free&appid=0&msg=%s'%(info))
    if r.status_code == 200:
        data = json.loads(r.content)['content']
        return data.encode('utf-8').replace('br','')
    else:
        return '请求失败'

if __name__ == "__main__":
    print getResQYK('给我唱首歌吧')
