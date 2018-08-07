# leetoce 202. 快乐数


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 10:
            if n == 1 or n == 7:
                return True
            else:
                return False
        new_n = 0
        while n:
            new_n += (n % 10)**2
            n //= 10
        return self.isHappy(new_n) 
