# -*- coding:utf-8 -*- 
__author__ = 'xuy'


class Solution(object):
    def findKthLargest1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        return self.findKth(nums, low, high, k)

    def findKth(self, nums, low, high, k):
        index = self.partation(nums, low, high)
        if index == k - 1:
            return nums[index]
        elif index < k - 1:
            return self.findKth(nums, index + 1, high, k)
        else:
            return self.findKth(nums, low, index - 1, k)

    def partation(self, nums, low, high):
        base = nums[low]
        while low < high:
            while low < high and nums[high] <= base:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] >= base:
                low += 1
            nums[high] = nums[low]
        nums[low] = base
        return low
    # 采用堆排序的方式：reference:https://blog.csdn.net/XX_123_1_RJ/article/details/80819850
    # def findKthLargest2(self, nums, k):


    def findKthLargest3(self, nums, k):
        return sorted(nums)[-k]

    def findKthLargest4(self,nums,k):
        import heapq
        return heapq.nlargest(k,nums)[-1]


nums=[2,3,4,5,1,32,12,51,24,13]
solu=Solution()
print(solu.findKthLargest1(nums,2))
print(solu.findKthLargest3(nums,2))
print(solu.findKthLargest4(nums,2))
