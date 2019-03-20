# -- coding: utf-8 --

class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        mid=len(nums)//2
        res=0
        for n in nums:
            res+=abs(n-nums[mid])
        return res
