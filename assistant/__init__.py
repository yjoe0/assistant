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

wakeUp          = originInstance.wakeUp
listen          = originInstance.listen

# in Audio
startAccord     = originInstance.startAccord

# in BD
setBdKey        = originInstance.setBdKey
getToken        = originInstance.getToken
txt2audio       = originInstance.txt2audio
audio2txt       = originInstance.audio2txt
play            = originInstance.play


# in TuLing
getResTuLing    = originInstance.getResTuLing

