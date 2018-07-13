#leetcode 485. 最大连续1的个数

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        List = []
        List_last = []
        for i in range(len(nums)):
            if nums[i] == 0:
                List.append(i)
            else:
                pass
        if len(List) == 0:
            return len(nums)
        else:
            List.insert(0,-1)
            List.append(len(nums))
            for i in range(1,len(List)):
                List_last.append(List[i]-List[i-1])
            return (max(List_last)-1)
