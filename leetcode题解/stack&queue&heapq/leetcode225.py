# -*- coding:utf-8 -*- 
__author__ = 'xuy'

"""
题目描述：使用队列来实现栈
reference:https://blog.csdn.net/qq_34364995/article/details/80640470
"""
# 方法１：使用列表
class Mystack:
    def __init__(self):
        self.stack=[]
    def push(self,x):
        self.stack.append(x)
    def pop(self):
        if self.stack is not None:
            return self.stack.pop()
        else:
            return False
    def top(self):
        # 返回最后一个元素
        if self.stack is not None:
            return self.stack[-1]
        else:
            return False
    def empty(self):
        if self.stack==[]:
            return True
        else:
            return False