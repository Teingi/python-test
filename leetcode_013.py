#leetcode 13. 罗马数字转整数

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        convert={'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1} 
        for i in range(len(s)-1):
            #if (s[i]=='I' or s[i]=='X' or s[i]=='C') and convert[s[i]]<convert[s[i+1]]:
            if convert[s[i]]<convert[s[i+1]]:
                sum=sum-convert[s[i]]
            else:
                sum=sum+convert[s[i]]
        return sum+convert[s[-1]]
