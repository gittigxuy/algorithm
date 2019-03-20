# -*- coding:utf-8 -*- 
__author__ = 'xuy'

"""
reference:https://github.com/yingl/LintCodeInPython/blob/master/subarray_sum_closest.py
描述
中文
English
给定一个整数数组，找到一个和最接近于零的子数组。返回第一个和最右一个指数。你的代码应该返回满足要求的子数组的起始位置和结束位置

您在真实的面试中是否遇到过这个题？  
样例
给出[-3, 1, 1, -3, 5]，返回[0, 2]，[1, 3]， [1, 1]， [2, 2] 或者 [0, 4]。

挑战
O(nlogn)的时间复杂度
"""

def subarraySumClosest(data,data_num):
    if not data:
        return []
    sums=[]
    #前缀和的数值
    tmp=0
    #求出所有的前缀和
    for i in range(data_num):
        tmp+=data[i]
        #[前缀和,index]
        sums.append([tmp,i])
    #时间复杂度：O(NlogN)
    sums.sort()
    ret=[0,0]
    diff = 2147483647
    for i in range(1, len(sums)):
        #找出相邻元素的差的最小值
        if abs(sums[i][0] - sums[i - 1][0]) < diff:
            diff = abs(sums[i][0] - sums[i - 1][0])
            ret = []
            ret.append(min(sums[i][1], sums[i - 1][1]) + 1)#append起始index
            ret.append(max(sums[i][1], sums[i - 1][1]))#append终止index
    return ret

num_data=[-3, 100, 14, -3, 5]
#sums=[[-3, 0], [-2, 1], [-1, 2], [-4, 3], [1, 4]]
#sorted:[[-4, 3], [-3, 0], [-2, 1], [-1, 2], [1, 4]]
li=list(num_data)
print(subarraySumClosest(num_data,len(num_data)))

