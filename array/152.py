# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 08:51:08 2021

@author: a8520
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # max_ = [1]
        # min_ = [1]
        next_max = 1
        next_min = 1
        max_val = nums[0]
        
        for i in range(len(nums)):
            if nums[i] < 0:        
                # next_max = max(nums[i] * min_[i], nums[i])
                # next_min = min(nums[i] * max_[i], nums[i])
                # max_.append(next_max)
                # min_.append(next_min)
                temp_max= next_max
                next_max = max(nums[i] * next_min, nums[i])
                next_min = min(nums[i] * temp_max, nums[i])
            else:
                # next_max = max(nums[i] * max_[i], nums[i])
                # next_min = min(nums[i] * min_[i], nums[i])
                # max_.append(next_max)
                # min_.append(next_min)
                next_max = max(nums[i] * next_max, nums[i])
                next_min = min(nums[i] * next_min, nums[i])
            # max_val = max(max_[-1], max_val)
            max_val = max(next_max, max_val)
        return max_val