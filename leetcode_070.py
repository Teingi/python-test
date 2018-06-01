# -*- coding:utf-8 -*-

'''
假设你正在爬楼梯。需要 n 步你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

'''

raw_floor = int(input("请输入楼梯层数："))

def climbStairs(n):
        # write your code here
        if n == 0: return 1
        if n == 1: return 1
         
        tmpList = [1,1]
        for i in range(0,n-1):
            x = tmpList[-1] + tmpList[-2]
            tmpList.append(x)
        return tmpList[-1]

raw_value = climbStairs(raw_floor)
print("爬楼方式有：",raw_value)
