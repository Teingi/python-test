#leetcode 821. 字符的最短距离


class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        List = self.indexChar(S,C)
        result = []
        for i in range(len(S)):
            result.append(min(abs(i-k) for k in List))
        return result
        
        
    def indexChar(self,S,C):
        """
        找出S中C的所有下标索引
        """
        res = []
        if len(S) == 0 or (C not in S):
            return -1
        for i in range(len(S)):
            if S[i] == C:
                res.append(i)
        return res
