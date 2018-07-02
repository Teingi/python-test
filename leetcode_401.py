#leetcode 401. 二进制手表

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        #遍历方法，复杂度高
        res=[]
        for hour in range(12):
            for minute in range(60):
                if (bin(hour)+bin(minute)).count('1')==num:#统计hour与minute的二进制1有多少，即表示亮灯有多少
                    res.extend(["%d:%02d"%(hour,minute)])
        return res
