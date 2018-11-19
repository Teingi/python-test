#leetcode 832. 翻转图像


class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            A[i] = A[i][::-1]
        for m in range(len(A)):
            for n in range(len(A[0])):
                if A[m][n] == 0:
                    A[m][n] = 1
                elif A[m][n] == 1:
                    A[m][n] = 0
        return A
