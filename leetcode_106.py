# 106. 从中序与后序遍历序列构造二叉树


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder == []:
            return None
        root = TreeNode(postorder[-1])
        x = inorder.index(root.val)#找到根在中序中的位置
        root.left=self.buildTree(inorder[:x],postorder[:x])
        root.right=self.buildTree(inorder[x+1:],postorder[x:-1])
        return root
