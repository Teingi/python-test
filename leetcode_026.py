# -*- coding:utf-8 -*-
'''
函数的主要功能是输入一组数字串，对这组数字串进行删重和排序

'''

nums_raw = input("请输入数组序列,以空格区分：")


#定义删除重复元素的函数
def delete_num(nums):
    nums_new = list(nums_raw.split(" "))
    num_set = set(nums_new)
    num_sort = sorted(num_set)
    return num_sort


#定义转换字符串为数字并排序的函数
def trans(s):
    num = []
    for i in range(0,len(s)):
        num.append(int(s[i]))
    num_sort = sorted(num)
    return num_sort



nums_del = delete_num(nums_raw)
num_trans = trans(nums_del)
print("整理后数组长度为：",len(num_trans))
print("整理后数组列表为：",num_trans)


