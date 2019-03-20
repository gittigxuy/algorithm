# -*- coding:utf-8 -*- 
__author__ = 'xuy'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class solution:
    def removeElements(self,head,val):
        # 设置头节点
        h=ListNode(-1)
        h.next=head
        pre=h
        cur=head

        while cur:
            if cur.val==val:
                pre.next=cur.next
                cur=cur.next
            else:
                pre=cur
                cur=cur.next

        return h.next