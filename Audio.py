# -*- coding: utf-8 -*-
from pyaudio import PyAudio, paInt16 
import numpy as np 
import wave
from io import BytesIO

NUM_SAMPLES = 2000      # pyAudio内部缓存的块的大小
SAMPLING_RATE = 8000    # 取样频率
LEVEL = 2300            # 声音保存的阈值
COUNT_NUM = 80          # NUM_SAMPLES个取样之内出现COUNT_NUM个大于LEVEL的取样则记录声音
SAVE_LENGTH = 4         # 声音记录的最小长度：SAVE_LENGTH * NUM_SAMPLES 个取样


# 将data中的数据保存到名为filename的WAV文件中
def save_wave_file(filename, data): 
    f = BytesIO()
    wf = wave.open(f, 'wb') 
    wf.setnchannels(1) 
    wf.setsampwidth(2) 
    wf.setframerate(SAMPLING_RATE) 
    wf.writeframes("".join(data)) 
    wf.close()
    return f.getvalue()

def startAccord(Times=100):
    # 开启声音输入
    pa = PyAudio() 
    stream = pa.open(format=paInt16, channels=1, rate=SAMPLING_RATE, input=True, 
                    frames_per_buffer=NUM_SAMPLES) 

    save_count = 0 
    save_buffer = [] 

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
        # print np.max(audio_data) 
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
                cacheFile = save_wave_file(filename, save_buffer) 
                save_buffer = [] 
                pa.close(stream)
                print filename, "saved" 
                return cacheFile
                break
        if Times < 0:
            pa.close(stream)
            return False
            break
if __name__ == "__main__":
    startAccord()