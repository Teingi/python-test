# 120. 三角形最小路径和

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        res = triangle[-1]
        i = len(triangle) - 2
        while i >= 0:
            for j in range(len(triangle[i])):
                res[j]  = min(res[j], res[j+1]) + triangle[i][j]
            i -= 1
        return res[0]
