# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 11:04:28 2021

@author: a8520
"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        i = 0
        len_nums = len(nums)
        nums.sort()
        cur_list = []
        return_list = []
        
        def dfs(start, nums, curList, returnList):
            returnList.append(curList[:])
            for i in range(start, len(nums)):
                # if first == True:
                if i > start and nums[i] == nums[i-1] :
                    continue
                curList.append(nums[i])
                dfs(i+1, nums, curList, returnList)
                curList.pop()
        dfs(0, nums, cur_list, return_list)
        return return_list