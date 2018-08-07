#leetcode 191. 位1的个数

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = 0
        Str = bin(n)[2:]
        for i in range(len(Str)):
            if Str[i] == '1':
                m += 1
        return m
