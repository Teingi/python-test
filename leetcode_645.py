#leetcode 645. 错误的集合


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_list = sorted(nums)
        i = 0
        List = []
        while i < len(nums):
            if nums_list[i] == nums_list[i+1]:
                List.append(nums_list[i])
                break
            else:
                i += 1
        List_raw = [i for i in range(1,len(nums)+1)]
        res = set(List_raw).difference(set(nums_list))
        List = List + list(res)
        return List
