# -*- coding:utf-8 -*- 
__author__ = 'xuy'
import itertools



class Solution(object):
    def ops(self,op,x,y):
        if op=='+':
            return x+y
        elif op=='-':
            return x-y
        elif op=='*':
            return x*y
    def ways(self,s):
        ans=[]
        for i in range(len(s)):
            if s[i] in "+-*":
                # 采用分治的方法，调用itertools.product表示笛卡尔积，reference:https://blog.csdn.net/qq_33528613/article/details/79365291
                ans+=[self.ops(s[i],left,right)for left,right in itertools.product(self.ways(s[0:i]),self.ways(s[i+1:]))]
        # 如果没有结果，那么返回第一个元素
        if not ans:
            ans.append(int(s))
        return ans
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        return self.ways(input)

# solu=Solution()
# print(solu.diffWaysToCompute('2-1-1'))
# print(solu.diffWaysToCompute('2*3-4*5'))

solu=Solution()
print(solu.diffWaysToCompute('2-1*3'))
# print(solu.diffWaysToCompute('2*3-4*5'))
