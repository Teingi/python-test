# leetcode 415. 字符串相加

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        dic = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9,}
        num_a = 0
        num_b = 0
        for i in range(len(num1)):
            num_a = num_a + dic[num1[i]] * (10**(len(num1) - i -1))
        for i in range(len(num2)):
            num_b = num_b + dic[num2[i]] * (10**(len(num2) - i -1))
        return str(num_a + num_b)
