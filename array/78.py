# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 11:04:28 2021

@author: a8520
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        returnList = [[]]
        len_nums = len(nums)
        i = 0
        while i < len_nums:
            cur_returnList_len = len(returnList)
            j = 0
            while j < cur_returnList_len:
                returnList.append(returnList[j][:])
                returnList[-1].append(nums[i])
                j += 1
            i += 1
        return returnList