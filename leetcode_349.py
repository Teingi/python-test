#leetcode 349
#给定两个数组，写一个函数来计算它们的交集。

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) <= len(nums2):
            list_raw1 = []
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    list_raw1.append(nums1[i])
            return list(set(list_raw1))
        else:
            list_raw2 = []
            for i in range(len(nums2)):
                if nums2[i] in nums1:
                    list_raw2.append(nums2[i])
            return list(set(list_raw2))
