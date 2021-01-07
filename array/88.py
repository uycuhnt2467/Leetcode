# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 14:57:55 2021

@author: a8520
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        
        # if m == 0:
        #     nums1 = nums2
        #     print(nums1)
        #     return
        if n == 0:
            # return nums1
            return
        l = 0
        n_pointer = 0
        
        while l < m:
            cur_insert = nums2[n_pointer]
            # print(cur_insert)
            while l < m and nums1[l] <= cur_insert:
                l += 1
            if l >= m:
                
                break
            temp = nums1[l]
            nums1[l] = cur_insert
            nums2[n_pointer] = temp
            j = n_pointer
            while j < n-1:
                if nums2[j] > nums2[j+1]:
                    temp2 = nums2[j]
                    nums2[j] = nums2[j+1]
                    nums2[j+1] = temp2
                    j += 1
                else:
                    break      
            l += 1
        for i in range(n):
            nums1[m+i] = nums2[i]
         
                
        # return nums1
                