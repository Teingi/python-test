#leetcode 171. Excel表列序号


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
        Str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(len(s)):
            n = n + (Str.index(s[i])+1) * (26 ** (len(s) - i -1))
        return n
