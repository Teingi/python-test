#leetcode 693. 交替位二进制数


class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        Str = bin(n)[2:]
        Str1 = Str[::2]
        if len(Str) > 1:
            Str2 = Str[1::2]
            if (len(set(Str2)) == 1) and (len(set(Str1))== 1) and (set(Str1) != set(Str2)):
                return True
            else:
                return False
        elif len(Str) == 1:
            return True
