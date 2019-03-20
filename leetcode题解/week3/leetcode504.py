# -- coding: utf-8 --

class Solution(object):
    def convertToBase7(self, num):
        if num==0:
            return "0"
        res=''
        n=abs(num)
        while n:
            res=str(n%7)+res
            n//=7
        return res if num>0 else '-'+res