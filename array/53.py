# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 08:51:08 2021

@author: a8520
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [nums[0]]
        cur_max = nums[0]
        for i in range(1, len(nums)):
            next_ = max(nums[i], nums[i] + dp[i-1])
            dp.append(next_)
            if next_ > cur_max:
                cur_max = next_
        return cur_max