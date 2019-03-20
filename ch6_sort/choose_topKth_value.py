# -*- coding:utf-8 -*- 
__author__ = 'xuy'

"""
找出第k大的元素:leetcode215
reference:https://blog.csdn.net/u012501459/article/details/46822007
python heapq
https://blog.csdn.net/xx_123_1_rj/article/details/80819850
一共有三种方法，最优解是基于快速排序的划分思想
"""


def partition(input_list, left, right):
    '''
    函数说明:根据left和right进行一次扫描，重新找到基准数
    Author:
        www.cuijiahua.com
    Parameters:
        input_list - 待排序列表
        left - 左指针位置
        right - 右指针位置
    Returns:
        left - 新的基准数位置
    '''
    base = input_list[left]
    while left < right:
        while left < right and input_list[right] >= base:
            right -= 1
        input_list[left] = input_list[right]
        while left < right and input_list[left] <= base:
            left += 1
        input_list[right] = input_list[left]
    input_list[left] = base
    # 返回划分点
    return left
#使用快速排序，时间复杂度是O(NlogN),其实可以使用num.sort()，也是快速排序
def quicksort(num, low, high):  # 快速排序
    if low < high:
        location = partition(num, low, high)
        quicksort(num, low, location - 1)
        quicksort(num, location + 1, high)
    return num


#使用快速排序的划分思想，时间复杂度是O(N)，找到划分点，不需要继续递归完成全部排序过程
def partition_change(input_list, left, right):
    '''
    函数说明:根据left和right进行一次扫描，重新找到基准数
    Author:
        www.cuijiahua.com
    Parameters:
        input_list - 待排序列表
        left - 左指针位置
        right - 右指针位置
    Returns:
        left - 新的基准数位置
    '''
    base = input_list[left]
    while left < right:
        #因为要找第k大的元素，因此划分点由原来的，小于base放到左边，大于base放到右边，
        # 改为大于base放到左边，小于base放到右边
        while left < right and input_list[right] <= base:
            right -= 1
        input_list[left] = input_list[right]
        while left < right and input_list[left] >= base:
            left += 1
        input_list[right] = input_list[left]
    input_list[left] = base
    return left

#使用快速排序的划分的思想
def findkth(num, low, high, k):  # 找到数组里第k个数

    """
    递归版本时间超时
    index = partition_change(num, low, high)
    #挑选出第k大的元素，说明有k-1个元素比该元素大，这里的index是从０开始的
    if index == k-1:
        return num[index]
    # 此时,index左边都是比该元素大的，右边都是比该元素小的
    # 因此需要向右递归
    if index < k-1:
        return findkth(num, index + 1, high, k)
    else:
        return findkth(num, low, index - 1, k)


    """

    #非递归版本
    while True:
        index=partition_change(num, low, high)
        if index==k-1:
            return num[index]
        if index<k-1:
            low=index+1
        else:
            high=index-1



# def findKth_heapq(nums,K):
#     import heapq
#     count_dict = {}
#     for i in nums:
#         # key是ｎｕｍｓ的元素，value是nums的词频
#         count_dict[i] = count_dict.get(i, 0) + 1
#     # print (count_dict)
#     p = []
#     for i in count_dict.items():
#         # 找出字典当中的词频
#         # print(i[0],i[1])
#         # 如果当前堆的数量等于k，那么就需要判断，是否有元素大于堆顶，如果有的话，那么弹出堆顶
#         if len(p) == k:
#             # 如果当前的元素大于堆顶，那么将堆顶弹出，然后将当前元素压入堆中
#             # print(p[0])
#             if i[1] > p[0][0]:
#                 heapq.heappop(p)
def findKth_heapq(nums,K):
    import heapq
    return heapq.nlargest(k,nums)[-1]

# pai = [2, 3, 1, 5, 4, 6]
k=4
# pai=[3,2,1,5,6,4]
pai = [3,2,3,1,2,4,5,5,6]
print(findKth_heapq(pai,k))
# quicksort(pai, 0, len(pai) - 1)
# print(pai[-k])

# print(findkth(pai, 0, len(pai) - 1, 4))