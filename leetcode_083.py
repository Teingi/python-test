# leetcode 83. 删除排序链表中的重复元素

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #此为不带头结点的链表
        if head is None:#链表为空
            return head
        cur=head
        while cur.next:#下一节点不为空
            if cur.val==cur.next.val:#第一次判断，头元素与头元素下一节点的值是否相等。。。
                cur.next=cur.next.next
            else:
                cur=cur.next
        return head
