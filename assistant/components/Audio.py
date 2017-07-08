# -*- coding: utf-8 -*-
from pyaudio import PyAudio, paInt16 
import numpy as np 
import wave
from io import BytesIO

def load_Audio(core):
    core.startAccord = Audio().startAccord
    core.setAudio    = Audio().setAudio
    core.setAudioDebug = Audio().setAudioDebug
# 单例模式，避免麦克风频繁打开
class GetAudio(type):  
    '''
        docs:单例模式，避免Audio被重复创建，因为MIC不能被多次打开
    '''
    def __init__(cls, name, bases, dict):  
        super(GetAudio, cls).__init__(name, bases, dict)  
        cls._instance = None  
    def __call__(cls, *args, **kw):  
        if cls._instance is None:  
            cls._instance = super(GetAudio, cls).__call__(*args, **kw)  
        return cls._instance  


class Audio(object):  
    '''
        docs:PyAudio 录音类
        methods: startAccord
    '''
    __metaclass__ = GetAudio
    debug = False
    NUM_SAMPLES = 2000
    SAMPLING_RATE = 8000
    LEVEL = 1300
    COUNT_NUM = 30
    SAVE_LENGTH = 4
    def setAudioDebug(self, debug = False):
        self.debug = debug
    # 设置开始录音的条件以及录音设置
    def setAudio(self,NUM_SAMPLES = 2000 ,SAMPLING_RATE = 8000 ,LEVEL = 1300 ,COUNT_NUM = 30 ,SAVE_LENGTH = 4):
        self.NUM_SAMPLES = NUM_SAMPLES if NUM_SAMPLES else self.NUM_SAMPLES
        self.SAMPLING_RATE = SAMPLING_RATE if SAMPLING_RATE else self.SAMPLING_RATE
        self.LEVEL = LEVEL if LEVEL else self.LEVEL
        self.COUNT_NUM = COUNT_NUM if COUNT_NUM else self.COUNT_NUM
        self.SAVE_LENGTH = SAVE_LENGTH if SAVE_LENGTH else self.SAVE_LENGTH

    def getStream(self):
        pa = PyAudio() 
        NUM_SAMPLES = self.NUM_SAMPLES
        SAMPLING_RATE = self.SAMPLING_RATE
        try:
            stream = pa.open(format=paInt16, channels=1, rate=SAMPLING_RATE, input=True, frames_per_buffer=NUM_SAMPLES)
            return stream
        except Exception as e:
            print 'MIC open failed: %s'%(e)
            exit()



    # 将data中的数据保存到名为filename的WAV文件中
    def save_wave_file(self, filename, data): 
        '''
            docs:保存Wav文件并返回音频流
            文件是保存在BytesIO()中，如要保存下wav文件，将wf = wave.open(f, 'wb') 中的f改为任意文件名即可
        '''
        f = BytesIO()
        wf = wave.open(f, 'wb') 
        wf.setnchannels(1) 
        wf.setsampwidth(2) 
        wf.setframerate( self.SAMPLING_RATE ) 
        wf.writeframes("".join(data)) 
        wf.close()
        return f.getvalue()

    # 开始录音,默认100一直循环录音,小于100时循环设定的次数
    def startAccord(self, Times=100):
        '''
        docs: Audio startAccord() 不设置Times值时会一直循环等待，直到获取到满足条件的录音流
        设置Times小于100时，会进入Times循环次数，返回值可能是音频流，也有可能返回False
        '''
        save_count = 0 
        save_buffer = [] 
        stream = self.getStream()
        
        NUM_SAMPLES = self.NUM_SAMPLES 
        SAMPLING_RATE = self.SAMPLING_RATE 
        LEVEL = self.LEVEL 
        COUNT_NUM = self.COUNT_NUM 
        SAVE_LENGTH = self.SAVE_LENGTH 

        if self.debug:
            print 'start accord'

        while True: 
            #时间控制
            if Times != 100:
                Times -=1
            # 读入NUM_SAMPLES个取样
            string_audio_data = stream.read(NUM_SAMPLES) 
            # 将读入的数据转换为数组
            audio_data = np.fromstring(string_audio_data, dtype=np.short) 
            # 计算大于LEVEL的取样的个数
            large_sample_count = np.sum( audio_data > LEVEL ) 
            if self.debug:
                print "max audio is %d"%( np.max(audio_data) )
            # 如果个数大于COUNT_NUM，则至少保存SAVE_LENGTH个块
            if large_sample_count > COUNT_NUM: 
                save_count = SAVE_LENGTH 
            else: 
                save_count -= 1 

            if save_count < 0: 
                save_count = 0 

            if save_count > 0: 
                # 将要保存的数据存放到save_buffer中
                save_buffer.append( string_audio_data ) 
            else: 
                # 将save_buffer中的数据写入WAV文件，WAV文件的文件名是保存的时刻
                if len(save_buffer) > 0: 
                    filename = "tmp.wav" 
                    cacheFile = self.save_wave_file(filename, save_buffer) 
                    save_buffer = [] 
                    if self.debug:
                        print filename, "saved" 
                    return cacheFile
                    break
            if Times < 0:
                return False
                break
