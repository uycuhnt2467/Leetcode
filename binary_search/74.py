# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 11:11:37 2020

@author: a8520
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        column = len(matrix[0])
        i = row - 1
        j = 0
        
        while i > -1 and j < column:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
        return False


class BinarySearch(object):
    def binarySearch(self, array, target):
        i = 0
        j = len(array) - 1
        
        while i < j:
            mid = i + (j-i)//2
            if array[mid] == target:
                return True
            elif array[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        if array[j] == target:
            return True
        return False

class Solution2(object):   
    # two binary search
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        if row == 0:
            return False
        
        column = len(matrix[0])
        if column == 0:
            return False
        
        # find row
        i = 0
        j = row - 1
        while i < j:
            mid = i + (j-i)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                j = mid - 1
            else:
                i = mid + 1
        

        if matrix[j][0] == target:
            return True
        elif matrix[j][0] > target:
            row = j - 1
        else:
            row = j
            
        # find column
        k = 0
        l = column - 1
        while k < l:
            mid = k + (l-k)//2
            # print(matrix[row][mid])
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                l = mid - 1
            else:
                k = mid + 1
        if matrix[row][k] == target:
            return True
        return False
        
        

sol = Solution2()
# test = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 3

# test = [[1]]
test = [[1,3]]
target = 3

print(sol.searchMatrix(test, target))