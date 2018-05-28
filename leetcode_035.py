# -*- coding:utf-8 -*-


'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

'''


nums_raw = input("请输入一个数组，以空格区分：")
index_raw = int(input("请输入一个目标值："))
nums_new = nums_raw.split(" ")

#转换输入的字符串为整型变量
def trans(num):
    nums_list = []
    for i in range(len(num)):
        nums_list.append(int(num[i]))
    return nums_list

nums_final = sorted(trans(nums_new))
print(nums_final)
#nums_final = sorted(nums_new)


#搜索索引函数
def serachIndex(nums,index):
    if index > nums[-1]:
        return len(nums)
    elif index == nums[-1]:
        return len(muns)-1
    elif index <= nums[0]:
        return 0
    else:
        for i in range(len(nums)):
            while index <= nums[i]:
                return i

index_final = serachIndex(nums_final,index_raw)
print(index_final)

            
