# leetcode 696. 计数二进制子串


class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = list(map(len, s.replace('01', '0 1').replace('10', '1 0').split(' ')))
        res = sum(min(a,b) for a,b in zip(L, L[1:]) )
        return res
