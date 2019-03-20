# -*- coding:utf-8 -*- 
__author__ = 'xuy'

"""
问题描述：对于链表元素进行排序
时间复杂度是Ｏ(nlogN)

使用归并排序的方法：
reference:https://blog.csdn.net/qq_34364995/article/details/80994110
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class solution:

    def get_mid(self,head):
        if head is None:
            return head
        fast,slow=head,head
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
        # 注意和876题目的区别，如果链表长度是偶数，那么返回前一个节点，如果链表长度是奇数，返回中间节点
        # eg:长度为５，返回３，长度为６返回3
        return slow
    def sortList(self,head):
        if head is None or head.next is None:
            return head
        mid=self.get_mid(head)
        left=head
        right=mid.next
        # 此时就拆分为left链表和right链表两个节点
        mid.next=None

        left=self.sortList(left)
        right=self.sortList(right)
        # 合并左右两个部分的链表
        return self.merge(left,right)



    def merge(self,l1,l2):
        # l1表示左半部分链表,l2表示右半部分链表
        h=ListNode(-1)
        # 采用尾插法，也就是在链表的后面的节点进行插入
        tail=h
        while l1 and l2:
            if l1.val <l2.val:
                tail.next=l1
                l1=l1.next
            else:
                tail.next=l2
                l2=l2.next
            tail=tail.next
        if l1:
            tail.next=l1
        if l2:
            tail.next=l2
        return h.next


