# leetcode 628. 三个数的最大乘积


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max_value1=nums[-3]*nums[-2]*nums[-1]
        max_value2=nums[0]*nums[1]*nums[-1]

        return max(max_value1,max_value2)
