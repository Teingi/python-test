#leetcode 908. 最小差值 I


class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if len(A) == 1:
            return 0
        res = max(A) - min(A)
        if res >= 2*K:
            return res -2*K
        else:
            return 0
