# leetcode 31. 下一个排列


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        if len(list(set(nums))) != 1:
            
            #先从尾部升序结束的点
            while i - 1 >= 0:
                if nums[i] <= nums[i - 1]:
                    i = i - 1
                else:
                    break
            #如果前面还有至少一个位置
            if i - 1 >= 0:
                j = i - 1
 
                t = len(nums) - 1
                #从后往前找第一个大于j位置上的数
                while nums[t] <= nums[j]:
                    t -= 1
                nums[t], nums[j] = nums[j], nums[t]
                a = sorted(nums[i:])
                a_index = 0
                #因为我不知道python分段排序的方法，于是就手动排序
                #以下是对nums的排序
                for index in range(i, len(nums)):
                    nums[index] = a[a_index]
                    a_index += 1
            #没有位置则sort
            else:
                nums.sort()
