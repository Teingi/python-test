#leetcode 872. 叶子相似的树

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaves1 = []
        leaves2 = []
        self.inOrder(root1, leaves1)
        self.inOrder(root2, leaves2)
        return leaves1 == leaves2
    
    def inOrder(self, root, leaves):
        if not root:
            return
        self.inOrder(root.left, leaves)
        if not root.left and not root.right:
            leaves.append(root.val)
        self.inOrder(root.right, leaves)
