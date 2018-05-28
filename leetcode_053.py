# -*- coding: utf-8 -*-


'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组
（子数组最少包含一个元素），返回其最大和.


解：
1、定义两个变量，一个用来存储之前的累加值，一个用来存储当前的最大和。遍历数组中的每个元素，假设遍历到第i个数时：
①如果前面的累加值为负数或者等于0，那对累加值清0重新累加，把当前的第i个数的值赋给累加值。
②如果前面的累加值为整数，那么继续累加，即之前的累加值加上当前第i个数的值作为新的累加值。

'''

def function(lists):
    max_sum = lists[0]
    pre_sum = 0
    for i in lists:
        if pre_sum < 0:
            pre_sum = i
        else:
            pre_sum += i
        if pre_sum > max_sum:
            max_sum = pre_sum
    return max_sum


def main():
    lists = [6,-3,1,-2,7,-15,1,2,2]
    print(function(lists))


if __name__ == "__main__":  
    main()  
    
