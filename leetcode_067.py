# leetcode 67. 二进制求和

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_new, b_new = int(a,2), int(b,2)
        Sum = a_new + b_new
        Str = bin(Sum)[2:]
        return Str
