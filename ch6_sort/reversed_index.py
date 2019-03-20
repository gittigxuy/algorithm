# -*- coding:utf-8 -*- 
__author__ = 'xuy'

"""
逆序数问题，i<j,但是data[i]>data[j]
"""

#采用暴力方法，时间复杂度是O(N^2)
def count_reversed_index1(data,num_data):
    count=0
    for i in range(num_data):
        for j in range(i+1,num_data):
            if data[i]>data[j]:
                count+=1

    return count

#采用归并排序的方式，时间复杂度降低到O(NlogN)
#reference:https://blog.csdn.net/contr4l_/article/details/80611675
def count_reversed_index2(data):
    # count=0
    if len(data)<=1:
        return data,0
    mid=len(data)//2
    left,left_count=count_reversed_index2(data[:mid])
    right,right_count=count_reversed_index2(data[mid:])
    list,count=merge(left,right,0)
    # return list,left_count+right_count+count
    return left_count+right_count+count
def merge(left,right,count):
    i,j=0,0
    # 新创建了一个空间复杂度为O(N)的变量
    result = []
    while i < len(left) and j < len(right):
        # 从小到大排序
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count=count+len(left)-i# 当右半部分的元素先于左半部分元素进入有序列表时，逆序对数量增加左半部分剩余的元素数
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result,count




li=[3,56,2,7,45,8,1]
# print(count_reversed_index1(li,len(li)))
print(count_reversed_index2(li))

