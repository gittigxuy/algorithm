# -*- coding:utf-8 -*- 
__author__ = 'xuy'

"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

荷兰国旗问题

begin=0,current=0,end=len(N)-1
case1:
    if a[current]==2
        swap(a[current],a[end])
        end--
case2:
    if a[current]==1:
        current++
case3:
    if a[current]==0:
        #如果刚开始的情况，那么begin++,current++
        if begin==current:
            begin++
            current++
        else:
            swap(a[current],a[begin])
            begin++


"""


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        # 不返回nums，否则会报错
        """

        begin = 0
        current = 0
        end = len(nums) - 1

        while current <= end:
            if nums[current] == 2:
                nums[current], nums[end] = nums[end], nums[current]
                end -= 1
            elif nums[current] == 1:
                current += 1
            elif nums[current] == 0:
                if begin == current:
                    begin += 1
                    current += 1
                else:
                    nums[current], nums[begin] = nums[begin], nums[current]
                    begin += 1
                    # 这行如果加上的话提高效率
                    # current+=1
        #真正提交的时候注释下一行
        return nums

data=[2,0,2,1,1,0]
solu=Solution()
print(solu.sortColors(data))