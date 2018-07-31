# leetcode 7. 反转整数

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            new = int(str(x)[::-1])
            if new > 2**31 -1:
                new = 0
            return new
        elif x == 0:
            return 0
        else:
            new = 0 - int(str(abs(x))[::-1])
            if new < - (2**31 -1):
                new = 0
            return new
