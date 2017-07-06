# -*- coding: utf-8 -*-
from components import Audio
from components import BD
from components import TuLing
# 指令集
instructs = [u'停止',u'关闭',u'关掉',u'退出']
# 唤醒集
wakeUpIns = [u'小小',u'猪',u'工作']

def listen(times):
    print 'wait wake up .....'
    cacheAudio = Audio().startAccord(times)
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
    cacheAudio = Audio().startAccord()
    status,txt = BD.audio2txt( cacheAudio )
    if status:
        print "you have said:%s"%(txt)
        if txt in wakeUpIns:
            BD.play('media/help.mp3')
            return True
    return False
if __name__ == '__main__':
    print 'start'
    while True:
        wakeup = wakeUp()
        print 'wakeup %d'%(wakeup)
        while wakeup > 0:
            if not listen(99):
                wakeup -=1
        if wakeup == 0:
            BD.play('media/bye.mp3')
            time.sleep(5)
