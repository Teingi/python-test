# leetcode 11. 盛最多水的容器

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1
        if not height or len(height) == 1 :
            return 0
        res = (r-l)*(height[l] if height[l] < height[r] else height[r])
        
        while l < r:
            if height[l] < height[r] :
                res = res if res > height[l]*(r-l) else height[l]*(r-l)
                l += 1
            else :
                res = res if res > height[r]*(r-l) else height[r]*(r-l) 
                r -=1
        return res
