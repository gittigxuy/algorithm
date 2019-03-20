# -*- coding:utf-8 -*- 
__author__ = 'xuy'

"""
字符串全排列问题，需要枚举所有的可能性，因此无论是否递归，时间复杂度都是n!
"""

# s='1234'
s='1223'
li=list(s)
len_li=len(li)
def swap(li,low,high):
    tmp=li[low]
    li[low]=li[high]
    li[high]=tmp
    return li

def isswap(li,low,high):
    bcan=True
    for i in range(low,high):
        #字符串中含有相同的元素，那么就不需要进行全排列，跳过这些元素
        if li[high]==li[i]:
            bcan=False
            break
    return bcan

#递归方法的全排列
def permutation(li,i):
    if li is None:
        return
    #递归输出条件，此时i=4已经完成全排列，需要输出结果,此时li是已经全排列好的结果
    if i==len_li:
        print(li)
        # return
    else:
        # 用来存储是否有重复的数字，初始值０表示没有重复数字
        mark = [0] * 256
        for j in range(i,len(li)):#时间复杂度为O(N)
            #如果字符串含有重复的数字，那么就需要判断是否需要swap,如果是重复的数字的话那就不需要swap，直接continue
            # if not isswap(li,i,j):#需要从头到尾遍历一次，因此时间复杂度为O(N)
            #     continue

            #加了这三行代码，使用哈希的方法，使得时间复杂度降了一个维度
            if mark[int(li[j])]==1:#判断这个字符串中是否有重复的数字，如果有的话continue，直到遇到mask=0
                continue
            # 然后将当前位置位１
            mark[int(li[j])]=1

            swap(li,i,j)
            # li[j],li[i]=li[i],li[j]
            #固定第一位，然后让后面的进行全排列
            permutation(li,i+1)#时间复杂度为f(n-1)
            # li[j], li[i] = li[i], li[j]
            #还原交换后的数据，变为原来的s字符串=1234
            swap(li,i,j)
permutation(li,0)

"""
因此，去重，也就是使用isswap函数调用之后的时间复杂度：
f(n)=n*[f(n-1)+n]=n*f(n-1)+n^2=(n+1)*n!
因此最终的时间复杂度为O((n+1)!),上限是O((n+1)!)
具体推倒看pdf

===============================================
我们可以使用空间换取时间的方法，将第二项n^2变为1，需要开辟一个新的数组来保存已经重复的数字
这样的话，f(n)=n*f(n-1)=O(n!),少了一个维度
"""
