# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 15:07:18 2020

@author: a8520
"""


# 75. Koko Eating Bananas
# Koko loves to eat bananas.  There are N piles of bananas, 
# the i-th pile has piles[i] bananas.  
# The guards have gone and will come back in H hours.
# Koko can decide her bananas-per-hour eating speed of K.  
# Each hour, she chooses some pile of bananas, and eats K bananas from that 
# pile.  
# If the pile has less than K bananas, she eats all of them instead, 
# and won't eat any more bananas during this hour.
# Koko likes to eat slowly, but still wants to finish eating all the bananas 
# before the guards come back.
# Return the minimum integer K such that she can eat all the bananas within H hours.

# Example 1:
# input: piles = [3,6,7,11], H = 8
# output: 4

# Example 2:
# input: piles = [30,11,23,4,20], H = 5
# output: 30

# Example 3:
# input: piles = [30,11,23,4,20], H = 6
# output: 23


class Solution(object):
    
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        
        def checkTime(K, piles, H):
            import math
            time = 0
            for i in piles:
                time += math.ceil(i/K)
                
            return time <= H
        
        # new_piles = quick_sort(piles)
        
        piles.sort()
        l = 1
        r = max(piles)
        
        while l < r:
            mid = l + (r - l) // 2
            if checkTime(mid, piles, H):
                r = mid
            else:
                l = mid + 1
        
        return l

            
            
test = Solution()
piles = [3,6,7,11]
H = 8
print(test.minEatingSpeed(piles, 8))
            
            
            
            
            
            
            
            
            