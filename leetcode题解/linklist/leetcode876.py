# -*- coding:utf-8 -*- 
__author__ = 'xuy'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class solution:
    # 不新建头结点
    def middleNode1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 没有空的头结点链表节点
        fast, slow = head, head
        # 这个循环判断有两种情况，
        # １）如果链表长度是奇数，那么循环结束的时候，fast指针指向链表的末尾，slow指针指向　　[ｌｅｎ(链表长度)//2]+1
        # ２）如果链表长度是偶数，那么循环结束的时候，ｆａｓｔ指针指向链表的末尾的next，slow指针指向中间节点的第二个节点
        while fast and fast.next:
            fast = fast.next.next

            slow = slow.next
        return slow
    # 不新建头结点,返回链表长度为偶数的时候，跳出循环的时候slow指向的是中间的第一个节点
    # def middleNode2(self,head):
    #     fast,slow=head,head
    #     #和方法１的区别就是跳出循环的条件不同，因此如果链表长度为偶数的话，跳出循环的时候slow指向的是中间的第一个节点，用来拆分链表
    #     while fast.next and fast.next.next:
    #         fast=fast.next.next
    #         slow=slow.next
    #     return slow.next

    def middleNode2(self,head):
        h=ListNode(-1)
        h.next=head
        fast,slow=h,h
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        # 链表长度为偶数，此时slow指针指向的是中间节点的第一个节点
        if fast:
            return slow.next
        else:
            return slow