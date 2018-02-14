# -*- coding=utf-8 -*-
import requests
import itchat
import random

KEY = '8edce3ce905a4c1dbb965e6b35c3834d'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    robots=['——By机器人小杨','——By机器人白杨','——By反正不是本人']
    reply = get_response(msg['Text'])+random.choice(robots)
    return reply or defaultReply

itchat.auto_login(enableCmdQR=True)
itchat.run()
