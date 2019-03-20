# -*- coding:utf-8 -*- 
__author__ = 'xuy'
"""
删除重复元素，时间复杂度是O(N^2)
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class solution:
    def deleteDuplicates(self,head):
        if head is None or head.next is None:
            return head
        # 也可以创建一个头结点，返回h.next
        pre=None
        cur=head
        while cur:
            pre=cur
            cur=cur.next
            while cur and cur.val==pre.val:
                pre.next=cur.next
                cur=cur.next
        return head



