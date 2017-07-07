# assistant
## 结合百度语音以及图灵机器人制作的一个工具集，like simple goole assistant

### 安装：python setup.py install 即可

### 依赖项：
Window下：   
['PyAudio', 'mp3play','numpy','requests']        
如果自动依赖项安装失败需要自己手动安装了。貌似PyAudio安装容易出问题

Linux下：       
['PyAudio'，','numpy','requests','mpg123']   
因为mp3play不支持在linux下运行。因此需要手动安装mpg123.（直接apt-get install mpg123就好）

## assistant目前提供接口如下：    
**wakeUp**：
    assistant.wakeUp()        
    返回参数：True|False   
    热词唤醒，默认设置[u'开始',u'工作']唤醒，可以自行参考Interface文件来修改wakeUp方法   

---

**listen**： assistant.listen(times)   
    返回参数：True|False   
    唤醒后开始监听语音，并调用图灵接口自动应答，参考Interface文件修改，参数times传递给下面startAccord     

---

**startAccord**：assistant.startAccord(times)    
    返回参数：捕获到的音频流|False（在设定times循环次数内没有捕获到符合条件的音频则返回False）
    开始录音，times表示等待录音时长，默认100表示一直等待直到获取到符合条件的音频流，
    times小于100则表示循环录音次数为times设定的次数，

---

**setBdKey**：assistant.setBdKey(apikey, secretKey)    
    设定百度apikey以及secretKey
---

**getToken**：assistant.getToken()    
    返回参数： 返回百度access_token
    获取百度Token

---

**txt2audio**：assistant.txt2audio(txt)   
    文本转语音播放

---

**audio2txt**：assistant.audio2txt(file)   
    语音转文本,file表示wave读取流，建议直接使用startAccord的返回数据

---

**play**：assistant.play(path)   
    播放mp3文件，path表示文件路径

---

**getResTuLing**：assistant.getResTuLing(info)   
    返回图灵接口的返回数据

---

**setTuLingKey**：assistant.setTuLingKey(key)   
    设定图灵key

---

