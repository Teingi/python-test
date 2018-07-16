#leetcode 507. 完美数

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        res = 0
        if num <= 3:
            return False
        else:
            for i in range(1,int(num**0.5)+1):
                if num % i == 0 and i == 1:
                    res = res + 1
                elif num % i == 0 and num/i != i:
                    res = res + i + num/i
                elif num % i == 0 and num/i == i:
                    res = res + i
                else:
                    pass
            if res == num:
                return True
            else:
                return False
