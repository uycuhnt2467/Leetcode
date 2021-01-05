# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 11:04:28 2021

@author: a8520
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        tempSet = set()
        
        for i in range(len(nums)):
            tempSet.add(nums[i])
            
        min_ = min(tempSet)
        max_ = max(tempSet)
        max_len = 1
        cur = min_
        while cur <= max_: 
            len_ = 0
            while cur in tempSet:
                len_ += 1
                cur += 1
            max_len = max(max_len, len_)
            cur += 1
                
        return max_len