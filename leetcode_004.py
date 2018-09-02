#leetcode 4. 两个排序数组的中位数


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        if len(nums) % 2 == 0:
            res = (nums[len(nums)//2 - 1] + nums[len(nums)//2]) / 2.0
        else:
            res = nums[len(nums)//2]
        return res
