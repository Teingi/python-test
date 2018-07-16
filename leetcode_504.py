# leetcode 504. 七进制数


class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 0
        else:
            res = ''
            n = abs(num)
            while n:
                res = str(n%7) + res
                n = n/7
            return res if num>0 else '-'+res
