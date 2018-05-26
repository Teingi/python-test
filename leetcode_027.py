# -*- coding:utf-8 -*-

'''
给定一个数组 nums 和一个值 val，
你需要移除所有数值等于 val 的元素，
返回移除后的数组。

'''

nums_raw0 = input("输入数字列表，以空格区分：")
nums_raw = nums_raw0.split(" ")
val_raw = int(input("请输入需移除的数字："))
#print(val_raw)


#转换字符串为数字列表函数
def trans(nums_a):
    nums_new = []
    for i in range(0,len(nums_a)):
        nums_new.append(int(nums_a[i]))
    return nums_new


nums = trans(nums_raw)
#print(nums)
if val_raw in nums:
    while val_raw in nums:
        nums.remove(val_raw)
    print("移除后新的数字列表：",nums)
else:
    print("输入的删除数字有误！！！")
        





