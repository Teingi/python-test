#leetcode 836. 矩形重叠

class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        if (rec2[0] >= rec1[2]) or (rec2[1] >= rec1[3]) or (rec2[2] <= rec1[0]) or (rec2[3] <= rec1[1]):
            return False
        else:
            return True
