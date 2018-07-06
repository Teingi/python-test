#leetcode 409. 最长回文串

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        resoult={}
        for i in s:
            resoult[i]=s.count(i)
        num = 0
        resoult_q = 0
        for keys in resoult:
            if resoult[keys] % 2 == 0:
                num = num + resoult[keys]
            elif resoult[keys] % 2 != 0 and resoult[keys] > 1:
                num = num + resoult[keys] - 1
                resoult_q += 1
            else:
                resoult_q += 1
        if resoult_q > 0:
            return num+1
        else:
            return num
