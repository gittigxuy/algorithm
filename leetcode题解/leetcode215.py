# -*- coding:utf-8 -*- 
__author__ = 'xuy'

# solution1:
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()

        return nums[-k]

#solution2

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.func(nums, 0, len(nums) - 1, k)

    def func(self, nums, low, high, k):
        while True:
            index = self.patation(nums, low, high)
            if index == k - 1:
                return nums[index]
            if index < k - 1:
                low = index + 1
            else:
                high = index - 1

    def patation(self, input_list, left, right):
        base = input_list[left]
        while left < right:
            # 因为要找第k大的元素，因此划分点由原来的，小于base放到左边，大于base放到右边，
            # 改为大于base放到左边，小于base放到右边
            while left < right and input_list[right] <= base:
                right -= 1
            input_list[left] = input_list[right]
            while left < right and input_list[left] >= base:
                left += 1
            input_list[right] = input_list[left]
        input_list[left] = base
        return left

#solution3,使用堆函数,heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        #返回的是一个降序的结果
        # heapq.nlargest返回一个降序的序列
        # heapq.nsmallest返回一个升序的序列
        return heapq.nlargest(k,nums)[-1]

#solution4,使用大顶堆
class Solution(object):
    def sort(self,data,num_data):
        self.build_heap(data,num_data)
        for i in range(num_data)[::-1]:
            data[0],data[i]=data[i],data[0]
            self.adjust(data,0,i)
        return data


    def build_heap(self,data,num_data):
        for i in range(num_data//2)[::-1]:
            self.adjust(data,i,num_data)

    def adjust(self,data,i,num_data):
        lchild=2*i +1
        rchild=2*i +2
        max=i
        if i<num_data//2:
            if lchild< num_data and data[max] <data[lchild]:
                max=lchild
            if rchild<num_data and data[max]<data[rchild]:
                max=rchild
            if i!=max:
                data[i],data[max]=data[max],data[i]
                self.adjust(data,max,num_data)

    def findkthlarget(self,nums,k):
        self.sort(nums,len(nums))
        return nums[-k]

