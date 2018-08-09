# leetcode 203. 删除链表中的节点


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head:
            while head.val == val:
                head = head.next
                if head is None:
                    return head
            q = head
            p = q.next
            while p:
                if p.val == val:
                    q.next = p.next
                else:
                    q = q.next
                p = p.next
        return head
