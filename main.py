# -*- coding: utf-8 -*-
import TuLing
import BD
import Audio
instructs = [u'停止',u'关闭',u'关掉',u'退出']

def loop():
    cacheAudio = Audio.startAccord()
    status,txt = BD.audio2txt( cacheAudio )

    if txt in instructs:
        BD.text2audio('即将退出')
        return
    if status == 1:
        print txt
        response = TuLing.getResTuLing( txt )
    else:
        response = txt
    BD.text2audio(response)
if __name__ == "__main__":
    loop()