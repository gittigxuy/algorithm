# -*- coding:utf-8 -*- 
__author__ = 'xuy'

'''
链表的基本操作，注意边界条件
'''
class ListNode:
    def __init__(self, x,_next=None):
        self.val = x
        self.next = _next

class MyLinkedList(object):

    """
    设置头尾指针
    """
    def __init__(self):
        # 创建头指针，尾指针
        self.head=self.tail=None
        # 链表大小
        self.count=0
    #ｉｎｄｅｘ表示链表的下标，从０开始
    # index的正常取值范围是【０,count-1】
    def get(self,index):
        #如果当前链表没有元素或者元素个数小于index,返回-1
        if index>=self.count or index<0:
            return -1
        # 新创建一个头结点，此时第０个元素是头结点，第index个元素就是所需要获取的值
        cur=ListNode(-1,self.head)
        for i in range(index+1):
            cur=cur.next
        return cur.val

    # 在头结点添加元素
    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """

        # 创建一个头节点，,相当于
        # new_head.val=val
        # new_head.next=self.head
        new_head=ListNode(val,self.head)
        self.head=new_head
        if self.count==0:
            self.tail=new_head
        self.count+=1


    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """

        new_tail=ListNode(val,None)
        if self.count==0:
            self.head=self.tail=new_tail
        else:
            self.tail.next=new_tail
            # 更新tail 指针
            self.tail=new_tail
            self.count+=1

    # 插入元素
    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index<0 or index>self.count:
            return
        if index==0:
            return self.addAtHead(val)
        if index==self.count:
            return self.addAtTail(val)
        # 创建头结点
        pre=ListNode(-1,self.head)
        # 找到插入元素的前缀链表节点
        for i in range(index):
            pre=pre.next
        #相当于：一共进行了两步：第一步是赋值，第二步是
        # new_node.val=val,
        # new_node.next=pre.next
        new_node=ListNode(val,pre.next)

        pre.next=new_node
        self.count+=1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        # 越界判断
        if index<0 or index>=self.count:
            return
        pre=ListNode(-1,self.head)
        for i in range(index):
            pre=pre.next
        # 删除节点方法１
        # pre.next=pre.next.next
        # 删除节点方法２
        cur=pre.next
        pre.next=cur.next
        cur=cur.next
        # 头节点
        if index==0:
            self.head=pre.next
        #尾节点
        if index==self.count-1:
            self.tail=pre
        self.count-=1







#
# def init_linklist(data,num_data):
#     # 添加链表的头节点
#     head=ListNode(-1,None)
#     point=head
#     for i in range(num_data):
#         point.next=ListNode(data[i])
#         point=point.next
#     # 最后尾指针设置为空
#     point.next=None
#     return head.next

obj=MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(index=1,val=2)
print(obj.get(0))
print(obj.get(1))
print(obj.get(2))
obj.deleteAtIndex(0)
print(obj.get(0))
