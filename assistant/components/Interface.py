# -*- coding: utf-8 -*-
from Audio import Audio
import BD
import TuLing

# 指令集
instructs = [u'停止',u'关闭',u'关掉',u'退出']
# 唤醒集
wakeUpIns = [u'开始',u'猪',u'工作']

def load_interface(core):
    core.wakeUp = wakeUp
    core.listen = listen
def wakeUp(self=None):
    cacheAudio = Audio().startAccord()
    status,txt = BD.audio2txt( self, cacheAudio )
    if status:
        print "you have said:%s"%(txt)
        if txt in wakeUpIns:
            BD.txt2audio(self, '您好， 有什么帮助的吗')
            return 1
    return -1

def listen(self, times=90):
    print 'wait wake up .....'
    cacheAudio = Audio().startAccord(times)
    if not cacheAudio:
        return False
    status,txt = BD.audio2txt( self, cacheAudio )

    if status == 1:
        print txt
        if txt in instructs:
            BD.txt2audio(self, '即将退出')
            exit()
        response = TuLing.getResTuLing( self, txt )
    else:
        response = txt
    BD.txt2audio(self, response)
    return True
