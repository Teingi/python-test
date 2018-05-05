'''
#闭包函数的实例
# outer是外部函数 a和b都是外函数的临时变量
def outer( a ):
    b = 10
    # inner是内函数
    def inner():
        #在内函数中 用到了外函数的临时变量
        print(a+b)
    # 外函数的返回值是内函数的引用
    return inner

if __name__ == '__main__':
    # 在这里我们调用外函数传入参数5
    #此时外函数两个临时变量 a是5 b是10 ，并创建了内函数，然后把内函数的引用返回存给了demo
    # 外函数结束的时候发现内部函数将会用到自己的临时变量，这两个临时变量就不会释放，会绑定给这个内部函数
    demo = outer(5)
    # 我们调用内部函数，看一看内部函数是不是能使用外部函数的临时变量
    # demo存了外函数的返回值，也就是inner函数的引用，这里相当于执行inner函数
    demo() # 15

    demo2 = outer(7)
    demo2()#17

###################################################   
def addx(x):
    def addy(y):
        return x + y
    return addy
xy = addx(6)
print(type(xy))
print(xy.__name__)
print(xy(7))

对以上代码加以说明： 
如果在一个内部函数里：addy(y)就是这个内部函数。 
对在外部作用域（但不是全局作用域）的变量进行引用：x就是被引用的变量，x在外部作用域addx（x）函数里，但不在全局作用域里。 
那么这个内部函数addy(y)就是闭包。
'''
#################################################
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)#注意这句代码返回的是f的开辟的内存地址，并不是值。
        # fs.append(f())# 这句代码返回的才是i*i的值
    return fs
f1, f2, f3 = count()#

print(f1)
print(f2)
print(f3)
print(f1(),f2(),f3())

