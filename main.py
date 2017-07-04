# -*- coding: utf-8 -*-
import TuLing
import BD
import Audio
import time
instructs = [u'停止',u'关闭',u'关掉',u'退出']
wakeUpIns = [u'小小',u'猪',u'工作']
def loop(times):
    print 'wait wake up .....'
    cacheAudio = Audio.startAccord(times)
    if not cacheAudio:
        return False
    status,txt = BD.audio2txt( cacheAudio )

    if status == 1:
        print txt
        if txt in instructs:
            BD.text2audio('即将退出')
            exit()
        response = TuLing.getResTuLing( txt )
    else:
        response = txt
    BD.text2audio(response)
    return True
def wakeUp():
    cacheAudio = Audio.startAccord()
    status,txt = BD.audio2txt( cacheAudio )
    if status == 1:
        print txt
        print txt in wakeUpIns
        if txt in wakeUpIns:
            BD.play('media/help.mp3')
            return 3
    return -1
if __name__ == "__main__":
    print 'start'
    while True:
        wakeup = wakeUp()
        print 'wakeup %d'%(wakeup)
        while wakeup > 0:
            if not loop(30):
                wakeup -=1
        if wakeup == 0:
            BD.play('media/bye.mp3')
            time.sleep(5)