# -*- coding:utf-8 -*- 
__author__ = 'xuy'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class solution:
    def has_cycle(self,head):
        if head==None:
            return False
        fast,slow=head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                return True
        return False