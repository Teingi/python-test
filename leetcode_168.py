# leetcode 168. Excel表列名称

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        S = ''
        Str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while n >= 1:
            S = Str[(n % 26) - 1] + S
            n = (n-1) / 26
        return S
