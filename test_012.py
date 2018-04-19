# -*- coding: utf-8 -*-

import threading, time

'''
现在写个捉迷藏的游戏来具体介绍threading.Condition的基本使用。
假设这个游戏由两个人来玩，一个藏(Hider)，一个找(Seeker)。游戏的规则如下：
1. 游戏开始之后，Seeker先把自己眼睛蒙上，蒙上眼睛后，就通知Hider；
2. Hider接收通知后开始找地方将自己藏起来，藏好之后，再通知Seeker可以找了；
3. Seeker接收到通知之后，就开始找Hider。Hider和Seeker都是独立的个体，
   在程序中用两个独立的线程来表示，在游戏过程中，两者之间的行为有一定的时序关系，
   我们通过Condition来控制这种时序关系。

'''

def Seeker(cond, name):
    time.sleep(2)
    cond.acquire()
    print('%s :我已经把眼睛蒙上了！'% name)
    cond.notify()
    cond.wait()
    for i in range(3):
        print('%s is finding!!!'% name)
        time.sleep(2)
    cond.notify()
    cond.release()
    print('%s :我赢了！'% name)

def Hider(cond, name):
    cond.acquire()
    cond.wait()
    for i in range(2):
        print('%s is hiding!!!'% name)
        time.sleep(3)
    print('%s :我已经藏好了，你快来找我吧！'% name)
    cond.notify()
    cond.wait()
    cond.release()
    print('%s :被你找到了，唉~^~!'% name)


if __name__ == '__main__':
    cond = threading.Condition()
    seeker = threading.Thread(target=Seeker, args=(cond, 'seeker'))
    hider = threading.Thread(target=Hider, args=(cond, 'hider'))
    seeker.start()
    hider.start()
