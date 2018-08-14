#leetocde 268. 缺失数字


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) + 1
        List = [i for i in range(n)]
        res = list(set(List).difference(set(nums)))
        return res[0]
