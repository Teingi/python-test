# 747. 至少是其他数字两倍的最大数


class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return 0
        max_num = max(nums)
        res = nums.index(max_num)
        nums.remove(max_num)
        if max_num >= 2 * max(nums):
            return res
        else:
            return -1
        
