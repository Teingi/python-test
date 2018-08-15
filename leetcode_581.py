# leetcode 581. 最短无序连续子数组


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_List = sorted(nums)
        i = 0
        j = len(nums) - 1
        while (nums_List[i] == nums[i]) and (i < len(nums)-1):
            i += 1
        while (nums_List[j] == nums[j]) and (j > 0):
            j = j - 1
        if j <= i:
            return 0
        else:
            return (j-i+1)
