# -*- coding:utf-8 -*- 
__author__ = 'xuy'

#1.快排
def partation(data,low,high):
    base=data[low]
    while low<high:
        while low<high and data[high]>=base:
            high-=1
        data[low]=data[high]
        while low<high and data[low]<=base:
            low+=1
        data[high]=data[low]
    data[low]=base
    return low

def quicksort(data,low,high):
    base=partation(data,low,high)
    quicksort(data,low,base-1)
    quicksort(data,base+1,high)

#2。插入排序：
def insert_sort(data,num_data):
    for i in range(1,num_data):
        key=data[i]
        j=i-1
        while j>=0:
            if data[j]>=key:
                data[j+1]=data[j]
                data[j]=key
            j-=1
    return data

#3.冒泡排序
def bubble_sort(data,num_data):
    for i in range(num_data):
        for j in range(i+1,num_data):
            if data[i]>=data[j]:
                data[i],data[j]=data[j],data[i]
    return data

# 4.选择排序：
def select_sort(data,num_data):
    for i in range(num_data):
        min=i
        for j in range(i+1,num_data):
            if data[j]<data[min]:
                min=j
            data[min],data[j]=data[j],data[min]
    return data

# 5.heap sort
def heap_sort(data,num_data):
    build_heapmap(data,num_data)
    for i in range(0,num_data)[::-1]:
        data[i],data[0]=data[0],data[i]
        adjust(data,0,i)
    return data
def build_heapmap(data,num_data):
    for i in range(0,num_data//2)[::-1]:
        adjust(data,i,num_data)
def adjust(data,i,num_data):
    lchild=2*i+1
    rchild=2*i+2
    max=i
    if i<num_data/2:
        if lchild<num_data and data[max]<data[lchild]:
            max=lchild
        if rchild<num_data and data[max]<data[rchild]:
            max=rchild
        if i!=max:#error!!!!,少了这个判断条件
            data[max],data[i]=data[i],data[max]
            adjust(data,max,num_data)

# merge sort:
def merge(left,right):
    i,j=0,0
    result=[]
    while i<len(left) and j <len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def mergesort(data):
    if len(data)<=1:
        return data
    mid=len(data)//2
    left=mergesort(data[:mid])
    right=mergesort(data[mid:])
    return merge(left,right)

