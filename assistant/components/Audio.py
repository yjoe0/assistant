# -*- coding: utf-8 -*-
from pyaudio import PyAudio, paInt16 
import numpy as np 
import wave
from io import BytesIO

# NUM_SAMPLES = 2000      # pyAudio内部缓存的块的大小
# SAMPLING_RATE = 8000    # 取样频率
# LEVEL = 2300            # 声音保存的阈值
# COUNT_NUM = 80          # NUM_SAMPLES个取样之内出现COUNT_NUM个大于LEVEL的取样则记录声音
# SAVE_LENGTH = 4         # 声音记录的最小长度：SAVE_LENGTH * NUM_SAMPLES 个取样



def load_Audio(core):
    core.startAccord = startAccord
    core.setAudio    = setAudio

# 录音以及条件设置
def setAudio(self,NUM_SAMPLES = 2000,SAMPLING_RATE = 8000,LEVEL = 2300,COUNT_NUM = 80,SAVE_LENGTH = 4):
    self.NUM_SAMPLES = NUM_SAMPLES
    self.SAMPLING_RATE = SAMPLING_RATE
    self.LEVEL = LEVEL
    self.COUNT_NUM = COUNT_NUM
    self.SAVE_LENGTH = SAVE_LENGTH

# 将data中的数据保存到名为filename的WAV文件中
def save_wave_file(self, filename, data): 
    f = BytesIO()
    wf = wave.open(f, 'wb') 
    wf.setnchannels(1) 
    wf.setsampwidth(2) 
    wf.setframerate(self.SAMPLING_RATE) 
    wf.writeframes("".join(data)) 
    wf.close()
    return f.getvalue()

def startAccord(self, Times=100):
    # 开启声音输入
    pa = PyAudio() 
    if not self.SAMPLING_RATE:
        setAudio(self)
    stream = pa.open(format=paInt16, channels=1, rate=self.SAMPLING_RATE, input=True, 
                    frames_per_buffer=self.NUM_SAMPLES) 

    save_count = 0 
    save_buffer = [] 

    while True: 
        #时间控制
        if Times != 100:
            Times -=1
        # 读入NUM_SAMPLES个取样
        string_audio_data = stream.read(self.NUM_SAMPLES) 
        # 将读入的数据转换为数组
        audio_data = np.fromstring(string_audio_data, dtype=np.short) 
        # 计算大于LEVEL的取样的个数
        large_sample_count = np.sum( audio_data > self.LEVEL ) 
        if self.debug:
            print np.max(audio_data) 
        # 如果个数大于COUNT_NUM，则至少保存SAVE_LENGTH个块
        if large_sample_count > self.COUNT_NUM: 
            save_count = self.SAVE_LENGTH 
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
                cacheFile = save_wave_file(self, filename, save_buffer) 
                save_buffer = [] 
                stream.close()
                if self.debug:
                    print "saved audio stream" 
                return cacheFile
                break
        if Times < 0:
            stream.close()
            return False
            break