# -*- coding:utf-8 -*- 
__author__ = 'xuy'

"""
题目描述：找到排列当中比当前数大的元素
"""
class solution:
    def nextPermutation(self,nums):
        i=j=r=len(nums)-1
        # 从后往前移动，找到不是逆序的index
        while i>0 and nums[i]<=nums[i-1]:
            i-=1
        i-=1
        if i>=0:
            # 从后往前遍历,找到不是逆序的index
            while j>=i and nums[j]<=nums[i]:
                j-=1
            # swap
            nums[i],nums[j]=nums[j],nums[i]

        i+=1
        while i<r:
            nums[i],nums[r]=nums[r],nums[i]
            i+=1
            r-=1

nums=[1,2,9,5]
solu=solution()
solu.nextPermutation(nums)
print(nums)


