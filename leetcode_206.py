#leetcode 206. 反转链表

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        cur = head
        pre = None
        nxt = cur.next
        while nxt:
            cur.next = pre
            pre = cur
            cur = nxt
            nxt = nxt.next
        cur.next = pre
        head = cur
        return head
