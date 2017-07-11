# -*- coding: utf-8 -*-
from components import Audio
from components import BD
from components import TuLing
from components import Interface
from core import Core
instanceList = []

def new_instance():
    newInstance = Core()
    instanceList.append(newInstance)
    return newInstance

originInstance = new_instance()

setDebug        = originInstance.setDebug
#in Interface
wakeUp          = originInstance.wakeUp
listen          = originInstance.listen
setWakeUpIns    = originInstance.setWakeUpIns

# in Audio
startAccord     = originInstance.startAccord
setAudio        = originInstance.setAudio

# in BD
setBdKey        = originInstance.setBdKey
getToken        = originInstance.getToken
txt2audio       = originInstance.txt2audio
audio2txt       = originInstance.audio2txt
play            = originInstance.play


# in TuLing
getTuLingRes    = originInstance.getTuLingRes
setTuLingKey    = originInstance.setTuLingKey
