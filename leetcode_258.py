#leetcode 258. 各位相加


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def addNum(n):
            Sum = 0
            while n > 0:
                Sum = Sum + (n % 10)
                n = n // 10
            return Sum
        
        if num < 10:
            return num
        else:
            while num >= 10:
                res = 0
                res = res + addNum(num)
                num = addNum(num)
            return res
