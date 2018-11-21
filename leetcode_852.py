# leetcode 852. 山脉数组的峰顶索引


class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        Max_index = A.index(max(A))
        if (len(set(A[:Max_index])) == Max_index) and (len(set(A[Max_index:])) == len(A) - Max_index):
            return Max_index
