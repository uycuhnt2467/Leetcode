# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 10:36:37 2021

@author: a8520
"""


class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
        count = 0
        sum_ = 0
        sum_dict = {0:1} # initialize the first sum.
        
        for i in range(len(A)):
            
            # sum_ += (((A[i] % K) + K) % K)
            # if sum_dict.get(sum_) != None:
            #     sum_dict[sum_] += 1
            # else:
            #     sum_dict[sum_] = 1
            sum_ += A[i]
            proc = ((sum_ % K) + K) % K
            if sum_dict.get(proc) != None:
                sum_dict[proc] += 1
            else:
                sum_dict[proc] = 1
        
        for i in sum_dict.keys():
            count += (sum_dict[i] * (sum_dict[i] -1) / 2)
        return count