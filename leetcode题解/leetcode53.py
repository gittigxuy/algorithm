# -*- coding:utf-8 -*- 
__author__ = 'xuy'
num_data=[1,-2,3,10,-4,7,2,-5]
li=list(num_data)

#方法一：递归法
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.result(nums, 0, len(nums) - 1)

    def result(self, nums, start, end):
        if start == end:
            return nums[start]
        middle = (start + end) // 2

        left_sum = nums[middle]
        currSum = 0
        for i in range(middle, start - 1, -1):
            currSum += nums[i]
            #在求max的时候不要用函数，需要自己写判断语句，能减少执行时间
            if currSum >= left_sum:
                left_sum = currSum

        right_sum = nums[middle + 1]
        currSum = 0
        for i in range(middle + 1, end + 1):
            currSum += nums[i]
            if currSum >= right_sum:
                right_sum = currSum
        maxSum = left_sum + right_sum
        m1 = self.result(nums, start, middle)
        m2 = self.result(nums, middle + 1, end)

        if m1 >= maxSum:
            maxSum = m1
        if m2 >= maxSum:
            maxSum = m2
        return maxSum
# 方法２：动态规划方法
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=nums[0]
        sum=nums[0]
        for i in range(1,len(nums)):
            if sum>0:
                sum+=nums[i]
            else:
                sum=nums[i]
            result=max(sum,result)
        return result