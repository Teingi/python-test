#leetcode 643. 子数组最大平均数 I



from collections import deque
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        s = 0
        ans = float("-inf")#负无穷
        queue = deque([])
        for num in nums:
            queue.append(num)
            s += num
            if len(queue) > k:
                s -= queue.popleft()
            if len(queue) == k:
                ans = max(ans, float(s) / k)
        return ans
