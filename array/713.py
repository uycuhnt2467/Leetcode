# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 11:04:28 2021

@author: a8520
"""


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # brute
#        subarray = []
#        temparray = []
#             if not nums:
#             return 0
        
#         subarray_count = 0
#         for i in range(1,len(nums) + 1):
#             start = i
#             cur_product = 1
#             for j in range(i):
#                 cur_product *= nums[j]        
#             if cur_product < k:
#                 subarray_count += 1    
#             while start < len(nums):
#                 cur_product /= nums[start - i]
#                 cur_product *= nums[start]
              
#                 if cur_product < k:
#                     subarray_count += 1
#                 start += 1
        # two pointer
        l = 0
        r = 0
        result = 0
        cur_product = 1
        while r < len(nums): 
            cur_product *= nums[r]
            r += 1
            while (l < r) and cur_product >= k:
                cur_product /= nums[l]
                l += 1
            result += (r - l)
        return result