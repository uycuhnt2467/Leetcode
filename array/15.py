# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 22:04:42 2021

@author: a8520
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 2a + b
        # a + b + c     
        # 2 sum -> x + y = target  y = target - x
        # 3 sum -> x + y + z
        # time complexity: o(n)
        nums.sort()    
        ans = []
        if len(nums) < 3:
            return ans
        fix = 0
        while fix < len(nums) - 2:        
            cur_sum = -nums[fix]
            l = fix + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == cur_sum:
                    ans.append([nums[fix], nums[l], nums[r]])
                    while l < r:
                        l +=1
                        if nums[l] != nums[l-1]:
                            break
                    while l < r:
                        r -=1
                        if nums[r] != nums[r+1]:
                            break
                elif nums[l] + nums[r] > cur_sum:
                    r -= 1
                else:
                    l += 1
            fix += 1
            while nums[fix] == nums[fix-1] and fix < len(nums)-2:
                fix += 1
        return ans