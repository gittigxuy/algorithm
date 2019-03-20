# -*- coding:utf-8 -*- 
__author__ = 'xuy'

"""
题目描述：链表重排
input:
1->2->3->4->5
result:
1->5->2->4->3
"""

#方法１：链表转化为数组
class LinkNode:
    def __init__(self,x):
        self.val=x
        self.next=None

# 返回一个保存链表指针的list
def copy_linklist(head):
    if not head:
        return
    list_tmp=[]
    cur=head
    while cur:
        list_tmp.append(cur)
        cur=cur.next
    return list_tmp[0]
class solution:
    def reorderlist1(self,head):
        if not head:
            return
        list_tmp=[]

        cur=head
        # 将所有的链表中的数据放到list当中
        while cur:
            # 存放当前链表的地址
            list_tmp.append(cur)
            cur=cur.next
        n=len(list_tmp)

        #进行链表的操作，从头扫描到n/2长度
        for i in range(n//2):
            list_tmp[i].next=list_tmp[n-1-i]
            # list_tmp[n-1-i]的后面的指针指向list_tmp[i]的元素，也就是list_tmp[i+1]
            list_tmp[n-1-i].next=list_tmp[i+1]
        #将尾节点指向null
        list_tmp[n//2].next=None
        # 返回头指针
        return list_tmp[0]

#返回链表头指针
def init_linklist(data,num_data):
    head = LinkNode(None)
    point = head
    for i in range(num_data):
        point.next = LinkNode(data[i])
        point = point.next

    return head.next

data=[1,2,3,4,5]
num_data=len(data)
head=init_linklist(data,num_data)
solu=solution()
head=solu.reorderlist1(head)
# head=copy_linklist(head)
# for i in range(len(head)):
#     print(head[i].val)
while head:
    print(head.val)
    head=head.next




