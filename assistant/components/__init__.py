# -*- coding: utf-8 -*-
from Audio import load_Audio
from BD import load_BD
from TuLing import load_TuLing
from Interface import load_interface

def load_components(core):
    load_TuLing(core)
    load_BD(core)
    load_Audio(core)
    load_interface(core)