# -*- coding:utf-8 -*-

'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

'''


def trans(price_s):
    price_str = price_s.split(" ")
    price_list = []
    for i in range (len(price_str)):
        price_list.append(int(price_str[i]))
    return price_list


def maxProfit(prices):
    list_price = []
    for i in range (len(prices)):
        for j in range(i+1,len(prices)):            
            if prices[i] >= prices[j]:
                list_price.append(0)
            else:
                list_price.append(int(prices[j] - prices[i]))
                #return list_price
    return list_price


price_nums = input("请输入一组数据，以空格区分：")
list_price1 = trans(price_nums)
# print(list_price1)
max_list = maxProfit(list_price1)
# print(max_list)
#max_max = sorted(max_list)
#print(max_max[len(max_max)-1])

print(max(max_list))


    
