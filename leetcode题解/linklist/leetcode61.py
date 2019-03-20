# -*- coding:utf-8 -*- 
__author__ = 'xuy'

"""
链表向右移动k个元素
"""

class LinkNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution:
    def RotateRight(self,head,k):
        """
        一共step
        1)遍历到链表尾节点
        ２）形成环
        ３）q从头指针开始移动，移动到新链表的尾部节点，一共移动length-k-1次
        """
        if not head:
            return None
        p=head
        length=1
        # 获取链表长度,从头指针开始，因为第一个链表的长度是１而不是０，因此循环结束的条件是p指向尾指针
        while p.next:
            p=p.next
            length+=1
        # 形成环形链表
        p.next=head
        k%=length
        q=head
        #尾指针q需要移动的次数：length-k-1
        for _ in range(length-k-1):
            q=q.next
        #ans表示新链表的头指针
        ans=q.next
        q.next=None
        return ans
    def RotateLeft(self,head,k):
        if not head:
            return None
        p=head
        length=1
        #获取链表长度,此时p指向链表的结尾
        while p.next:
            p=p.next
            length+=1
        # 构成环
        p.next=head
        k %= length
        q = head
        #找到尾指针q需要移动的长度不同，
        # 左移动是k-1次，因此头指针移动k次
        # 右移动是length-k-1次，因此头指针移动length-k次
        for _ in range(k-1):
            q=q.next
        ans=q.next
        q.next=None
        return ans



def init_linklist(data,num_data):
    head=LinkNode(None)
    point=head
    for i in range(num_data):
        point.next=LinkNode(data[i])
        point=point.next
    # 最后尾指针设置为空
    point.next=None
    return head.next

if __name__=='__main__':
    solu=Solution()
    data=[1,2,3,4,5]
    k=2
    head=init_linklist(data,len(data))
    head=solu.RotateRight(head,k)
    # head=solu.RotateLeft(head,k)

    while head:
        print (head.val)
        head=head.next

