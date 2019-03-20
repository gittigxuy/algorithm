# -*- coding:utf-8 -*- 
__author__ = 'xuy'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 时间复杂度O(N),空间复杂度：O(N/2)
class solution:
    def isPalindrom(self,head):
        # 使用快慢指针
        fast,slow=head,head
        # 创建栈结构
        stack=[]
        # 快慢指针的退出条件
        # 退出条件是fast指向链表的最后一个节点
        while fast and fast.next:
            # 从头开始到链表的中间节点，append　value
            stack.append(slow.val)
            # 快慢指针向后移动
            slow=slow.next
            fast=fast.next.next
        #如果快指针指向了链表当中的最后一个节点，那么slow指针移动到后半部分
        if fast:
            slow=slow.next
        # 此时slow从链表的中间节点移动到链表末尾
        while slow:
            # 元素出栈
            top=stack.pop()
            if top!=slow.val:
                return False
            slow=slow.next
        return True



def init_linklist(data,num_data):
    head=ListNode(None)
    point=head
    for i in range(num_data):
        point.next=ListNode(data[i])
        point=point.next
    # 最后尾指针设置为空
    point.next=None
    return head.next



data=[1,2,2,3,2,1]
num_data=len(data)
solu=solution()
head=init_linklist(data,num_data)
result=solu.isPalindrom(head)
print(result)