# -*- coding: utf-8 -*-
# Audio 中含有Audio,GetAudio 俩个类，因此需要在init中单独导入
from Audio import Audio
from Audio import load_Audio
from BD import load_BD
from TuLing import load_TuLing
from Interface import load_interface

def load_components(core):
    load_TuLing(core)
    load_BD(core)
    load_Audio(core)
    load_interface(core)