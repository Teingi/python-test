#---coding:utf-8

from socket import *

HOST = 'localhost'
PORT =21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('>')
    if not data:
        break
    tcpCliSock.send(bytes(data,'utf-8'))
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print(data.decode('utf-8'))
tcpClisock.close()
