import threading, time
import random

'''
事件处理的机制：全局定义了一个“Flag”，如果“Flag”值为 False，那么当程序执行 event.wait 方法时就会阻塞；
如果“Flag”值为True，那么执行event.wait 方法时便不再阻塞。

    clear：将“Flag”设置为False
    set：将“Flag”设置为True
    用 threading.Event 实现线程间通信，使用threading.Event可以使一个线程等待其他线程的通知，我们把这个Event传递到线程对象中，

    Event默认内置了一个标志，初始值为False。一旦该线程通过wait()方法进入等待状态，
	直到另一个线程调用该Event的set()方法将内置标志设置为True时，该Event会通知所有等待状态的线程恢复运行。
'''
def light():
    if not event.isSet():    #初始化evet的flag为真
        event.set()    #wait就不阻塞 #绿灯状态
    count = 0
    while True:
        if count < 10:
            print('\033[42;1m---green light on---\033[0m')
        elif count < 13:
            print('\033[43;1m---yellow light on---\033[0m')
        elif count < 20:
            if event.isSet():
                event.clear()
            print('\033[41;1m---red light on---\033[0m')
        else:
            count = 0
            event.set()    #打开绿灯
        time.sleep(1)
        count += 1

def car(n):
    while 1:
        time.sleep(random.randrange(3, 10))
        #print(event.isSet())
        if event.isSet():
            print("car [%s] is running..." % n)
        else:
            print('car [%s] is waiting for the red light...' % n)
            event.wait()    #红灯状态下调用wait方法阻塞，汽车等待状态

if __name__ == '__main__':
    car_list = ['BMW', 'AUDI', 'SANTANA']
    event = threading.Event()
    Light = threading.Thread(target=light)
    Light.start()
    for i in car_list:
        t = threading.Thread(target=car, args=(i,))
        t.start()
