#leetcode 762. 二进制表示中质数个计算置位


class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        # L,R 是在 [1,10^6] 中的整数，因此置位的个数最多为 19
        #创建列表 p，0-20 中质数为置 1 ，非质数位置 0

        p = (0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1)
        re = 0
        for n in range(L, R + 1):
            re += p[bin(n).count('1')] 
        return re
