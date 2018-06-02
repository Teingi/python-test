# -*- coding:utf-8 -*-

'''
排列组合练习

'''


# n_raw = int(input("请输入一个整数n："))
# m_raw = int(input("请输入一个整数m："))
# 定义一个求阶乘的函数
def myfact(n):
    fact = 1
    if n < 0:
        pass
    elif n == 0:
        return fact
    else:
        for i in range(1,n + 1):
            fact = fact * i
        return fact

#k = myfact(n_raw)
#print("该整数的阶乘是：",k)


#求排列
def myfact2(n,m):
    if n < m:
        pass
    elif n == m:
        return(myfact(n))
    else:
        return(int(myfact(n)/myfact(n-m)))



# 求组合
def myfact3(a,b):
    if a < b:
        pass
    elif a == b:
        return 1
    else:
        return(int((myfact(a)/myfact(a-b))/myfact(b)))

# l = myfact2(n_raw,m_raw)
# print("排列值为：",l)

# t = myfact3(n_raw,m_raw)
# print("组合值为：",t)
        

raw_floor = int(input("请输入楼梯层数："))


def floor(n_floor):
    if n_floor % 2 ==0:
        n_value = 0
        for i in range(0,int(n_floor/2)+1):
            n_value = n_value + myfact3(n_floor - i,i)
        return n_value
    else:
        n_value = 0
        for i in range(0,int((n_floor-1)/2)+1):
            n_value = n_value + myfact3(n_floor - i,i)
        return n_value

raw_value = floor(raw_floor)
print("爬楼方式有：",raw_value)
    
