# leetcode 104. 二叉树的最大深度

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:#递归边界
            return 0
        else:
            l=1+self.maxDepth(root.left)#递归
            r=1+self.maxDepth(root.right)
            return max(l,r)
