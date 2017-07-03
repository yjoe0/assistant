# -*- coding: utf-8 -*-
import requests
import json
import urllib
def getResTuLing(info):
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
def getResQYK(info):
    r = requests.get('http://api.qingyunke.com/api.php?key=free&appid=0&msg=%s'%(info))
    if r.status_code == 200:
        data = json.loads(r.content)['content']
        return data.encode('utf-8').replace('br','')
    else:
        return '请求失败'

def getXF(info):
    header = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cookie': 'pgv_si=s8394245120; pgv_pvi=951518208; pgv_info=ssi=s6425475795; JSESSIONID=FFD8B15ECF83ABB279322FC7542B7493; token=02950a64-45d0-4a45-9fb2-82a61da37529; account_id=2375191847; _ga=GA1.2.1287525527.1497697513; _gid=GA1.2.1963554924.1499009699; Hm_lvt_83a57cc9e205b0add91afc6c4f0babcc=1497699876,1499067176; Hm_lpvt_83a57cc9e205b0add91afc6c4f0babcc=1499067713'
    }
    url = 'http://aiui.xfyun.cn/taste/getAnswer?appid=5959f328&text=%s&uid=p7em1t'%(urllib.quote(info))
    print url
    r = requests.get(url, headers = header)
    if r.status_code == 200:
        print r.content
        # data = json.loads(r.content)['content']
        # return data.encode('utf-8').replace('br','')
    else:
        return '请求失败'
if __name__ == "__main__":
    print getXF('给我唱首歌')

    # 'http://aiui.xfyun.cn/taste/getAnswer?appid=5959f328&text=%E5%94%B1%E6%AD%8C'