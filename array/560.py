# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 09:34:52 2021

@author: a8520
"""


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Brute Force
        # count = 0
        # for i in range(len(nums)): #0,1,2
        #     for length in range(1, len(nums)-i+1):
        #         total = 0
        #         for j in range(i, i+length):
        #             total += nums[j]
        #         if total == k:
        #             count += 1
        
        # Hashtable to store the sum
        # Concept: k = sum_ - (sum_ - k)
        # The current sum_ will continue be inserted into the dictionary as
        # the later reference (sum - k).
        #
        #  1  2  3  4  5  6  7  8
        #     |              |
        #    sum-k          sum
        #     ------k---------
        
        count = 0
        sum_ = 0
        sum_dict = {0:1} # initialize the first sum.
        for i in range(len(nums)):
            sum_ += nums[i]
            if sum_dict.get(sum_ - k) != None:
                print(sum_ - k)
                count += sum_dict.get(sum_ - k)
                
            if sum_dict.get(sum_) != None:
                sum_dict[sum_] = sum_dict[sum_] + 1
            else:
                sum_dict[sum_] = 1
                         
        return count