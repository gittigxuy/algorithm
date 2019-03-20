# -*- coding:utf-8 -*- 
__author__ = 'xuy'

"""
荷兰国旗问题

问题描述：
给定数组A[0...N-1]，其中元素只能取0,1,2
输出：[0...0,1...1,2....2]

"""

"""
方法1：使用首尾指针的思想
begin=0,current=0,end=len(N)-1
case1:
    if a[current]==2
        swap(a[current],a[end])
        end--
case2:
    if a[current]==1:
        current++
case3:
    if a[current]==0:
        #如果刚开始的情况，那么begin++,current++
        if begin==current:
            begin++
            current++
        else:
            swap(a[current],a[begin])
            begin++
            如果加上current++的话省下一些时间
    
"""
data=[0,0,1,0,2,1,0,1,2,1,1,0]
li=list(data)

# def swap(li,low,high):
#     tmp=li[low]
#     li[low]=li[high]
#     li[high]=tmp
#     return tmp

def Holland(data,num_data):
    begin=0
    end=num_data-1
    current=0
    while(current<=end):
        if(data[current]==2):
            # swap(data,current,end)
            data[current],data[end]=data[end],data[current]
            end-=1
        #只有当data[current]==1的时候，current才能领先于begin,才能触发case3的else条件
        elif(data[current]==1):
            current+=1
        elif(data[current]==0):
            #二者相等的情况是：前面的元素一直为0 的情况
            if begin==current:
                begin+=1
                current+=1
            else:
                # swap(li,current,begin)
                data[current],data[begin]=data[begin],data[current]
                begin+=1
                current+=1
    return data

print(Holland(li,len(li)))


