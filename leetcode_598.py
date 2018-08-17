# leetcode 598. 范围求和 II


class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        List_a = []
        List_b = []
        for i in range(len(ops)):
            List_a.append(ops[i][0])
            List_b.append(ops[i][1])
        if (len(List_a) == 0) or (len(List_b) == 0):
            return m*n
        else:
            return min(List_a)*min(List_b)
