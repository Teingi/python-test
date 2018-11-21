# leetcode 849. 到最近的人的最大距离


class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        List = []
        for i in range(len(seats)):
            if seats[i] == 1:
                List.append(i)
        if len(List) == 1:
            return max(len(seats)-List[0]-1,List[0])
        List2 = []
        for m in range(0,len(List)-1):
            List2.append(List[m+1] - List[m])
        if (min(List) > 0) and (max(List) < len(seats) - 1):
            return max(max(List2)/2,List[0],len(seats) - List[-1] - 1)
        elif (min(List) > 0) and (max(List) == len(seats) - 1):
            return max(max(List2)/2,List[0])
        elif (min(List) == 0) and (max(List) < len(seats) - 1):
            return max(max(List2)/2,len(seats) - List[-1] - 1)
        elif (min(List) == 0) and (max(List) == len(seats) - 1):
            return max(List2)/2
