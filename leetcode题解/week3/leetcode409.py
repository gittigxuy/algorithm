# -- coding: utf-8 --

class Solution(object):
    def longestPalindrome(self,s):
        maxLen=0
        single=False
        d={}
        for c in s:
            # 统计词频
            d[c]=d.get(c,0)+1
        for key in d:
            if d[key]>=2:
                count=d[key]
                left=d[key]%2
                d[key] = left
                maxLen += count - left
            if not single:
                if d[key] == 1:
                    maxLen += 1
                    single = True
        return maxLen
    def longestPalindrome2(self,s):
        maxLen = 0
        # 判断是否是奇数，默认不是奇数
        odd=0

        d = {}
        for c in s:
            # 统计词频
            d[c]=d.get(c,0)+1
        print(d)
        for key in d:
            maxLen += d[key] & (~1)
            odd |= d[key] & 1
            # print(key)
            # print(d[key])
        return maxLen+odd


solu=Solution()
result=solu.longestPalindrome2('abccccdd')
print(result)


