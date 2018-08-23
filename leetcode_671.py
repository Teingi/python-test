# leetcode 671. 二叉树中第二小的节点



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        s = set()
        queue = [root]
        while queue and queue[0]:
            node = queue.pop(0)
            s.add(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if len(s) < 2:
            return -1
        else:
            s.remove(min(s))
            return min(s)
