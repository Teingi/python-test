#leetcode 110. 平衡二叉树


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        elif abs(self.height(root.left)-self.height(root.right))>1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def height(self,root):
        if root == None:
            return 0
        else:
            return max(self.height(root.left),self.height(root.right))+1
