#leetcode367. 有效的完全平方数

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left=0;right=num
        while left<right:
            mid=(left+right)//2
            if num<mid**2:
                right=mid
            else:
                left=mid+1
        if left>1:
            sqrt_num=left-1
        else:
            sqrt_num=left
        return sqrt_num**2==num
