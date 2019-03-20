# -- coding: utf-8 --


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict={}
        result=[]
        for i in nums:
            dict[i] = dict.get(i, 0) + 1

        return max(dict.items(),key=lambda x:x[1])[0]

    def majorityElement2(self, nums):
        return sorted(nums)[len(nums) // 2]

solu=Solution()
result=solu.majorityElement2([2,2,3,1,2,2])
print(result)