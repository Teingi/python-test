# leetcode 496. 下一个更大元素 I


class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        m = 0
        List = []
        for i in range(len(findNums)):
            index_num = nums.index(findNums[i])
            if index_num == len(nums) - 1:
                List.append(-1)
            else:
                if max(nums[(index_num + 1):]) < findNums[i]:
                    List.append(-1)
                else:
                    for n in range((index_num + 1),len(nums)):
                        if nums[n] - findNums[i] > 0:
                            List.append(nums[n])
                            break
                        else:
                            pass
        return List
