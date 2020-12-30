# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 11:33:26 2020

@author: a8520
"""

import unittest
class Solution:

    def checkSecondCondition(self,mid, nums):
        if mid != 0 and mid != len(nums):
            if nums[mid-1] <= nums[mid] and nums[mid] > nums[mid+1]:
                return True
            else:
                return False
        elif mid == len(nums):
            if nums[mid-1] < nums[mid]:
                return True
            else:
                return False
        elif mid == 0:
            if nums[mid] > nums[mid+1]:
                return True
            else:
                return False
        else:
            return True
    
    def search_pivot(self, nums):
       l = 0
       r = len(nums)-1
       mid = l + (r-l)//2
       #  4, 5, 6, 7, 9, 1, 2
       while (nums[l] <= nums[mid] and nums[mid] > nums[r] and self.checkSecondCondition(mid, nums)) != True:
           # print(nums[l] , nums[mid], nums[r])
           if nums[l] > nums[mid]:
               # move left 
               r = mid
           elif nums[mid] > nums[r]:
               # move right
               l = mid
           else:
               mid = -1
               break
           mid = l + (r-l)//2
       return mid
    def binary_search(self, nums, target, l, r):
        mid = l + (r-l)//2
        while mid != r+1:
            if r-l ==1:
                break
            elif nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid         
            else:
                break
            mid = l + (r-l)//2
            
        
        if nums[mid] == target:
            return mid
        elif mid - 1 >= 0 and nums[mid-1] == target:
            return mid-1
        elif mid + 1 < len(nums) and nums[mid+1] == target:
            return mid+1
        else:
            return -1
            
    def search_pos(self, nums, target):
        
        pivot = self.search_pivot(nums)
        if pivot == -1:
            return self.binary_search(nums, target, 0, len(nums))
    
        if nums[pivot] == target:
            return pivot
        elif nums[pivot] > target and nums[0] <= target:
            return self.binary_search(nums, target, 0, pivot)
        else:
            if (nums[-1] < target):
                return -1
            return self.binary_search(nums, target, pivot+1, len(nums))
   

sol = Solution()
test1 = [1]
target = 1
result = sol.search_pos(test1, target)
print(result)

# print(sol.search_pivot(test1))

class TestStringMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.sol = Solution()
    
  
    def test_pivot(self):
        test1 = [2,3,1]
        # print(self.sol.search_pivot(test))
        expected = 1
        result = self.sol.search_pivot(test1)
        self.assertEqual(expected, result, msg="tp1")
    
    def test_pivot2(self):  
        test1 = [10,1,2,3,4,5,6,7,8,9]
        # print(self.sol.search_pivot(test))
        expected = 0
        result = self.sol.search_pivot(test1)
        self.assertEqual(expected, result, msg="Equal")
    def test_pivot3(self):
        test1 = [10,1]
        # print(self.sol.search_pivot(test))
        expected = 0
        result = self.sol.search_pivot(test1)
        self.assertEqual(expected, result, msg="Equal")
    def test_pivot4(self):
        test1 = [1,2,3,4,5,6]
        expected = -1
        result = self.sol.search_pivot(test1)
        self.assertEqual(expected, result, msg="Equal")
    def test_pivot5(self):
        test1 = [2,3,4,5,6, 1]
        expected = 4
        result = self.sol.search_pivot(test1)
        self.assertEqual(expected, result, msg="Equal")
    def test_pivot6(self):
        test1 = [2,3]
        expected = -1
        result = self.sol.search_pivot(test1)
        self.assertEqual(expected, result, msg="Equal")
    
    def test_binary_search1(self):
        test1 = [1,2,3,4,5,6]
        expected = 2
        result = self.sol.binary_search(test1, 3, 0, len(test1))
        self.assertEqual(expected, result, msg="bs1")
    
    def test_binary_search2(self):
        test1 = [1,2,3,4,5,6, 9]
        expected = 2
        result = self.sol.binary_search(test1, 3, 0, len(test1))
        self.assertEqual(expected, result, msg="bs2")
        
    def test_binary_search3(self):
        test1 = [1,2,3,4,5,6, 7, 9, 15]
        expected = 7
        result = self.sol.binary_search(test1, 9, 0, len(test1))
        self.assertEqual(expected, result, msg="bs3")
        
    def test_binary_search4(self):
        test1 = [1,2,3,4,5,6, 7, 9, 15]
        expected = -1
        result = self.sol.binary_search(test1, 8, 0, len(test1))
        self.assertEqual(expected, result, msg="bs4")
    
    def test_search_pos1(self):
        test1 = [4,5,6,7,0,1,2]
        target = 0
        result = self.sol.search_pos(test1, target)
        expected = 4
        self.assertEqual(expected, result, msg="sp1")
    
    def test_search_pos2(self):
        test1 = [4,5,6,7,0,1,2]
        target = 3
        result = self.sol.search_pos(test1, target)
        expected = -1
        self.assertEqual(expected, result, msg="sp2")
    def test_search_pos3(self):
        test1 = [1]
        target = 0
        result = self.sol.search_pos(test1, target)
        expected = -1
        self.assertEqual(expected, result, msg="sp3")
    def test_search_pos4(self):
        test1 = [1]
        target = 1
        result = self.sol.search_pos(test1, target)
        expected = 0
        self.assertEqual(expected, result, msg="sp4")
   
    


# if __name__ == '__main__':
#     unittest.main()