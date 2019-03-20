# -*- coding:utf-8 -*- 
__author__ = 'xuy'


"""
使用栈来实现队列操作,可以使用list或者双端队列进行求解
"""

# 使用两个list,python当中list就是栈的数据结构，append表示向后添加元素，pop表示将最后的元素弹出
class MyQueue1:
    def __init__(self):
        # 栈
        self.stack1=[]
        # 中转
        self.stack2=[]
    def push(self,x):
        self.stack1.append(x)

    def pop(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        # 获取并且弹出stack1的第一个元素
        result=self.stack2.pop()
        # 还原stack1中的元素，从stack1的第二个元素开始压入栈
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return result
    # 获取stack1的第一个元素
    def peek(self):
        return self.stack1[0]
    def empty(self):
        return not self.stack1

# 采用双端队列的方式,导入deque
from collections import deque
class MyQueue2:
    def __init__(self):
        """
                Initialize your data structure here.
        """
        self.Myqueue = deque()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.Myqueue.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.Myqueue) > 0:
            return self.Myqueue.popleft()
        else:
            return None

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.Myqueue) > 0:
            return self.Myqueue[0]
        else:
            return None

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.Myqueue) == 0