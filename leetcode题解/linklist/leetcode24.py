# -*- coding:utf-8 -*- 
__author__ = 'xuy'
"""
链表重排
input:1->2->3->4
output:2->1->4->3
https://blog.csdn.net/xiaoling_000666/article/details/78927687
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        h=ListNode(-1)
        h.next=head
        pre=h
        cur=pre.next
        while cur and cur.next:
            pre.next=cur.next
            cur.next=pre.next.next
            pre.next.next=cur

            pre=cur
            cur=cur.next

        return h.next


