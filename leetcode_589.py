# 589. N叉树的前序遍历

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return [];
        if not root.children:
            return [root.val];
        result = [root.val];
        for child in root.children:
            result += self.preorder(child);
        return result;
