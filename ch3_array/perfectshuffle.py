# -*- coding:utf-8 -*- 
__author__ = 'xuy'

import math
# 数组下标从1开始，f是圈的头部，mod为2*n+1
def cycleLeader(a, f, mod):
    # for i in range(f*2%mod,5,2*i/mod)
    i = 2 * f % mod
    while (i != f):
        t = a[i - 1]
        a[i - 1] = a[f - 1]
        a[f - 1] = t
        # print(a[i-1],a[f-1])
        i = 2 * i % mod
        print(a)


#test cycleLeaser
# l2=[1,2,3,4,5,6,7,8,9,10]
# mod=len(l2)+1
# cycleLeader(l2,1,mod)

'''
K个圈：对于2*n=(3^k-1)这种长度的数组，恰好只有k个圈，且每个圈的起始位置分别是1,3,9,...3^(k-1)
对于2n!=(3^k-1)长度的数组,
    找到最大2m=(3^k-1)的部分，且3^k<=2*n<3^(k+1)
    把a[m+1...m+n]部分循环右移m为(循环左移n-m位)
    对每个i=0,1,2,...,k-1,3^i是每个圈的起始位置，做cycleLeader算法
        因为子数组长度为m，所以对2*m+1取模
    对数组的剩余部分A[2m+1...2n]继续使用本算法
'''


def reverseString(s, f, to):
    while (f < to):
        # print(f)
        t = s[f]
        s[f] = s[to]
        s[to] = t
        f += 1
        to -= 1
        # print(s)

##循环左移n-m，第二个参数是字符串长度，第三个参数是循环左移的位数
def leftRotateString(s, n, m):
    m=m%n
    reverseString(s, 0, m - 1)
    reverseString(s, m, n - 1)
    reverseString(s, 0, n - 1)
    # print(''.join(s))
    # print(s)


def perfectShuffle2(a, n):
    # print(n)
    final = []
    while (n > 1):
        #step1，找到2*m=3^k-1,3^k<=2n<3^(k+1)
        #其中,m指的是从n中抽取出m个元素,k表示 k个环
        n2 = n * 2
        m = 1
        k = 0

        #3^k<=2n<3^(k+1)，找出k
        while ((n2 + 1) / m >= 3):
            k += 1
            m *= 3
        m = math.floor(m / 2)
        # print(m)

        #对于字符进行拆分
        t1 = a[:m]
        t2 = a[m:m + n]
        t3 = a[m + n:]

        #step2，我们需要对于t2字符串进行循环左移
        #第一个参数是t2,第二个参数是：一共长度，第三个参数是循环左移n-m位
        leftRotateString(t2, n, n - m)

        i = 0
        t = 1
        #记录循环左移之后的字符串
        a = t1 + t2 + t3
        # print(a)
        # print(k)

        #step3:找到k个cycle
        while (i < k):
            #找出循环圈
            cycleLeader(a, t, m * 2 + 1)
            i += 1
            t *= 3

        #step4,对于剩余的长度为数组2*(n-m)进行递归操作

        #记录最终结果，先记录前2m个元素，剩余2(n-m)个元素
        final += a[:2 * m]
        a = a[2 * m:]
        n -= m
    if n == 1:  # 最后仅剩两个元素时
        t = a[0]
        a[0] = a[1]
        a[1] = t
        final += a
    print(final)


l3 = [1, 2, 3, 4, 5, 6, 7, 8, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# l3=[1,2,3,4,5,'a','b','c','d','e']
perfectShuffle2(l3, int(len(l3) / 2))