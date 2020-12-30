# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 17:16:41 2020

@author: a8520
"""


# A conveyor belt has packages that must be shipped from one port to another 
# within D days.

# The i-th package on the conveyor belt has a weight of weights[i].  
# Each day, we load the ship with packages on the conveyor belt (in the order 
# given by weights).

# We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on 
# the conveyor belt being shipped within D days.

# Example 1:
# Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
# Output: 15

# Example 2:
# Input: weights = [3,2,2,4,1,4], D = 3
# Output: 6

# Example 3:
# Input: weights = [1,2,3,1,1], D = 4
# Output: 3
class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        def checkDay(w):
            day = 0
            i = 0
            cur_w = w
            while i < len(weights):
                if cur_w - weights[i] >= 0:
                    cur_w -= weights[i]
                    i += 1
                else:
                    day += 1
                    cur_w = w
            day += 1
            return day <= D
        
        l = max(weights)
        r = sum(weights)
        
        while l < r:
            mid = l + (r - l)//2
            if checkDay(mid):
                # can load less
                r = mid
            else:
                # can load more
                l = mid + 1
        return r

sol = Solution()
weights = [1,2,3,4,5,6,7,8,9,10]
D = 5

print(sol.shipWithinDays(weights, D))

sol = Solution()
weights = [3,2,2,4,1,4]
D = 3
print(sol.shipWithinDays(weights, D))        
                    

weights = [1,2,3,1,1]
D = 4
print(sol.shipWithinDays(weights, D))        
        

weights = [2,99]
D = 4
print(sol.shipWithinDays(weights, D))        
        
        
        
        
        
        
        