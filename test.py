# -*- coding: utf-8 -*-
import assistant
apiKey = 'xxxxxxxxxxxxxx'  
secretKey = 'xxxxxxxxxxxxxxx'
TuLingKey = 'xxxxxxxxxxxxxxxxxxxx'
assistant.setBdKey(apiKey, secretKey)
assistant.txt2audio('哈哈哈')

assistant.setTuLingKey( TuLingKey )
print assistant.getTuLingRes('你好')
assistant.setDebug(True)
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
