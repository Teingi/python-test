#leetcode 169. 求众数

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = set(nums)
        for num in set_nums:
            if nums.count(num) > len(nums) // 2:
                return num
