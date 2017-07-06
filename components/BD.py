# -*- coding: utf-8 -*-
import requests
import base64
import json
import urllib
import mp3play
import time

def getToken():
    return '24.1b9356047b34e68d578d16a91caa7d0d.2592000.1501600048.282335-9232460'
    apiKey = "EXYmNkELXIqXkWN5wyyEsIyG"  
    secretKey = "475d29a02a98877e15c1cd8c846e63c5"
    auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey;  
  
    try:
        res = requests.get(auth_url)
    except Exception as e:
        print 'net work failed: %s'%(e)
        exit()
    if res.status_code == 200:
        json_data = res.content
        access_token = json.loads(json_data)['access_token']
        return  access_token
    else:
        print 'BaiDU yuyin access_token get failed:'
        print res
        exit()

def audio2txt(file):
    speech_data = file
    speech_base64=base64.b64encode(speech_data).decode('utf-8')
    speech_length=len(speech_data)
    data = {
        "format":"wav",
        "rate":8000,
        "channel":1,
        "token":getToken(),
        "cuid":"armbian-yjoe0",
        'speech': speech_base64,
        'len':speech_length
    }
    datas = json.dumps(data).encode('utf-8')
    url = 'http://vop.baidu.com/server_api'
    try:
        r = requests.post(url, data = datas)
    except Exception as e:
        print 'net work failed: %s'%(e)
        exit()
    result = json.loads(r.content)
    if result.has_key('result'):
        return True,result['result'][0][:-1]
    else:
        return False,'不好意思，我没听明白'


def text2audio(text):
    cuid = "armbian-yjoe0"   # MAC address
    baidu_url = "http://tsn.baidu.com/text2audio?tex=" + urllib.quote(text) + "&lan=zh&cuid=" + cuid + "&ctp=1&tok=" + getToken()
    try:
        r = requests.get(baidu_url)
    except Exception as e:
        print 'net work failed: %s'%(e)
        exit()
    if r.status_code == 200:
        with open('tmp.mp3', 'wb') as mp3:
            mp3.write(r.content)
        mp3 = mp3play.load('tmp.mp3')
        mp3.play()
        time.sleep(mp3.seconds()+1)

def play(path):
    mp3 = mp3play.load(path)
    mp3.play()
    time.sleep(mp3.seconds()+1)
if __name__ == "__main__":
    text2audio('我先睡了，有事叫我哦')