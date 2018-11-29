#  105. 从前序与中序遍历序列构造二叉树

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder==[]:
            return None
        root = TreeNode(preorder[0])
        x = inorder.index(root.val)#找到根在中序中的位置
        root.left=self.buildTree(preorder[1:x+1],inorder[0:x])
        root.right=self.buildTree(preorder[x+1:],inorder[x+1:])
        return root
