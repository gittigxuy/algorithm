# -*- coding:utf-8 -*- 
__author__ = 'xuy'
"""
题目描述：
找出根号x的整数部分
"""
class solution:
    '''
    采用二分查找的方式
    '''
    def sqrt1(self,x):
        left=0
        right=x+1
        while left<right:
            middle=left+(right-left)//2
            if middle*middle >x:
                right=middle
            else:
                left=middle+1
        return left-1


solu=solution()
print(solu.sqrt1(9))