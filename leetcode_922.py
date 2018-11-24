#leetcode 922. 按奇偶排序数组 II



class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res1, res2 = [], []
        res = []
        for item in A:
            res1.append(item) if item % 2 == 0 else res2.append(item)
        for i in range(len(res1)):
            res.append(res1[i])
            res.append(res2[i])
        return res
