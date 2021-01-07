# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 14:36:11 2021

@author: a8520
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(nums)
        
        if r == 0:
            return [-1, -1]
        
        while l < r:
            mid = l + (r-l)//2
            
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        if mid >= 0 and mid < len(nums) and nums[mid] == target:
            s = mid
            while s >= 0 and nums[s] == target:
                s -= 1
            e = mid
            while e < len(nums) and nums[e] == target:
                e += 1
            return [s+1, e-1]
        elif mid-1 >= 0 and mid-1 < len(nums) and nums[mid-1] == target:
            s = mid -1
            while s >= 0 and nums[s] == target:
                s -= 1
            e = mid -1
            while e < len(nums) and nums[e] == target:
                e += 1
            return [s+1, e-1]
        elif mid+1 >= 0 and mid+1 < len(nums) and nums[mid+1] == target:
            s = mid +1
            while s >= 0 and nums[s] == target:
                s -= 1
            e = mid +1
            while e < len(nums) and nums[e] == target:
                e += 1
            return [s+1, e-1]
        else:
            return [-1, -1]