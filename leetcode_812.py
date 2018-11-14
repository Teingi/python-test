# leetcode 812. 最大三角形面积


class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        List = []
        for i in range(len(points)-2):
            for j in range(i+1,len(points)-1):
                for k in range(j+1,len(points)):
                    S = self.TriangleArea(points[i],points[j],points[k])
                    List.append(S)
        return max(List)
                    
        
    def TriangleArea(self,A,B,C):
        """
        给定三个坐标，求三角形面积
        """
        x1,x2,x3 = A[0],B[0],C[0]
        y1,y2,y3 = A[1],B[1],C[1]
        return 0.5 * abs(x2 * y3 + x1 * y2 + x3 * y1 - x3 * y2 - x2 * y1 - x1 * y3)
