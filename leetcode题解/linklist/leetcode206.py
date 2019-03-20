# -*- coding:utf-8 -*- 
__author__ = 'xuy'

"""
链表逆序,结合leetcode92一起看
"""

class LinkNode:
    def __init__(self,x):
        self.val=x
        self.next=None

# reference:https://www.youtube.com/watch?v=esl_A_pzBcg
# 很形象
class Solution:
    """
    解题思路：
    step1:先生成一个空指针pre
    None->1 ->  2->  3->  4

    pre <-cur   lat
          pre <-cur   lat


                       <-  pre  cur  lat ＃此时cur已经跳出循环了
    step2:
    将cur.next指向pre
    step3:
    将pre后移到cur
    step4:
    将cur后移到lat
    """
    def reverse_linklist(self,head):
        if not head:
            return None
        cur=head
        # pre存储的是逆置之后的链表节点，
        # lat是cur的后面一个节点
        pre=None
        # 遍历到结尾
        while cur:
            lat=cur.next
            cur.next=pre
            # pre向后移动
            pre=cur
            # ｃｕｒ向后移动
            cur=lat
        return pre

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
solu=Solution()
head=init_linklist(data,num_data)
head=solu.reverse_linklist(head)
while head:
    print(head.val)
    head=head.next