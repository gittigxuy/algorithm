# -*- coding:utf-8 -*- 
__author__ = 'xuy'

"""
求两个链表的交集,没有写测试样例
"""
class solution:
    def getIntersetion(self,headA,headB):
        n1,n2=headA,headB
        # 跳出循环的条件就是，两个指针相等
        while n1!=n2:
            # 如果n1没有到尾节点，那么直接向后移动，如果n1到达尾节点，那么n1指向headB
            n1=n1.next if n1 else headB
            n2=n2.next if n2 else headA

        return n1