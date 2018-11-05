# leetcode 724. 寻找数组的中心索引



class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        sum_nums = sum(nums)
        for i in range(len(nums)):
            if not d:
                d[i] = 0
            else:
                d[i] = d[i-1] + nums[i-1]
            if d[i] * 2 + nums[i] == sum_nums:
                return i
        return -1
