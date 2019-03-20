# -*- coding:utf-8 -*- 
__author__ = 'xuy'

"""
最大连续子数组,对应leetcode53题
"""

num_data=[1,-2,3,10,-4,7,2,-5]
li=list(num_data)
"""
方法一：暴力,时间复杂度O(N^3)
"""
def maxsubArray1(data,num):
    maxsum=data[0]
    result_elem=[]
    #最大子数组的起点
    for i in range(num):
        #最大子数组的终点
        for j in range(i,num):
            currentSum=0
            for k  in range(i,j+1):
                currentSum+=data[k]

            if currentSum>maxsum:
                maxsum=currentSum
                #记录最大子数组的起点和终点
                x=i
                y=j
    for result_index in range(x,y+1):
        result_elem.append(data[result_index])
    return maxsum,result_elem

"""
方法二：
我们注意到x[i..j]之和 = x[i..j-1]之和 + x[j]，因此在j的for循环中，可直接求出sum。
时间复杂度降低为O(N^2)
"""
def maxsubArray2(data,num):
    maxSum=data[0]
    # 用来存储符合条件的区间当中所有的元素
    result_elem = []
    for i in range(num):
        currSum=0
        for j in range(i,num):
            currSum+=data[j]
            # maxSum=max(maxSum,currSum)
            if currSum>maxSum:
                maxSum=currSum
                x=i
                y=j
    for result_index in range(x,y+1):
        result_elem.append(data[result_index])
    return maxSum,result_elem



"""
分治法,注意边界
时间复杂度分析：O(NlogN)，具体见pdf
"""
def  maxsubArray3(data,start,end):
    if start==end:
        return data[start]
    middle=(start+end)//2


    #找出中间跨立的最大值
    #先从中间往左扫描，找出左边部分最大值
    # 假定data[middle]是左半部分的最大值
    left_sum=data[middle]
    current_sum=0
    for i in range(middle,start-1,-1):
        current_sum=current_sum+data[i]
        left_sum=max(left_sum,current_sum)
    # 然后从中间往右扫，找出右边部分的最大值，然后再加和
    right_sum=data[middle+1]
    current_sum=0
    for i  in range(middle+1,end+1):
        current_sum=current_sum+data[i]
        right_sum=max(current_sum,right_sum)

    # 递归左边部分的最大值
    m1 = maxsubArray3(data, start, middle)
    # 递归右边部分的最大值
    m2 = maxsubArray3(data, middle+1, end)
    m3=left_sum+right_sum
    return max(m1,m2,m3)


#采用dp方法，时间复杂度是O(N),具体分析 见pdf
#s(i)=max(s[i-1]+data[i],data[i])==>转化为sum与0比较 大小
def maxsubArray4(data,num):
    result=data[0]
    sum=data[0]
    for i in range(1,num):
        #如果当前
        if sum>0:
            sum+=data[i]
        else:
            sum=data[i]

        result=max(sum,result)
    return result

# def maxsubArray5(data,num_data):
#     if not data:
#         return []
#     sums=[]
#     #前缀和的数值
#     tmp=0
#     #求出所有的前缀和
#     for i in range(num_data):
#         tmp+=data[i]
#         #[前缀和,index]
#         sums.append([tmp,i])
#     #求出最小的前缀和
#     min_m=sums[0][0]
#     min_index=0
#     result=sums[0][0]
#     for i in range(1,len(sums)):
#         if min_m>sums[i][0]:
#             min_m=sums[i][0]
#             min_index=i
#
#         # print(result)
#
#         if result<sums[i][0]-min_m:
#             result = sums[i][0] - min_m
#     return result
#         # for j in range(i):
#         # if sums[i][0]<min_m:
#         #     min_m=sums[i][0]
#         #     min_index=i
#     # #求出最大的前缀和
#     # max_m=sums[0][0]
#     # max_index=0
#     # for i in range(1,len(sums)):
#     #     if sums[i][0]>max_m:
#     #         max_m=sums[i][0]
#     #         max_index=i
#     # # print(min_m,min_index)
#     # # print(max_m,max_index)
#     # result=0
#     # for i in range(min_index+1,max_index+1):
#     #     result+=data[i]
#     # return result











print(maxsubArray4(li, len(li)))
# print(maxsubArray3(li,0,len(li)-1))