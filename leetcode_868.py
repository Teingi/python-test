#leetcode 868. 二进制间距

class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        Str = bin(N)[2:]
        List = []
        res = []
        for i in range(len(Str)):
            if Str[i] == '1':
                List.append(i)
        if len(List) <= 1:
            return 0
        for j in range(1,len(List)):
            res.append(List[j] - List[j-1])
        return max(res)
