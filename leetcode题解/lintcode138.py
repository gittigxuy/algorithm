# -*- coding:utf-8 -*- 
__author__ = 'xuy'
# https://www.lintcode.com/problem/subarray-sum/description
#reference:https://github.com/yingl/LintCodeInPython/blob/master/subarray_sum.py

"""
采用前缀和的思想

样例 1:
	输入: [-3, 1, 2, -3, 4]
	输出: [0,2] 或 [1,3]
	
	样例解释：
	返回任意一段和为0的区间即可。

样例 2:
	输入: [-3, 1, -4, 2, -3, 4]
	输出: [1,5]
"""

#时间复杂度：O(N^2)
def subarraySum(data,num_data):
    for i in range(num_data):
        sum=data[i]
        if sum==0:
            return [i,i]
        #遍历[i+1...最后]
        for j in range(i+1,num_data):
            sum+=data[j]
            if sum==0:
                return [i,j]


num_data=[-3, 1, 2, -3, 4]
li=list(num_data)
print(subarraySum(li,len(li)))


