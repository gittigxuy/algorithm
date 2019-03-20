# -*- coding:utf-8 -*- 
__author__ = 'xuy'
"""
返字符串中匹配模式串的第一个字符下标
"""
str_s="1234567"
str_pattern="23"
#
# def calcNext(str_pattern,next):
#     str_pattern_len=len(str_pattern)
#     next[0]=-1
#     k=-1
#     j=0
#     while(j<str_pattern_len-1):
#
#         if k==-1 or str_pattern[j]==str_pattern[k]:
#             k+=1
#             j+=1
#             next[j]=k
#         else:
#             k=next[k]
#《高效算法》实现方法
def KMP_1(string,pattern):
    assert pattern != ''
    len_string = len(string)
    len_pattern = len(pattern)
    next = [0] * len_pattern
    j = next[0] = -1
    #step1:计算next数组
    for i in range(1,len_pattern):
        #不匹配情况，递归执行计算next数组
        while j>=0 and pattern[i-1]!=pattern[j]:
            j=next[j]
        j+=1
        next[i]=j
    j=0
    # step2:计算匹配字符串的第一个index
    for i in range(len_string):
        # 不匹配情况，递归执行计算next数组
        while j>=0 and string[i]!=pattern[j]:
            j=next[j]
        j+=1
        if j==len_pattern:
            return i-len_pattern+1
    return -1

#视频中c代码转化为python代码
#思路很清晰，用这个代码
def KMP_2(string,pattern):
    assert pattern!=''
    #原串
    len_string=len(string)
    #模式串
    len_pattern=len(pattern)
    next=[0]*len_pattern
    j=next[0]=-1
    i=0
    #step1:使用模式串计算next数组,
    while(i<len_pattern-1):
        """
        此刻注意：j也就是next[i-1],并且pattern[j]表示前缀，pattern[i]表示后缀
        注意：j==-1表示没有找到j前缀与j后缀相等，首次分析可以先忽略
        """
        #如果是初始化或者是前缀和后缀匹配，那么就更新next[i]数组
        if j==-1 or pattern[i]==pattern[j]:
            j+=1
            i+=1
            next[i]=j
        #如果pattern[i]！=pattern[j]，那么继续递归前缀索引pattern[next[j]]
        else:
            j=next[j]
    #step2:重新初始化i,j,然后开始进行模式串与字符串的匹配
    i=0
    j=0
    #step3:使用原串计算匹配字符串的第一个index
    while (i<len_string):
        #如果原串和模式串匹配的话，那么就原串str与模式串pattern一起向后移动
        if j==-1 or string[i]==pattern[j]:
            i+=1
            j+=1
        #如果不匹配的话，那么继续递归前缀索引str_pattern[next[j]]
        else:
            j=next[j]
        #到了模式串的最后，说明已经匹配了，因此返回i-模式串的长度，表示原串当中的起始index
        # 此时j已经指向了匹配串的结尾,i也指向了原串当中模式串的末尾，如果想要返回公共匹配串的起始，需要i-len_pattern
        if j==len_pattern:
            return i-len_pattern

    #没有找到匹配
    return -1


#对于KMP算法的改进，进行了剪枝，更高效的算法
# 如果pattern[i]==pattern[j]，因为string[i]!=pattern[i]那么string[i]!=pattern[j],也就是i和j没有匹配，应该继续滑动next[j],即next[i]=next[j]
def KMP_3(string,pattern):
    assert pattern!=''
    len_string=len(string)
    len_pattern=len(pattern)
    next=[0]*len_pattern
    j=next[0]=-1
    i=0
    #step1:计算next数组
    while(i<len_pattern-1):
        """
        此刻注意：j也就是next[i-1],并且pattern[j]表示前缀，pattern[i]表示后缀
        注意：j==-1表示没有找到j前缀与j后缀相等，首次分析可以先忽略
        """


        """
        未进行剪枝
        #如果是初始化或者是前缀和后缀匹配，那么就更新next[i]数组
        if j==-1 or pattern[i]==pattern[j]:
            j+=1
            i+=1
            next[i]=j
        #如果pattern[i]！=pattern[j]，那么继续递归前缀索引pattern[next[j]]
        else:
            j=next[j]
        
        """
        #如果是初始化或者是前缀和后缀匹配，那么就更新next[i]数组
        if j==-1 or pattern[i]==pattern[j]:
            j+=1
            i+=1
            #i和j没有匹配，在这里进行剪枝
            #因为text[i]!=pattern[j],所以text[i]!=pattern[i]
            if pattern[i]==pattern[j]:
                next[i]=next[j]
            else:
                next[i]=j
        #如果pattern[i]！=pattern[j]，那么继续递归前缀索引pattern[next[j]]
        else:
            j=next[j]
    #step2:重新初始化i,j,然后开始进行模式串与字符串的匹配
    i=0
    j=0
    #计算匹配字符串的第一个index
    while (i<len_string):
        #如果匹配的话，那么就原串str与模式串pattern一起向后移动
        if j==-1 or str_s[i]==str_pattern[j]:
            i+=1
            j+=1
        #如果不匹配的话，那么继续递归前缀索引pattern[next[j]]
        else:
            j=next[j]

        if j==len_pattern:
            return i-len_pattern

    #没有找到匹配
    return -1



print(KMP_3(str_s,str_pattern))


