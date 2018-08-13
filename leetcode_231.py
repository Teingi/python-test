#leetcode 231.2的幂

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        else:
            while n % 2 == 0:
                n = n / 2
            return True if n == 1 else False
