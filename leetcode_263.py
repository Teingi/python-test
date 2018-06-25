'''
leetcode 263题. 丑数

编写一个程序判断给定的数是否为丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

'''


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num >0 and num%2==0:
            num /= 2
        while num >0 and num%3==0:
            num /= 3
        while num >0 and num%5==0:
            num /= 5
        return True if num == 1.0 else False
