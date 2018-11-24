#leetcode 905. 按奇偶排序数组


class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if len(A) == 0:
            return []
        res1, res2 = [],[]
        for item in A:
            if item % 2 == 0:
                res1.append(item)
            elif item % 2 == 1:
                res2.append(item)
        return res1 + res2
