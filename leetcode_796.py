# leetcode 796. 旋转字符串


class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):return False
        elif len(A) == len(B) == 0:return True
        List = []
        List.append(A)
        for i in range(1,len(A)-1):
            List.append(A[i] + A[i+1:] + A[:i])
        List.append(A[-1] + A[:len(A)-1])
        if B in List:
            return True
        return False
