# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 08:58:26 2021

@author: a8520
"""


class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        
        # dynamic programming
        # dp[i][j] = The common max length between A[~i] and B[~j]
        
        dp = [[0 for j in range(len(B)+1)] for i in range(len(A)+1)]
        
        start = 1
        max_ = 0
        while start <= len(A):
            i = start
            j = 1
            while j <= len(B):
                check = dp[i][j-1]
                # while check >= 0:
                #     if A[check] == B[j-1]:
                #         dp[i][j] = check + 1
                #         break
                #     elif check == 0:
                #         dp[i][j] = 0
                #         break
                #     else:
                #         check -= 1
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_ = max(dp[i][j], max_)
                else:
                    dp[i][j] = 0
                j += 1
            start += 1
        
        
        # for i in range(len(dp)):
        #     cur_max = max(dp[i])
        #     if cur_max > max_:
        #         max_ = cur_max
        return max_
            