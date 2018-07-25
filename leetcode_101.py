# leetcode 101. 对称二叉树


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSameTree(p,q):
            if not p and not q:#两二叉树皆为空，递归边界，两者皆为空返回真  
                return True  
            if p and q and p.val==q.val:  
                l=isSameTree(p.left,q.right) 
                r=isSameTree(p.right,q.left)  
                return l and r#and操作，需要l与r皆为true时，才返回真。只用最后一次递归边界return值  
            else:  
                return False
        if not root:
            return True
        else:
            return isSameTree(root.left,root.right)
