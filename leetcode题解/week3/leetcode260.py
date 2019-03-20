# -- coding: utf-8 --

"""

也是一个词频统计问题
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict = {}
        result = []
        for i in nums:
            dict[i] = dict.get(i, 0) + 1
        for key in dict:
            # key 表示元素
            # dict[key]表示词频
            if dict[key] == 1:
                result.append(key)
                # print(key)
            # print dict[key]
        return result


