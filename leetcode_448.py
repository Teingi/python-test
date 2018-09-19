# leetcode 448. 找到所有数组中消失的数字

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        while i < len(nums):
            if nums[i] != nums[nums[i] - 1]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
            else:
                i += 1

        res = []
        for i in  range(len(nums)):
            if i + 1 != nums[i]:
                res.append(i+1)
        return res
