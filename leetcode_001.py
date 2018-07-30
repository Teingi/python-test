#leetcode 1. 两数之和

class Solution:
    def twoSum(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for x in range(n):
            for y in range(x+1,n):
                if nums[y] == target - nums[x]:
                    return x,y
                    break
                else:
                    continue
