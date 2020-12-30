# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:22:15 2020

@author: a8520
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l, r, mid = 1, x, -1
        
        while l < r:
            print(l, r, mid)
            mid = l + (r-l)//2
            if r-l == 1:
                if r**2 > x:
                    return l
                else:
                    return r
            elif mid** 2 > x:
                r = mid
            elif mid **2 == x:
                return mid
            else:
                # mid**2 < x
                l = mid
        
        if mid != -1:
            return mid
        return 1

sol = Solution()

print(sol.mySqrt(8))
# print(sol.mySqrt(1))
