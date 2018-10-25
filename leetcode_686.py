##leetcode 686. 重复叠加字符串匹配


class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        x,y=len(A),len(B)
        for i in range(y//x,int((y+2*x-2)//x)+1):
            if (A*i).find(B)!=-1:
                return i
        return -1
