# -*- coding:utf-8 -*- 
__author__ = 'xuy'

class Solution:
    def coinChange(self,coins,amount):
        dp=[-1]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            for j in range(len(coins)):
                if i >= coins[j] and dp[i-coins[j]]!=-1:
                    if dp[i]==-1 or dp[i]>dp[i-coins[j]]+1:
                        dp[i]=dp[i-coins[j]]+1
        return dp[amount]


solu=Solution()
coins=[1,2,5]
amount=11


print(solu.coinChange(coins,amount))