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
    
    def numSubarrayBoundedMax_2(self, arr, l, r):
        if not arr or not l or not r:
            return -1
        cum_l, cum_r = self.helper(arr, l-1), self.helper(arr, r)
        return int(cum_r - cum_l)
        
    def helper(self, arr, max_):
        i = 0 
        cum_ = 0
        cur_total = 0
        while i < len(arr):
            if arr[i] <= max_:
                cur_total += 1
                cum_ += cur_total
            else:
                cur_total = 0
            i+= 1
        return cum_
sol = Solution()
test = [2, 1, 4, 3]
# print(sol.numSubarrayBoundedMax(test, 2, 3))
print(sol.numSubarrayBoundedMax_2(test, 2, 3))

