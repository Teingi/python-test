# leetcode 674. 最长连续递增序列


class Solution(object):
    def findLengthOfLCIS(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        index = []
        if length >= 1:
            key = nums.count(nums[0])
            if key == length:
                return 1
            else:
                flag = 1
                for i in range(length):
                    j = i + 1
                    while j < length:
                        if nums[i] < nums[j] and j <= length - 1:
                            flag += 1
                            break
                        else:
                            if i < length -1:
                                index.append(flag)
                                flag = 1
                                break
                            else:
                                return max(index)
                index.append(flag)
            return max(index)
        else:
            return 0
