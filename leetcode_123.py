#leetcode 123 . 买卖股票的最佳时机 III


class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if prices is None or len(prices) < 2:
            return 0
        def Solve(part, t):
            if t == -1:
                part = part[::-1]
            if part is None or len(part) < 2:
                return 0
            Begin_value = part[0]
            result = 0
            for p in part:
                result = max(result, p-Begin_value)
                Begin_value = min(Begin_value, p)
            return result

        begin, index, stop = 0, 0, 1    #开始买入指针，临时指针，结束卖出指针
        Sum, Max = 0, 0
        for i in range(len(prices)-1):
            Sum += prices[i+1]-prices[i]
            if Sum > Max:
                Max = Sum
                stop = i + 1
                begin = index
            Sum = max(0, Sum)
            if Sum == 0:
                index = i + 1
        part_1 = Max + Solve(prices[:begin], 1)
        part_2 = Max + Solve(prices[begin:stop+1], -1)if Max > 0 else 0
        part_3 = Max + Solve(prices[stop+1:], 1)
        #part_2中的判断语句是因为可能出现part_2最大利润Max为0，即递减数组，而第二次交易又在此part，第二次的最大利润>0,矛盾。
        return max(part_1, part_2, part_3)
