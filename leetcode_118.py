# -*- coding:utf-8 -*-


'''
打印杨辉三角

'''


def numRows(n):
    numslist = [[1]]
    for i in range (2,n+1):
        numslist.append([1]*i)    #这一步最关键，先把列表长度先固定，用1填充
        #print(numslist)
        for j in range(1,i-1):
            numslist[i-1][j] = numslist[i-2][j]+numslist[i-2][j-1]
    return numslist

n_raw = int(input("请输入杨辉三角的层数 n："))
nums = numRows(n_raw)
print(nums)        
