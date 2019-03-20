# -*- coding:utf-8 -*- 
__author__ = 'xuy'
"""
字符串循环左移k位
"""
"""
方法1：每次左移/右移1次，循环移动k次，时间复杂度O(kN),N为字符串长度
"""
s='13542'
li=list(s)
print(li)
# def left_move(s):
#     tmp=s[0]
#     for i in range(len(s)-1):
#         s[i%len(s)]=s[(i+1)%len(s)]
#     s[-1]=tmp
#     return s
#
# def right_move(s):
#     tmp=s[-1]
#     for i in range(len(s)-1,0,-1):
#         s[i%len(s)]=s[(i-1)%len(s)]
#         # print(i)
#     s[0]=tmp
#     return s
#
#
# for i in range(2):#循环右移2次
#     right_move(li)
# print(li)
# print(''.join(left_move(li)))#将list转化为string

"""
方法2：三次拷贝，需要新开辟一个空间，用来存储需要移动的临时变量
这里需要注意：python下标是左闭右开，长度需要计算好，
时间复杂度O(N),空间复杂度O(k)
"""
# 向左移动k个单位
# k=2
# # T=li[:]
# T=[]
#
# len_li=len(li)
# T[0:k]=li[0:k]#新开辟大小为k的空间,用来存储li中前k个元素
#
# li[0:len_li-k]=li[k:len_li]
#
# li[len_li-k:len_li]=T[0:k]
#
# print(li)

"""
方法3：这种方法在完美洗牌算法中还会遇到，时间复杂度O(N),空间复杂度O(1)
"""
len_li=len(li)
k=2%len_li#左移动2位
# k=len_li-k#右移动2位
def leftmove(li,low,high):
    # 边界判断
    if li is None or low<0 or high<0 or low>=high or len(li)<high+1:
        return
    while low<high:
        # temp=li[low]
        # li[low]=li[high]
        # li[high]=temp
        li[low],li[high]=li[high],li[low]
        low+=1
        high-=1


leftmove(li,0,k-1)
leftmove(li,k,len_li-1)
leftmove(li,0,len_li-1)

print(li)



