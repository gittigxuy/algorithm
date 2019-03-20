# -- coding: utf-8 --

class Solution:
    """
    题目描述：返回矩阵当中第k小的元素
    """
    def kthSmallest(self,matrix,k):
        nums=[]
        for i in len(matrix):
            nums.extend(matrix[i])
        nums.sort()
        return nums[k-1]
