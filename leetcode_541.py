# leetcode 541. 反转字符串 II

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s) <= k:
            return s[::-1]
        elif (k < len(s)) and (len(s) < 2*k):
            return s[0:k][::-1] + s[k:]
        else:
            return s[0:k][::-1] + s[k:2*k] + self.reverseStr(s[2*k:], k)
