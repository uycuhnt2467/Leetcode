# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 00:04:10 2021

@author: a8520
"""


class Solution:
    def numSubarrayBoundedMax(self, arr, l, r):
        if not arr:
            return -1
        
        i = 0
        
        cum_r = 0
        cur_total = 0
        while i < len(arr) + 1:
            if i == len(arr):
                if cur_total != 0:
                    cum_r += ((1 + cur_total) * (cur_total) / 2)
                break
            if arr[i] <= r:
                cur_total += 1
            else:
                if cur_total != 0:
                    cum_r += ((1 + cur_total) * (cur_total) / 2)
                    cur_total = 0
            i+= 1
        
        cum_l = 0
        cur_total = 0
        i = 0
        while i < len(arr) + 1:
            if i == len(arr):
                if cur_total != 0:
                    cum_l += ((1 + cur_total) * (cur_total) / 2)
                break
            
            if arr[i] < l:
                cur_total += 1
            else:
                if cur_total != 0:
                    cum_l += ((1 + cur_total) * (cur_total) / 2)
                    cur_total = 0
            i+= 1
        
        return int(cum_r - cum_l)
    
sol = Solution()
test = [2, 1, 4, 3]
print(sol.numSubarrayBoundedMax(test, 2, 3))

