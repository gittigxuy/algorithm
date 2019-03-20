# -*- coding:utf-8 -*- 
__author__ = 'xuy'

"""
字符串全排列非递归，leetcode31题,提交一下


"""

#方法一：使用sort函数，对于【i+1，len(li)-1】进行排序
# s='1234'
s='1223'
li=list(s)
len_li=len(li)
def my_reverse(li, low, high):
    while (low < high):
        li[low],li[high]=li[high],li[low]
        low += 1
        high -= 1

    return li[low:high + 1]
# def nextpermutation(li):
#     if len(li)<=1:
#         return
#     #这种遍历的好处是：i+1肯定不越界
#     for i in range(len(li)-2,-1,-1):
#         #从后往前找，找到最后一个生序的index
#         if li[i]<li[i+1]:
                #从最后一个元素开始遍历
#             for k in range(len(li)-1,i,-1):
#                 #如果当前值li[k]>之前已经找到的li[i],也就是从i+1到len(li)-1当中找到比li[i]大的最小值
#                 if li[k]>li[i]:
#                     swap(li,i,k)
#                     li[i+1:]=sorted(li[i+1:])#使用了排序，时间复杂度至少o(nlogn),从小到大进行排序
#                     # li[i+1:]=reverse(li,i+1,len(li)-1)
#                     break
#             break
#         else:
#             if i==0:
#                 li.sort()
# 时间慢的原因是：使用了一个sort函数
# Runtime: 40 ms, faster than 23.90% of Python online submissions for Next Permutation.

#方法2：使用list当中自带的翻转函数reversed
def nextPermutation(self, li):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if len(li) <= 1:
        return
    # 从倒数第二个元素开始往前遍历
    for i in range(len(li) - 2, -1, -1):

        if li[i] < li[i + 1]:
            for k in range(len(li) - 1, i, -1):

                if li[k] > li[i]:
                    # swap(li, i, k)
                    li[i],li[k]=li[k],li[i]
                    #进行了就地逆置,reversed返回一个地址，需要对于其返回值进行赋值
                    li[i+1:]=reversed(li[i+1:])
                    break
            break
        else:
            #从头到尾开始逆置
            if i == 0:
                li[:] = reversed(li[:])

#方法3：不使用sort函数，而是使用自定义逆置函数
# Runtime: 32 ms, faster than 82.87% of Python online submissions for Next Permutation.
# def nextPermutation(self, li):
#     """
#     :type nums: List[int]
#     :rtype: void Do not return anything, modify nums in-place instead.
#     """
#     if len(li) <= 1:
#         return
#
#     for i in range(len(li) - 2, -1, -1):
#
#         if li[i] < li[i + 1]:
#             for k in range(len(li) - 1, i, -1):
#
#                 if li[k] > li[i]:
#                     swap(li, i, k)
#                     #进行了就地逆置
#                     my_reverse(li, i + 1, len(li) - 1)
#                     break
#             break
#         else:
#             #从头到尾开始逆置
#             if i == 0:
#                 my_reverse(li, i, len(li) - 1)