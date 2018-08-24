# leetcode 680. 验证回文字符串 Ⅱ


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)
        cmp_time=(n+1)//2-1
        i=0
        while i<cmp_time and s[i]==s[n-1-i]:
            i += 1
        if i==cmp_time:return True
        if s[i]==s[n-1-i-1]:
            while i<cmp_time and s[i]==s[n-1-i-1]:
                i += 1
        if s[i+1]==s[n-1-i]:
            while i<cmp_time and s[i+1]==s[n-1-i]:
                i += 1
        if i==cmp_time:return True
        return False
