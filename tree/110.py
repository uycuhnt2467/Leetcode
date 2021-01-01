# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 16:15:26 2021

@author: a8520
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(node):
            if node == None:
                return True, 0
            
            left_balance, left_height = dfs(node.left)
            right_balance, right_height = dfs(node.right)
            
            return left_balance and right_balance and (abs(left_height-right_height) < 2), max(left_height, right_height) + 1
        
        result, _ = dfs(root)
        return result
    
        