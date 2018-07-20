# leetcode 561. 数组拆分 I


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_List = sorted(nums)[::2]
        Sum = 0
        for i in range(len(num_List)):
            Sum += num_List[i]
        return Sum
