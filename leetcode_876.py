# 876. 链表的中间结点


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next is None:
            return [head.val]
        else:
            List = []
            cur = head
            while cur is not None:
                List.append(cur.val)
                cur = cur.next
            return List[len(List)/2 :]
