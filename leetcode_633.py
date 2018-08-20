# leetcode 633. 平方数之和


class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if int(c**0.5) == c**0.5:
            return True
        else :
            heigh = int(c**0.5)
        low = 1
        while  low <= heigh:
            if low**2 + heigh**2 > c:
                heigh -= 1
            elif low**2 + heigh**2 <c:
                low += 1
            else :
                return True
        return False
