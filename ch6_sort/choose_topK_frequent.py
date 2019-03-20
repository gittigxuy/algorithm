# -*- coding:utf-8 -*- 
__author__ = 'xuy'

"""
topK问题汇总：https://www.cnblogs.com/qlky/p/7512199.html


leetcode347,找出列表当中前k个词频最多的元素
主要思路：我们可以构建一个小顶堆，时间复杂度是：Ｏ(Nlogk)，其中小顶堆大小是K,Ｎ表示一共Ｎ个数

分析一下：

若选用最大堆的话，堆顶是堆的最大值，我们考虑既然要选出从10000万个数里选出前100个最大的数据，我们在建堆的时候，已经考虑了最大堆的特性，那这样的话最大的数据必然在它顶端。
假若真不巧，我开始的前100个数据中已经有这10000个数据中的最大值了，那对于我后面剩余的10000-100的元素再想入堆是不是入不进去了！！！
所以，选用最大堆从10000万个数里选出前100个最大的数据只能找出一个，而不是100个。


那如果选用最小堆的数据结构来解决，最顶端是最小值，再次遇到比它大的值，就可以入堆，入堆后重新调整堆，将小的值pass掉。
这样我们就可以选出最大的前K个数据了。言外之意，假若我们要找出N个数据中最小的前k个数据，就要用最大堆了。
---------------------

原文：https://blog.csdn.net/hanjing_1995/article/details/51539593

"""
# heaqp的用法
#https://www.cnblogs.com/Joyce-song94/p/7149440.html


#代码出处：https://blog.csdn.net/qq_17550379/article/details/80957793
import heapq
#返回前k个高频元素
def topFrequent1(nums,k):
    count_dict={}
    for i in nums:
        #key是ｎｕｍｓ的元素，value是nums的词频
        count_dict[i]=count_dict.get(i,0)+1
    # print (count_dict)
    p=[]
    #遍历字典，i[0]表示字典当中的数值，i[1]表示字典当中的词频
    for i in count_dict.items():
        #找出字典当中的词频,
        # print(i[0],i[1])
        # print(p)
        #如果当前堆的数量等于k，那么就需要判断，是否有元素大于堆顶，如果有的话，那么弹出堆顶
        # 堆满了
        if len(p)==k:
            #如果当前的元素的词频大于堆顶词频，那么将堆顶弹出，然后将当前元素压入堆中
            # p[0][0]表示堆顶的词频
            # print(p)
            if i[1]>p[0][0]:
                heapq.heappop(p)
                heapq.heappush(p,(i[1],i[0]))
        #否则直接插入元素即可
        else:
            #直接压入list，顺序是（词频，元素）
            heapq.heappush(p,(i[1],i[0]))
    # 在heapq.push的时候，换了一下顺序，此时i[1]表示元素，i[0]表示词频
    return [i[1]for i in p]

def topFrequent2(nums,k):
    import heapq
    count_list = dict()
    for i in nums:
        count_list[i] = count_list.get(i, 0) + 1
    p = list()
    #直接压入堆中，然后最后进行筛选，这种空间复杂度是O(N),而不是上面第一种方法，O(K)
    for i in count_list.items():
        heapq.heappush(p, (i[1], i[0]))
    #经过排序之后，找出词频最大的元素，从大到小排序
    #使用了nlargest，免得进行判断了
    return [i[1] for i in heapq.nlargest(k, p)]

nums=[11,11,11,11,11,3,2,5,4,4,3,3,5]
k=3
print(topFrequent1(nums,k))