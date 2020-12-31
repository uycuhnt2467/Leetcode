# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 16:54:31 2020

@author: a8520
"""


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root == None: return True
        next_layer = [[root]]
        
        while next_layer:
            cur_layer = next_layer.pop()
            start = 0
            end = len(cur_layer) - 1
            while start < end:
                if cur_layer[start] == None and cur_layer[end] == None:
                    pass
                elif cur_layer[start] == None and cur_layer[end] != None:
                    return False
                elif cur_layer[start] != None and cur_layer[end] == None:
                    return False
                else:
                    if cur_layer[start].val != cur_layer[end].val:
                        return False
                start += 1
                end -= 1
            next_ = []
            for i in cur_layer:
                if i == None:
                    next_.append(None)
                    next_.append(None)
                else:
                    next_.append(i.left)
                    next_.append(i.right)
            j = 0
            
            while j < len(next_):
                if next_[j] != None:
                    next_layer.append(next_)
                    break
                j += 1
            if j == len(next_):
                return True
            
            
        return True