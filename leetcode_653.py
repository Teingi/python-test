# leetcode 653. 两数之和 IV - 输入 BST



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        s = set()
        queue = [root]
        while queue:
            node = queue.pop(0)
            s.add(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        for num in s:
            if k - num in s and 2 * (k - num) != k:
                return True
        return False
