# -*- coding:utf-8 -*- 
__author__ = 'xuy'

"""
输入一个链表＋一个数字x，使用x分隔两个链表

设计思路：新开辟两个头结点指针：less_head和more_head，将小于x的放到less_head节点当中,将大于x的放到moore_head当中
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class solution:
    def partition(self,head,x):
        less_head=ListNode(-1)
        more_head=ListNode(-1)
        # 使用移动指针指向三个头结点
        cur=head
        less_point=less_head
        more_point=more_head
        # 循环结束之后构造了more_head以及less_head的链表
        while cur:
            if cur.val<x:
                less_point.next=cur
                less_point=less_point.next
            else:
                more_point.next=cur
                more_point=more_point.next
            cur=cur.next
        less_point.next=more_head.next
        more_point.next=None
        return less_head.next


def init_linklist(data,num_data):
    head=ListNode(None)
    point=head
    for i in range(num_data):
        point.next=ListNode(data[i])
        point=point.next
    # 最后尾指针设置为空
    point.next=None
    return head.next



data=[1,4,3,2,5,2]
num_data=len(data)
x=3
solu=solution()
head=init_linklist(data,num_data)
head=solu.partition(head,x)
while head:
    print(head.val)
    head=head.next


