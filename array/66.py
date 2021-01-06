# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 10:38:06 2021

@author: a8520
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        init_len = len(digits) - 1
        i = len(digits) - 1
        prev = 0
        while i > -1:
            if i == init_len:
                temp = digits[i] + 1
            else:
                temp = digits[i] + prev
                
            prev = 0
            if temp < 10:
                digits[i] = temp
                break
            else:
                digits[i] = temp % 10
                prev = 1
                if i == 0:
                    digits.insert(0, 1)
            i -= 1
        return digits