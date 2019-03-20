# -*- coding:utf-8 -*- 
__author__ = 'xuy'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class solution:
    def mergeLinkList(self,l1,l2):
        # 新创建一个链表头结点，然后使用该头结点合并l1和l2链表
        new_head=ListNode(-1)

        cur_l1=l1
        cur_l2=l2
        new_point=new_head

        while cur_l1 and cur_l2:
            # 插入l1链表元素
            if cur_l1.val <= cur_l2.val:
                new_point.next=cur_l1
                cur_l1=cur_l1.next
            else:
                new_point.next=cur_l2
                cur_l2=cur_l2.next
            new_point=new_point.next

        # 插入l1或者l2后面的元素
        if cur_l1:
            new_point.next=cur_l1
        if cur_l2:
            new_point.next=cur_l2
        # 返回第一个节点
        return new_head.next


    # def mergeLinkList2(self,l1,l2):
    #     if l1 is None or l2 is None:
    #         return l1 if l1 is None else l2
    #     if l1.val<l2.val:
    #         l1.next=self.mergeLinkList2(l1.next,l2)
    #         return l1
    #     else:
    #         l2.next=self.mergeLinkList2(l1,l2.next)
    #         return l2



def init_linklist(data,num_data):
    # 添加链表的头节点
    head=ListNode(None)
    point=head
    for i in range(num_data):
        point.next=ListNode(data[i])
        point=point.next
    # 最后尾指针设置为空
    point.next=None
    return head.next

data1=[1,2,4]
data2=[1,3,4]

head1=init_linklist(data1,len(data1))
head2=init_linklist(data2,len(data2))
solu=solution()
result_head=solu.mergeLinkList(head1,head2)
while result_head:
    print(result_head.val)
    result_head=result_head.next


