#leetcode 492. 构造矩形

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        List = []
        List_last = []
        for i in range(1,int(area**(0.5))+1):
            if area % i == 0:
                List.append(i)
        List_last.append(area/max(List))
        List_last.append(max(List))
        return List_last
