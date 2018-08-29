# 590. N叉树的后序遍历

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        if not root.children:
            return [root.val]
        result = []
        for child in root.children:
            result += self.postorder(child)
        result += [root.val]
        return result
