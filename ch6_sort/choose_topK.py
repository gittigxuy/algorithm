# -*- coding:utf-8 -*- 
__author__ = 'xuy'



#找出nums当中前k个元素

def topK(nums,k):
    import heapq
    # 从大到小进行排序
    return heapq.nlargest(k,nums)

nums=[2,3,4,5,1,32,12,51,24,13]
print(topK(nums,2))