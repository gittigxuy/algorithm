# -*- coding:utf-8 -*- 
__author__ = 'xuy'

"""
题目说明：无向图加上哪一条边之后，使得图构成环,使用并查集
"""
# 并查集模板
class UnionfindSet:
    def __init__(self,n):
        # 指向父节点
        self._parents = [i for i in range(n + 1)]
        # 秩
        self._ranks = [1 for i in range(n + 1)]
    # 非递归写法
    # def find(self, u):
    #     while u != self._parents[u]:
    #         self._parents[u] = self._parents[self._parents[u]]
    #         u = self._parents[u]
    #     return u
    # 递归写法
    def find(self,u):
        if u!=self._parents[u]:
            self._parents[u]=self.find(self._parents[u])
        return self._parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: return False

        if self._ranks[pu] < self._ranks[pv]:
            self._parents[pu] = pv
        elif self._ranks[pu] > self._ranks[pv]:
            self._parents[pv] = pu
        else:
            self._parents[pv] = pu
            self._ranks[pu] += 1

        return True

    # def __init__(self,n):
    #     # 指向父节点
    #     self._parents=[i for i in range(n+1)]
    #     # 秩
    #     self._rank=[1 for i in range(n+1)]
    # # 进行回溯，找到当前节点的父节点，一直找到根节点
    # def find(self,u):
    #     # 如果当前节点u不是根节点，那么进行回溯
    #     while u!=self._parents[u]:
    #         self._parents[u]=self._parents(self._parents[u])
    #         u=self._parents[u]
    # def union(self,u,v):
    #     root_u,root_v=self.find(u),self.find(v)
    #     if root_u==root_v:
    #         return False
    #     # 此时需要将root_v放到root_u当中
    #     if self._rank[root_u]>self._rank[root_v]:
    #         self._parents[root_v]=root_u
    #     elif self._rank[root_v]>self._rank[root_u]:
    #         self._parents[root_u]=self._rank[root_v]
    #     else:
    #         self._parents[root_u]=self._rank[root_v]
    #         self._rank[root_v]+=1
    #     return True

class Solution:
    def findRedundantConnection(self, edges):
        s = UnionfindSet(len(edges))
        for edge in edges:
            if not s.union(edge[0], edge[1]): return edge
        return None