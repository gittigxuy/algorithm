# -*- coding:utf-8 -*- 
__author__ = 'xuy'

"""
最长公共子序列
采用dp的方式解决


2.自底向上的方法
        |-二维的动态规划：
            |-状态LCS(m, n)：表示S1[0...m]和S2[0...n]的最长公共子序列的长度
            |-m, n 为LCS中新增加的两个字符，我们只需要考虑当前新增这两个字符后的状态转移即可。
            |-状态转移方程分为两种情况：
                |-1. S1[m] == S2[n]: LCS(m, n)=1+LCS(m-1,n-1)
                |-2. S1[m] != S2[N]: LCS(m, n)=max(Lcs(m-1, n), LCS(m, n-1))

            |-时间复杂度O(m*n)

"""


# 3 动态规划,空间复杂度是O(M*N)
def dp(S1, S2):
    m = len(S1)
    n = len(S2)
    if m < 0 or n < 0:
        return 0
    # 创建m+1行,n+1列
    memo = [[0] * (n + 1) for j in range(m + 1)]
    flag=[[0]*(n+1)for j in range(m+1)]
    # 初始状态 第0行 第0列 都是0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S1[i - 1] == S2[j - 1]:  # S1中的第i个字符 S2中的第j个字符
                memo[i][j] = 1 + memo[i - 1][j - 1]
                flag[i][j] ='ok'

            else:
                # memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])
                if memo[i - 1][j]>memo[i][j - 1]:
                    memo[i][j]=memo[i - 1][j]
                    flag[i][j]='left'
                else:
                    memo[i][j]=memo[i][j - 1]
                    flag[i][j] = 'up'
    return memo[m][n],flag


S1 = 'AFDZSAFDSAB'
S2 = 'FDWZSAFDB'
print(dp(S1, S2))