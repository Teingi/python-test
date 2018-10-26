#leetcode 687. 最长同值路径
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    maxLen = 0
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.getMaxLen(root, root.val)
        return self.maxLen
    
    def getMaxLen(self, root, val):
        if not root:
            return 0
        left = self.getMaxLen(root.left, root.val)
        right = self.getMaxLen(root.right, root.val)
        self.maxLen = max(self.maxLen, left + right)
        if root.val == val:
            return max(left, right) + 1
        return 0
