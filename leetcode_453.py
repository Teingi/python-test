#leetcode 453. 最小移动次数使数组元素相等
#给定一个长度为 n 的非空整数数组，找到让数组所有元素相等的最小移动次数。每次移动可以使 n - 1 个元素增加 1。


'''
分析：逆向思考，每次移动让剩余的n-1个数加1，相当于每次移动让选定的那个数减1， 
所以最少移动次数其实就是所有元素减去最小元素的和

'''

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_raw = sorted(nums)
        Sum = 0
        for i in range(1,len(nums_raw)):
            Sum += (nums_raw[i] - nums_raw[0])
        return Sum
