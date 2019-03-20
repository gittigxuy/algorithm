# -*- coding:utf-8 -*- 
__author__ = 'xuy'
"""
reference:
"""
class MinStack1():
    def __init__(self):
        self.stack=[]
    def push(self,x):
        self.stack.append(x)
    # 弹出最后的元素
    def pop(self):
        if self.stack is None:
            return
        else:
            return self.stack.pop()
    # 获取最后的元素
    def top(self):
        if self.stack is None:
            return
        else:
            return self.stack[-1]
    def getMin(self):
        if self.stack is None:
            return
        else:
            # 遍历栈中所有的元素
            return min(self.stack)

# 引入min变量，保存最小元素
class Minstack2():
    def __init__(self):
        self.stack=[]
        self.min=None
    def push(self,x):
        self.stack.append(x)
        if self.min is None or self.min>x:
            self.min=x
    def pop(self):
        # 获取pop之后的元素
        popItem=self.stack.pop()
        # 如果弹出之后为空，那么将min置位None，返回弹出之后的节点
        if len(self.stack)==0:
            self.min=None
            return popItem
        # 如果弹出的节点为最小值，那么还需要找到剩余的stack当中的最小值，更新min
        if popItem==self.min:
            # 假设最小值是第一个元素
            self.min=self.stack[0]
            #遍历弹出之后的栈，找到最小值
            for i in self.stack:
                if i<self.min:
                    self.min=i
        return popItem

    # ERROR
    # def pop(self):
    #     if self.min==self.stack[-1]:
    #         self.min=self.stack[0]
    #         for i in self.stack[:-1]:
    #             if i<self.min:
    #                 self.min=i
    #     return self.stack.pop()

    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.min

# 引入min栈，类似于方法２
# reference:https://blog.csdn.net/AntiZheng/article/details/82746006

class MinStack3(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.stack_min = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.stack_min == [] or self.stack_min[-1] >= x:
            self.stack_min.append(x)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack_min[-1] == self.stack[-1]:
            self.stack_min.pop()
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack_min[-1]