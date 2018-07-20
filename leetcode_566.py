#leetcode 566. 重塑矩阵


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        List = []
        List_new = []
        if len(nums)*len(nums[0]) != r*c:
            return nums
        else:
            for i in range(len(nums)):
                List += nums[i]
            for j in range(len(List)/c):
                List_new.append(List[j*c:(j+1)*c])
            return List_new
