# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 11:11:47 2021

@author: a8520
"""


# 792. Number of Matching Subsequences
class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        if not S or not words:
            return -1
        
        pos_dict = {}
        for idx, char in enumerate(S):
            if char not in pos_dict:
                pos_dict[char] = list()
                pos_dict[char].append(idx)
            else:
                pos_dict[char].append(idx)
                
        count = 0
        for word in words:
            if self.find_word(pos_dict, word):
                count += 1
        return count
        
    def find_word(self, pos_dict, word):
        # brutal
        i = 0
        for idx, char in enumerate(word):
            if idx == 0:
                if char in pos_dict:
                    i = pos_dict[char][0]
                else:
                    return False
            else:
                if char in pos_dict:
                    temp_list = pos_dict[char]
                    j = 0
                    while j < len(temp_list):
                        if temp_list[j] > i:
                            i = temp_list[j]
                            break
                        else:
                            j += 1
                            if j == len(temp_list):
                                return False
                else:
                    return False
        return True
    
    def numMatchingSubseq_2(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        if not S or not words:
            return -1
        
        pos_dict = {}
        for idx, char in enumerate(S):
            if char not in pos_dict:
                pos_dict[char] = list()
                pos_dict[char].append(idx)
            else:
                pos_dict[char].append(idx)
                
        count = 0
        for word in words:
            print(pos_dict)
            if self.find_word_2(pos_dict, word):
               
                count += 1
                
        return count
    
    def find_word_2(self, pos_dict, word):
        # binary search
        i = -1
        for idx, char in enumerate(word):
            print("idx", idx)
            print("cur i", i)
            if idx == 0:
                if char in pos_dict:
                    i = pos_dict[char][0]
                else:
                    return False
            else:
                if char not in pos_dict:
                    print("not in char", char)
                    return False
                else:
                    temp_list = pos_dict[char]
                    print("i", i)
                    print("char", char)
                    print("temp_list", temp_list)
                    i = self.binary_search(temp_list, i)
                    if i == -1:
                        print("not in char 2", char)
                        print(word)
                        return False
                
        return True
    
    def binary_search(self, temp_list, i):
        total_len = len(temp_list)
        l = 0
        r = len(temp_list)
        while l < r:
            mid = l + (r-l)//2
            if temp_list[mid] == i:
                if mid + 1 < total_len:
                    return temp_list[mid+1]
                else:
                    return -1
            elif temp_list[mid] > i:
                r = mid
            else:
                # temp_list[mid] < i
                if mid + 1 < total_len and temp_list[mid+1] > i:
                    return temp_list[mid+1]
                else:
                    l = mid + 1
        if temp_list[mid] > i:
            return mid
        return -1
            

sol = Solution()
S = "abcde"
words = ["a", "bb", "acd", "ace"]
# words = ["acd"]
print(sol.numMatchingSubseq(S, words))
print(sol.numMatchingSubseq_2(S, words))