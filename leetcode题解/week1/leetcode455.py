# -*- coding:utf-8 -*- 
__author__ = 'xuy'

class solution:
    def findContentChildren(self,g,s):
        """
        总结：一般贪心算法使用排序，取当前的最优解
        :param g: 表示孩子的胃口
        :param s: 表示饼干的大小
        :return: result,表示饼干的大小可以满足多少孩子的胃口，返回孩子的数量
        """
        g.sort(reversed=True)
        s.sort(reversed=True)
        g_index,s_index,result=0,0,0
        while g_index<len(g) and s_index <len(s):
            # 饼干大小满足孩子的胃口
            if s[s_index]>=g[g_index]:
                result+=1
                s_index+=1
                g_index+=1
            # 如果饼干大小不满足孩子的胃口，那么遍历下一个孩子的胃口
            else:
                g_index+=1
        return result