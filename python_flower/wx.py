import itchat, time  
from itchat.content import *  
from imagerec import recgnize  
 
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])  
def text_reply(msg):  
    msg.user.send('%s: %s' % ('回复', msg["Text"]))  
 
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])  
def download_files(msg):  
    msg.download(msg.fileName)  
    type1 = recgnize(msg.fileName)  
    print(type1)  
    typeSymbol = {  
        PICTURE: 'img',  
        VIDEO: 'vid', }.get(msg.type, 'fil')  
          
    msg.user.send(type1)  
    #return '@%s@%s' % (typeSymbol, msg.fileName)  
 
@itchat.msg_register(FRIENDS)  
def add_friend(msg):  
    msg.user.verify()  
    msg.user.send('Nice to meet you!')  
  
  
  
itchat.auto_login()  
itchat.run(True)  
