# -*- coding:utf-8 -*- 
__author__ = 'xuy'

"""
在链表中，从m开始到n进行链表的逆置
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class solution:
    def reverselinklist_mn(self,head,m,n):
        # head传入的是链表当中的第一个节点
        if head is None or head.next is None or m>=n or m<0 or n<0:
            return None

        # 创建空的头结点
        h=ListNode(-1)
        h.next=head


        pre=h
        cur=head
        i=1
        # 此时cur指向第m个节点,此时pre指向第m-1个节点
        while i<m and cur:
            pre=cur
            cur=cur.next
            i+=1
        # t1指向第m-1个链表节点，t2指向第m个节点
        # 逆置之后t1仍然指向m-1的节点，t2指向第n个节点
        t1=pre
        t2=cur
        # cur指向第n个节点结束，从第m个节点开始进行逆置
        while i<=n and cur:
            # 链表逆置
            lat=cur.next
            cur.next=pre
            pre=cur
            cur=lat
            i+=1
        # 此时pre指向的是链表逆置之后的头指针
        t1.next=pre
        # 此时cur指向的是链表逆置之后的尾指针
        t2.next=cur
        # 返回的是空的头指针的下一个节点，防止m=1的情况
        return h.next


def init_linklist(data,num_data):
    head=ListNode(None)
    point=head
    for i in range(num_data):
        point.next=ListNode(data[i])
        point=point.next
    # 最后尾指针设置为空
    point.next=None
    return head.next

data=[1,2,3,4,5]
num_data=len(data)
m,n=2,4
solu=solution()
head=init_linklist(data,num_data)
head=solu.reverselinklist_mn(head,m,n)
while head:
    print(head.val)
    head=head.next

