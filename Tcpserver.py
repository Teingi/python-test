#---coding:utf-8
#创建tcp服务器
from socket import *
from time import ctime

#对bind()方法的标识，表示它可以使用任何可用的地址
HOST = ''
PORT = 21567
BUFSIZE = 1024 #将缓冲区的大小设置为1KB
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock,addr = tcpSerSock.accept()
    print('...connected from:',addr)

    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        #tcpClisock.send('[%s] %s' %(bytes(ctime(), 'utf-8'),data))
        tcpCliSock.send(bytes('[%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8'))
    tcpCliSock.close()
tcpSerSock.close()
