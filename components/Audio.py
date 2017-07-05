# -*- coding: utf-8 -*-
from pyaudio import PyAudio, paInt16 
import numpy as np 
import wave
from io import BytesIO


NUM_SAMPLES = 2000      # pyAudio内部缓存的块的大小
SAMPLING_RATE = 8000    # 取样频率
LEVEL = 1300            # 声音保存的阈值
COUNT_NUM = 30          # NUM_SAMPLES个取样之内出现COUNT_NUM个大于LEVEL的取样则记录声音
SAVE_LENGTH = 4         # 声音记录的最小长度：SAVE_LENGTH * NUM_SAMPLES 个取样


# 单例模式，避免麦克风频繁打开
class GetAudio(type):  
    def __init__(cls, name, bases, dict):  
        super(GetAudio, cls).__init__(name, bases, dict)  
        cls._instance = None  
    def __call__(cls, *args, **kw):  
        if cls._instance is None:  
            cls._instance = super(GetAudio, cls).__call__(*args, **kw)  
        return cls._instance  



class Audio(object):  
    __metaclass__ = GetAudio
    pa = PyAudio() 
    stream = pa.open(format=paInt16, channels=1, rate=SAMPLING_RATE, input=True, frames_per_buffer=NUM_SAMPLES)

    # 将data中的数据保存到名为filename的WAV文件中
    def save_wave_file(self, filename, data): 
        f = BytesIO()
        wf = wave.open(f, 'wb') 
        wf.setnchannels(1) 
        wf.setsampwidth(2) 
        wf.setframerate(SAMPLING_RATE) 
        wf.writeframes("".join(data)) 
        wf.close()
        return f.getvalue()

    def test(self):
        print self.stream
    # 开始录音,默认100一直循环录音,小于100时循环设定的次数
    def startAccord(self, Times=100):
        save_count = 0 
        save_buffer = [] 
        stream = self.stream
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
            print np.max(audio_data) 
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
                    print filename, "saved" 
                    return cacheFile
                    break
            if Times < 0:
                return False
                break



# a = Audio()