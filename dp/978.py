# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 22:47:57 2021

@author: a8520
"""

# Input: arr = [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]

class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        max_ = 1
        
        if len(arr) == 1:
            return 1
        
        if arr[0] > arr[1]:
            prev_relation = 1
            count = 2
        elif arr[0] < arr[1]:
            prev_relation = -1
            count = 2
        else:
            prev_relation = 0
            count = 1
        if count > max_:
            max_ = count
            
        for i in range(1, len(arr) - 1):
            print("------------")
            print("arr[i]", arr[i])
            print("arr[i+1]", arr[i+1])
            print("prev relation,", prev_relation)
            if arr[i] > arr[i+1]:
                if prev_relation == 1:
                    count = 2
                elif prev_relation == -1:
                    count += 1
                    prev_relation = 1
                else:
                    prev_relation = 1
                    count = 2
            elif arr[i] < arr[i+1]:
                if prev_relation == 1:
                    count += 1
                    prev_relation = -1
                elif prev_relation == -1:
                    count = 2
                else:
                    # prev_relation == 0
                    prev_relation = -1
                    count = 2
            else:
                # arr[i] == arr[i-1]
                count = 1
                prev_relation = 0
            print("cur_count", count)
            if count > max_:
                max_ = count
        return max_

sol = Solution()

arr = [9,4,2,10,7,8,8,1,9]
# arr = [9,9]
arr = [0,1,1,0,1,0,1,1,0,0]
# arr = [37,199,60,296,257,248,115,31,273,176]
print(sol.maxTurbulenceSize(arr))
        