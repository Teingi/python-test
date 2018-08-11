#leetcode 219. 存在重复元素 II



class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
       
        num_map={}
        for i in xrange(len(nums)):
            if nums[i] in num_map and i-num_map[nums[i]]<=k:
                return True
            else:
                num_map[nums[i]]=i
        
        return False
