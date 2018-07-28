#leetcode 111. 二叉树的最小深度

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        elif root.left == None and root.right != None:
            return self.minDepth(root.right)+1
        elif root.right ==None and root.left != None:
            return self.minDepth(root.left)+1
        elif root.left != None and root.right !=None:
            return min(self.minDepth(root.left), self.minDepth(root.right))+1
