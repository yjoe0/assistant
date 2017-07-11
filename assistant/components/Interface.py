# -*- coding: utf-8 -*-
import Audio
import BD
import TuLing

# 指令集
ExitIns = [u'停止',u'关闭',u'关掉',u'退出']
# 唤醒集
# wakeUpIns = [u'开始',u'工作']

def load_interface(core):
    core.wakeUp         = wakeUp
    core.listen         = listen
    core.setWakeUpIns   = setWakeUpIns
    core.wakeUpIns = [u'开始',u'工作']
# 设定唤醒热词
def setWakeUpIns(self, wakeUpIns):
    self.wakeUpIns = wakeUpIns

# 热词唤醒实现
def wakeUp(self):
    print 'Waiting to be waked up'
    cacheAudio = Audio.startAccord(self)
    status,txt = BD.audio2txt( self, cacheAudio )
    if status:
        print "you have said:%s"%(txt)
        if txt in self.wakeUpIns:
            BD.txt2audio(self, '您好， 有什么可以帮助的吗')
            return 1
    return -1

# 听写对话
def listen(self, times=90):
    print 'I\'m listening.....'
    cacheAudio = Audio.startAccord(self, times)
    if not cacheAudio:
        return False
    status,txt = BD.audio2txt( self, cacheAudio )

    if status == 1:
        print txt
        if txt in ExitIns:
            BD.txt2audio(self, '即将退出')
            exit()
        response = TuLing.getTuLingRes( self, txt )
    else:
        response = txt
    BD.txt2audio(self, response)
    return True
