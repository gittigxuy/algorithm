# -*- coding:utf-8 -*- 
__author__ = 'xuy'

"""
题目描述：
找到两个字符串是否经过swap之后是相等的，因此我们可以
"""

class solution:
    def isAnagram(self,s,t):
        if len(s)!=len(t):
            return False
        s=list(s)
        t=list(t)

        s=sorted(s)
        t=sorted(t)
        return s==t

