# -*- coding: utf-8 -*-
import assistant
apiKey = "EXYmNkELXIqXkWN5wyyEsIyG"  
secretKey = "475d29a02a98877e15c1cd8c846e63c5"
TuLingKey = '1cd3fb922c85135f9e198c4319cae0fe'
assistant.setBdKey(apiKey, secretKey)
assistant.txt2audio('哈哈哈')

assistant.setTuLingKey( TuLingKey )
print assistant.getTuLingRes('你好')
assistant.setAudioDebug(True)
assistant.wakeUp()
assistant.setWakeUpIns([u'上班'])
assistant.wakeUp()
# print assistant.getToken()
while True:
    wakeup = assistant.wakeUp()
    while wakeup > 0:
        if not assistant.listen(5):
            wakeup -=1
    if wakeup == 0:
        assistant.txt2audio('睡觉')
