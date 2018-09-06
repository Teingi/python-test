# leetcode 16. 最接近的三数之和

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = sum(nums[:3])
        m = abs(res - target)
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l < r:
                temp = nums[i] + nums[l] +nums[r]
                if abs(res - target) > abs(temp-target):
                    res = temp
                elif target < temp:
                    r -=1
                else :
                    l +=1
        return res
