# leetcode 69. x 的平方根


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        min = 0
        max = x
        mid = x//2
        while min<=max:
            m = mid*mid
            if m>x:
                max = mid-1
            elif m<x:
                min = mid+1
            else:
                return mid
                break
            mid = (min+max)//2
        return mid        
